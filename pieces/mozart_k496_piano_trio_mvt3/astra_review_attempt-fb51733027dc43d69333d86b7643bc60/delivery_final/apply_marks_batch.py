"""Apply frozen dependent notation to batch02, retaining exact addressed payloads."""
from pathlib import Path
from lxml import etree as E
from fractions import Fraction as F
from copy import deepcopy
import json,re,hashlib
R=Path(__file__).resolve().parent.parent;D=R/'delivery_final'
h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
cs=json.load(open(R/'reviewer/phase3_review.json'))['correction_targets'];batch=json.load(open(D/'correction_batch_02.json'));src=D/batch['working_xml'];assert h(src)==batch['working_xml_sha256'];tree=E.parse(str(src));nodes={n.get('id'):n for n in tree.findall('.//note')};tim=json.load(open(D/'correction_batch_02_checks.json'))['timeline'];records=[];pending=[];DIV=96

def child(n,t):
 x=n.find(t)
 if x is None:x=E.SubElement(n,t)
 return x
def put(n,t,v):
 if v is None:
  for e in n.findall(t):n.remove(e)
 else:child(n,t).text=str(v)
def pitch(n,p):
 m=re.fullmatch(r'([A-G])([#b]*)(-?\d+)',p);assert m,p;x=child(n,'pitch');put(x,'step',m[1]);a=m[2].count('#')-m[2].count('b');put(x,'alter',a if a else None);put(x,'octave',m[3])
def beam(t,l,v):
 n=nodes[t]
 for x in n.findall('beam'):
  if x.get('number','1')==str(l):n.remove(x)
 if v is not None:E.SubElement(n,'beam',number=str(l)).text=v
slur_pairs=[]
def span(a,tag='slur'):
 s=a['start'];t=a['stop'];assert s in nodes and t in nodes,(s,t)
 for typ,nt in [('start',s),('stop',t)]:
  attrs={'type':typ}
  for k in ['placement','orientation']:
   if k in a:attrs[k]=a[k]
  if tag=='tied':
   if not any(x.get('type')==typ for x in nodes[nt].findall('tie')):E.SubElement(nodes[nt],'tie',type=typ)
  else:attrs['number']='1'
  x=E.SubElement(child(nodes[nt],'notations'),tag,**attrs)
  if tag=='slur':slur_pairs.append((s,t,typ,x))
def direction(anchor,a,kind):
 n=nodes[anchor];m=n.getparent();di=E.Element('direction',placement=a.get('placement','below'));dt=E.SubElement(di,'direction-type');v=a.get('value',a.get('dynamic',a.get('words',a.get('text'))));assert v is not None,a
 if kind=='dynamics':E.SubElement(E.SubElement(dt,'dynamics'),v)
 else:E.SubElement(dt,'words').text=v
 desired=F(a.get('onset_q',tim[anchor]['onset_q']));at=F(tim[anchor]['onset_q']);off=(desired-at)*DIV
 if off:assert off.denominator==1;put(di,'offset',int(off))
 if 'voice' in a:put(di,'voice',a['voice'])
 put(di,'staff',a.get('staff',n.findtext('staff','1')));m.insert(m.index(n),di);return di

def clef(c):
 a=c['after'];ts=c['targets'];target=ts[0]
 if target.startswith('P'):
  g=re.search(r'(P\d+).*?(?:m|measure)(\d+)',target);pid,bar=g[1],str(int(g[2]));staff='2'
 else:pid=tim[target]['part'];bar=tim[target]['measure'];staff=nodes[target].findtext('staff','1')
 m=tree.find(f"part[@id='{pid}']/measure[@number='{bar}']");found=[x for x in m.findall('attributes/clef') if x.get('number','1')==staff];assert len(found)==1,(c['id'],len(found));x=found[0];x.getparent().remove(x)
 if isinstance(a,dict):
  for k in ['sign','line']:
   if k in a:put(x,k,a[k])
  if 'onset_q' in a:on=F(a['onset_q'])
  elif 'before' in a:on=F(tim[a['before']]['onset_q'])
  else:on=F(tim[a['after']]['onset_q'])+F(tim[a['after']]['duration_q'])
 else:on=F(a)
 # Insert clef at an exact stream position, restoring cursor after attributes.
 cur=F(0);pos=len(m)
 for i,e in enumerate(m):
  if e.tag=='note' and e.find('chord') is None and cur>=on:pos=i;break
  if e.tag=='note' and e.find('chord') is None:cur+=F(int(e.findtext('duration','0')),DIV)
  elif e.tag in ('backup','forward'):cur+=F(int(e.findtext('duration')),DIV)*(-1 if e.tag=='backup' else 1)
 q=on-cur;els=[]
 if q:
  e=E.Element('forward' if q>0 else 'backup');put(e,'duration',int(abs(q)*DIV));els.append(e)
 e=E.Element('attributes');e.append(x);els.append(e)
 if q:
  e=E.Element('backup' if q>0 else 'forward');put(e,'duration',int(abs(q)*DIV));els.append(e)
 for j,e in enumerate(els):m.insert(pos+j,e)
 return m

def snapshot(ts):return {t:E.tostring(nodes[t],encoding='unicode') for t in ts if t in nodes}
for p in batch['pending']:
 c=cs[p['index']];attr=p['attribute'];a=c['after'];ts=c['targets'];before=snapshot(ts);extra=[]
 if attr=='replacement_embedded_marks':
  payload=p['payload']['payload'];ids=p['payload']['new_event_ids'];main=[t for t in ids if '-v2-' not in t];regular=[t for t in main if nodes[t].find('grace') is None]
  for group in payload.get('beams',[]):
   groupids=[regular[i-1] for i in group];level=2 if all(nodes[t].findtext('type')=='16th' for t in groupids) else 1
   for j,t in enumerate(groupids):
    for l in range(1,level+1):beam(t,l,'begin' if j==0 else 'end' if j==len(groupids)-1 else 'continue')
  for start,stop in payload.get('slurs',[]):span({'start':regular[start-1],'stop':regular[stop-1]})
  if 'lower_slur' in payload:span(dict(zip(['start','stop'],payload['lower_slur'])))
  for k,typ in [('tie_start','start'),('tie_stop','stop')]:
   if k in payload:
    t=payload[k];E.SubElement(nodes[t],'tie',type=typ);E.SubElement(child(nodes[t],'notations'),'tied',type=typ)
  if 'beam' in payload:
   ba=payload['beam']
   for j,ev in enumerate(ba['events']):
    for k,v in ba.items():
     if k.startswith('level'):beam(regular[ev-1],int(k[5:]),v[j])
  if 'text' in payload:extra.append(direction(payload['text']['anchor'],payload['text'],'words'))
  ts=ids
 elif attr=='beam/stem':
  if 'groups' in a:
   groups=[[next(t for t in ts if re.search(r'-e0*'+str(i)+r'$',t)) for i in g] for g in a['groups']]
   for g in groups:
    for j,t in enumerate(g):
     for l in range(1,a['levels']+1):beam(t,l,'begin' if j==0 else 'end' if j==len(g)-1 else 'continue')
  else:
   levels={int(k[5:]):v for k,v in a.items() if k.startswith('level') and k!='levels'}
   if 'levels' in a:
    for l in range(1,a['levels']+1):levels[l]=a['values']
   for l,vs in levels.items():
    for j,t in enumerate(ts):beam(t,l,vs.get(t) if isinstance(vs,dict) else vs[j])
  for t in ts:put(nodes[t],'stem',a['stem'])
 elif attr=='beam[2]':
  for j,t in enumerate(ts):beam(t,2,a['values'][j] if isinstance(a,dict) else a)
 elif attr=='beam[2,3]':
  for l in a['levels']:
   for j,t in enumerate(ts):beam(t,l,a['values'][j])
 elif attr=='notations/slur':span(a)
 elif attr in ('tie+tied','tie/notations/tied','tie/tied','tie/tied/pitch'):
  if a is None:
   for t in ts:
    for x in nodes[t].findall('tie')+nodes[t].findall('notations/tied'):x.getparent().remove(x)
  else:
   for sa in a if isinstance(a,list) else [a]:
    if 'destination_pitch' in sa:pitch(nodes[sa['stop']],sa['destination_pitch'])
    span(sa,'tied')
 elif attr in ('notations/tuplet','tuplet'):
  start=a.get('start',ts[0]);stop=a.get('stop',ts[-1]);assert start in nodes and stop in nodes
  if attr=='tuplet':
   for t in ts:
    tm=child(nodes[t],'time-modification');put(tm,'actual-notes',a['actual']);put(tm,'normal-notes',a['normal'])
  for typ,t in [('start',start),('stop',stop)]:
   at={'type':typ,'number':'1'}
   for k in ['bracket','placement','show-number']:
    if k in a:at[k]=a[k]
   if 'show_number' in a:at['show-number']=a['show_number']
   E.SubElement(child(nodes[t],'notations'),'tuplet',**at)
 elif attr=='voice':
  for t in ts:
   if t not in nodes:continue
   if isinstance(a,str):v=a
   elif 'G5' in a:v=a['G5'] if nodes[t].findtext('pitch/step')=='G' and nodes[t].findtext('pitch/octave')=='5' else a['other']
   elif 'held_D4' in a:v=a['held_D4'] if nodes[t].findtext('pitch/step')=='D' and nodes[t].findtext('pitch/octave')=='4' and F(tim[t]['duration_q'])==2 else a['melody']
   else:v='6' if t in a['voice6'] else '5';assert t not in a['delete']
   put(nodes[t],'voice',v)
 elif attr in ('direction','direction/dynamics','direction/words'):
  kind='dynamics' if 'dynamic' in a or a.get('type')=='dynamics' or attr=='direction/dynamics' else 'words';extra.append(direction(ts[0],a,kind))
 elif attr in ('clef_position','attributes/clef-position','onset_q'):
  m=clef(c);extra.append(m)
 elif attr=='barline/right':
  pid,bar=ts[0].split(':m');m=tree.find(f"part[@id='{pid}']/measure[@number='{int(bar)}']");bl=m.find("barline[@location='right']")
  if bl is None:bl=E.SubElement(m,'barline',location='right')
  put(bl,'bar-style',a['bar-style']);extra.append(bl)
 elif attr=='accidental':
  for t in ts:put(nodes[t],'accidental',a)
 elif attr=='pitch':
  for t in ts:pitch(nodes[t],a)
 elif attr=='notations/fermata':
  for t in ts:E.SubElement(child(nodes[t],'notations'),'fermata',type=a.get('type','upright')).text=a.get('shape','normal')
 elif attr=='notations/ornaments':
  for t in ts:
   orn=child(child(nodes[t],'notations'),'ornaments');E.SubElement(orn,a['type'])
   if a.get('accidental-mark'):
    ac=a['accidental-mark'];E.SubElement(orn,'accidental-mark',placement=ac.get('placement','below')).text=ac['value']
 else:pending.append(p);continue
 records.append({'index':p['index'],'id':c['id'],'attribute':attr,'before_xml':before,'after_xml':snapshot(ts),'added_or_relocated_xml':[E.tostring(e,encoding='unicode') for e in extra],'source_inspection':c['inspection_record'],'source_evidence':c['source_evidence'],'print_reason':c['print_reason'],'interpretation_status':c['status'],'status':'APPLIED_TO_PARTIAL_WORKING_XML'})
# Distinct overlapping slurs receive reusable MusicXML numbers within their part.
pairs={}
for s,t,typ,x in slur_pairs:pairs.setdefault((s,t),[]).append((typ,x))
active={};alloc=[]
def loc(t):return (int(tim[t]['measure']),F(tim[t]['onset_q']),0 if nodes[t].find('grace') is not None else 1)
for (s,t),els in sorted(pairs.items(),key=lambda it:(tim[it[0][0]]['part'],loc(it[0][0]),loc(it[0][1]))):
 pid=tim[s]['part'];busy=active.setdefault(pid,{});busy={n:end for n,end in busy.items() if end>loc(s)};num=next(n for n in range(1,1000) if n not in busy);busy[num]=loc(t);active[pid]=busy
 for _,x in els:x.set('number',str(num))
 alloc.append({'start':s,'stop':t,'number':num})
seq=['grace','cue','chord','pitch','unpitched','rest','duration','tie','instrument','footnote','level','voice','type','dot','accidental','time-modification','stem','notehead','notehead-text','staff','beam','notations','lyric','play','listen']
for n in nodes.values():
 kids=list(n)
 for x in kids:n.remove(x)
 for x in sorted(kids,key=lambda x:seq.index(x.tag) if x.tag in seq else 999):n.append(x)
f=D/'UNVERIFIED_notation_partial.musicxml';tree.write(str(f),encoding='utf-8',xml_declaration=True,pretty_print=True)
# Every note retains exact timing. This is application verification, not Phase5.
actual={}
for part in E.parse(str(f)).findall('part'):
 div=1
 for m in part.findall('measure'):
  cur=F(0);last=F(0)
  for e in m:
   if e.tag=='attributes' and e.find('divisions') is not None:div=int(e.findtext('divisions'))
   elif e.tag in ('backup','forward'):cur+=F(int(e.findtext('duration')),div)*(-1 if e.tag=='backup' else 1)
   elif e.tag=='note':
    on=last if e.find('chord') is not None else cur;dur=F(int(e.findtext('duration','0')),div);actual[e.get('id')]={'part':part.get('id'),'measure':m.get('number'),'onset_q':str(on),'duration_q':str(dur)}
    if e.find('chord') is None:last=cur;cur+=dur
assert actual==tim
save(D/'correction_batch_03.json',{'schema':'astra_correction_batch.v1','complete':True,'primary_complete':False,'source_xml_sha256':h(src),'working_xml':f.name,'working_xml_sha256':h(f),'applied':records,'pending':pending})
save(D/'correction_batch_03_checks.json',{'schema':'astra_correction_batch_checks.v1','scope':'Application verification; not Phase5','working_xml_sha256':h(f),'applied_operations':len(records),'pending':len(pending),'note_timing_unchanged':True,'slur_number_assignments':alloc,'note_count':len(nodes),'requires_remaining_work':['Review implementation fidelity against every frozen payload, especially compound replacement marks','Minimize continuous voice topology; preserve cross-staff lines','Check per-member chord voice/stems and note-local payloads after rebuilding','Write correction ledger and primary checkpoint before Phase5']})
print(len(records),'operations applied;',len(pending),'pending')
