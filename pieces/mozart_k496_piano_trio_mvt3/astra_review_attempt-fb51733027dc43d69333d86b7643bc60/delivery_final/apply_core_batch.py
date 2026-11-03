"""Apply frozen core proposals to an exact rational timeline; never certifies delivery."""
from pathlib import Path
from lxml import etree as E
from fractions import Fraction as F
from copy import deepcopy
import json,re,hashlib,os
R=Path(__file__).resolve().parent.parent;D=R/'delivery_final'
h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
cs=json.load(open(R/'reviewer/phase3_review.json'))['correction_targets'];b1=json.load(open(D/'correction_batch_01.json'));src=D/b1['working_xml'];assert h(src)==b1['working_xml_sha256']
tree=E.parse(str(src));nodes={};tim={};measure={};other={};divs={};order={};changed=set();records=[];deferred=[]
def put(n,t,v):
 x=n.find(t)
 if v is None:
  if x is not None:n.remove(x)
 else:
  if x is None:x=E.SubElement(n,t)
  x.text=str(v)
def child(n,t):
 x=n.find(t)
 if x is None:x=E.SubElement(n,t)
 return x
def remove(n,*tags):
 for tag in tags:
  for x in n.findall(tag):n.remove(x)
def pitch(n,p):
 remove(n,'pitch','rest')
 if p=='R':E.SubElement(n,'rest');return
 m=re.fullmatch(r'([A-G])([#b]*)(-?\d+)',p);assert m,p
 x=E.SubElement(n,'pitch');put(x,'step',m[1]);a=m[2].count('#')-m[2].count('b');put(x,'alter',a if a else None);put(x,'octave',m[3])
for part in tree.findall('part'):
 div=1
 for m in part.findall('measure'):
  key=(part.get('id'),m.get('number'));measure[key]=m;other[key]=[]
  cur=F(0);last=F(0)
  for i,e in enumerate(m):
   if e.tag=='attributes' and e.find('divisions') is not None:div=int(e.findtext('divisions'))
   if e.tag in ('backup','forward'):cur+=F(int(e.findtext('duration')),div)*(-1 if e.tag=='backup' else 1)
   elif e.tag=='note':
    t=e.get('id');assert t not in nodes;nodes[t]=e;on=last if e.find('chord') is not None else cur
    dur=F(int(e.findtext('duration','0')),div);tim[t]=[key,on,dur];order[t]=i
    if e.find('chord') is None:last=cur;cur+=dur
   else:other[key].append((cur,i,e))
  divs[key]=div
original_timing=deepcopy(tim)
def drop(t):
 if t in nodes:
  changed.add(tim[t][0]);del nodes[t];del tim[t]
def setevent(spec,anchor=None,on=None):
 t=spec['id']
 if spec.get('delete'):drop(t);return []
 old=nodes.get(t);new=old is None
 if old is None:
  n=E.Element('note',id=t);g=re.match(r'm(\d+)-s(\d+)-v(\d+)',t);assert g,t
  staff=int(g[2]);key=(f'P{staff}' if staff<3 else 'P3',str(int(g[1])));put(n,'staff',staff if staff<3 else staff-2)
  if staff==2:put(n,'staff',1)
  put(n,'voice',g[3]);tim[t]=[key,F(on or 0),F(0)];nodes[t]=n;order[t]=order.get(anchor,100)
 else:n=old;key=tim[t][0]
 changed.add(key)
 if 'onset_q' in spec:tim[t][1]=F(spec['onset_q'])
 elif new and on is not None:tim[t][1]=F(on)
 if 'duration_q' in spec or 'metrical_duration_q' in spec:tim[t][2]=F(spec.get('duration_q',spec.get('metrical_duration_q')))
 pp=spec.get('pitches',spec.get('pitch'));pp=pp if isinstance(pp,list) else [pp] if pp is not None else None
 if spec.get('rest'):pp=['R']
 if pp is not None:pitch(n,pp[0])
 if spec.get('measure_rest'):child(n,'rest').set('measure','yes')
 for k in ('voice','stem','accidental'):
  if k in spec:put(n,k,spec[k])
 typ=spec.get('written_type',spec.get('type'))
 if typ is not None:
  put(n,'type',typ);remove(n,'dot','time-modification')
 if 'dots' in spec:
  remove(n,'dot')
  for _ in range(spec['dots']):E.SubElement(n,'dot')
 if 'grace' in spec:
  remove(n,'grace');E.SubElement(n,'grace',**spec['grace']);remove(n,'duration');assert tim[t][2]==0
 elif tim[t][2]>0:remove(n,'grace')
 if 'tuplet' in spec:
  remove(n,'time-modification');v=spec['tuplet']
  if v:
   x=E.SubElement(n,'time-modification');put(x,'actual-notes',v['actual']);put(x,'normal-notes',v['normal'])
 if 'beam' in spec:
  remove(n,'beam')
  for l in range(1,spec.get('beam_levels',1)+1):E.SubElement(n,'beam',number=str(l)).text=spec['beam']
 out=[t]
 if pp is not None and len(pp)>1:
  for j,p in enumerate(pp[1:],2):
   ct=t+f'-p{j}';cn=nodes.get(ct)
   if cn is None:cn=deepcopy(n);cn.set('id',ct);nodes[ct]=cn
   pitch(cn,p);remove(cn,'chord');E.SubElement(cn,'chord');tim[ct]=list(tim[t]);order[ct]=order[t]+j/100;out.append(ct)
   for tag in ['duration','type','dot','grace','time-modification','voice','staff']:
    remove(cn,tag)
    for x in n.findall(tag):cn.append(deepcopy(x))
 if pp is not None:
  for j,nt in enumerate(out):
   if 'member_stems' in spec:put(nodes[nt],'stem',spec['member_stems'][j])
   if 'member_accidentals' in spec:put(nodes[nt],'accidental',spec['member_accidentals'][j])
 return out
def snap(ts):return {t:{'xml':E.tostring(nodes[t],encoding='unicode'),'onset_q':str(tim[t][1]),'duration_q':str(tim[t][2])} for t in ts if t in nodes}
allowed={'events','event','replace_events','delete_event','delete_events','kind/pitch','duration/type','duration/dots','onset/duration/type','duration/tuplet','duration/rest','insert_before','chord/pitch','add_chord_member'}
# Compound replacement notation is retained for an explicit later application, never silently dropped.
compound=[]
for pend in b1['pending']:
 idx=pend['index'];c=cs[idx];a=c['after'];attr=c['attribute'];ts=c['targets']
 if attr not in allowed and not(attr=='onset_q' and all(t in nodes for t in ts)):deferred.append(pend);continue
 before=snap(ts);touched=set(ts)
 if attr in ('delete_event','delete_events') or attr in ('event','events') and (a is None or isinstance(a,str)):
  assert a is None or a.startswith('delete;'),c
  for t in ts:drop(t)
 elif attr in ('events','replace_events'):
  full=attr=='replace_events' or '-REPLACE' in c['id']
  if isinstance(a,dict):
   groups=[(k[5:],v) for k,v in a.items() if k.startswith('voice') and isinstance(v,list)]
   if 'events' in a:groups=[(None,a['events'])]
   compound.append({'index':idx,'id':c['id'],'payload':{k:v for k,v in a.items() if k!='events' and not k.startswith('voice')},'new_event_ids':[x['id'] for _,vs in groups for x in vs]})
  else:groups=[(None,a)]
  if full:
   for t in ts:
    for ct in list(nodes):
     if ct==t or ct.startswith(t+'-p'):drop(ct)
  for voice,specs in groups:
   cur=F(0)
   for spec0 in specs:
    spec=deepcopy(spec0)
    if voice is not None:spec.setdefault('voice',voice)
    out=setevent(spec,on=cur if full else None);touched.update(out)
    if out:cur=tim[out[0]][1]+tim[out[0]][2]
 elif attr=='kind/pitch':
  for t in ts:setevent(dict(a,id=t));touched.add(t)
 elif attr=='insert_before':
  anchor=ts[0];assert anchor in nodes
  for sp in a if isinstance(a,list) else [a]:touched.update(setevent(sp,anchor=anchor,on=tim[anchor][1]))
 elif attr=='chord/pitch':
  drop(a['delete_chord_member']);setevent({'id':ts[0],'pitch':a['pitches'][0],'accidental':a['accidental']})
 elif attr=='add_chord_member':
  base=nodes[ts[0]];t=a['id'];nodes[t]=deepcopy(base);nodes[t].set('id',t);E.SubElement(nodes[t],'chord');tim[t]=list(tim[ts[0]]);order[t]=order[ts[0]]+.03;setevent(a);touched.add(t)
 elif attr=='onset_q':
  for t in ts:tim[t][1]=F(a);changed.add(tim[t][0])
 elif attr=='duration/tuplet':
  for j,t in enumerate(ts):setevent({'id':t,'duration_q':a['duration_q'][j],'type':a['written_types'][j],'tuplet':a['tuplet']})
 else:
  for t in ts:
   sp={k:v for k,v in a.items() if k!='insert_after'};setevent(dict(sp,id=t))
   if 'insert_after' in a:touched.update(setevent(a['insert_after'],anchor=t))
 records.append({'index':idx,'id':c['id'],'attribute':attr,'before':before,'after':snap(touched),'source_inspection':c['inspection_record'],'source_evidence':c['source_evidence'],'print_reason':c['print_reason'],'interpretation_status':c['status'],'status':'CORE_APPLIED_COMPOUND_MARKS_PENDING' if any(x['index']==idx for x in compound) else 'APPLIED_TO_PARTIAL_WORKING_XML'})
# Encode all rational times at divisions 96 (source has 24). Preserve every event onset.
DIV=96
for key,m in measure.items():
 entries=[]
 for on,i,e in other[key]:
  if e.tag=='attributes':
   dv=e.find('divisions')
   if dv is not None:dv.text=str(DIV)
  for off in e.findall('offset'):off.text=str(int(F(off.text)*DIV/divs[key]))
  entries.append((on,0,i,e,None))
 for t,n in nodes.items():
  if tim[t][0]!=key:continue
  on,dur=tim[t][1:]
  if n.find('grace') is None:
   assert (dur*DIV).denominator==1,(t,dur);put(n,'duration',int(dur*DIV))
  base=t.split('-p')[0];baseorder=order.get(base,order[t]);member=int(t.rsplit('-p',1)[1]) if '-p' in t else 0
  # Original order retains chord adjacency, grace before main event at same onset.
  entries.append((on,1 if n.find('grace') is not None else 2,(baseorder,member),n,t))
 for e in list(m):m.remove(e)
 cur=F(0);last=None
 for on,_,__,e,t in sorted(entries,key=lambda x:(x[0],x[1],x[2])):
  isch=t is not None and e.find('chord') is not None
  if not isch and on!=cur:
   q=on-cur;shift=E.SubElement(m,'forward' if q>0 else 'backup');assert (abs(q)*DIV).denominator==1;put(shift,'duration',int(abs(q)*DIV));cur=on
  if isch:assert last is not None and tim[last][1]==on,(t,last)
  m.append(e)
  if t is not None:
   if not isch:cur=on+tim[t][2];last=t
 # Every part starts with divisions already; normalization doesn't change sounding times.
seq=['grace','cue','chord','pitch','unpitched','rest','duration','tie','instrument','footnote','level','voice','type','dot','accidental','time-modification','stem','notehead','notehead-text','staff','beam','notations','lyric','play','listen']
for n in nodes.values():
 kids=list(n)
 for x in kids:n.remove(x)
 for x in sorted(kids,key=lambda x:seq.index(x.tag) if x.tag in seq else 999):n.append(x)
f=D/'UNVERIFIED_core_partial.musicxml';tree.write(str(f),encoding='utf-8',xml_declaration=True,pretty_print=True)
# Independently reparse resulting onset/duration for every note, including untouched notes.
actual={}
for p in E.parse(str(f)).findall('part'):
 div=1
 for m in p.findall('measure'):
  cur=F(0);last=F(0)
  for e in m:
   if e.tag=='attributes' and e.find('divisions') is not None:div=int(e.findtext('divisions'))
   elif e.tag in ('backup','forward'):cur+=F(int(e.findtext('duration')),div)*(-1 if e.tag=='backup' else 1)
   elif e.tag=='note':
    dur=F(int(e.findtext('duration','0')),div);on=last if e.find('chord') is not None else cur;actual[e.get('id')]=[(p.get('id'),m.get('number')),on,dur]
    if e.find('chord') is None:last=cur;cur+=dur
assert actual==tim,[(t,actual.get(t),v) for t,v in tim.items() if actual.get(t)!=v][:10]
for x in compound:deferred.append({'index':x['index'],'id':x['id'],'attribute':'replacement_embedded_marks','reason':'Core applied; embedded beams/slurs/ties/text still pending','payload':x})
save(D/'correction_batch_02.json',{'schema':'astra_correction_batch.v1','complete':True,'primary_complete':False,'source_xml_sha256':h(src),'working_xml':f.name,'working_xml_sha256':h(f),'audit_sha256':h(R/'reviewer/phase3_review.json'),'applied':records,'pending':deferred})
save(D/'correction_batch_02_checks.json',{'schema':'astra_correction_batch_checks.v1','scope':'Correction application only; not Phase5 validation','working_xml_sha256':h(f),'applied_core_operations':len(records),'pending_operations':len(deferred),'exact_fraction_timeline_reparse_match':True,'final_note_count':len(nodes),'divisions':DIV,'compound_marks_pending':compound,'timeline':{t:{'part':v[0][0],'measure':v[0][1],'onset_q':str(v[1]),'duration_q':str(v[2])} for t,v in tim.items()}})
print(len(records),'core operations applied;',len(deferred),'pending')
