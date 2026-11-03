"""First correction batch: stable, note-local targets outside pending event rebuilds.
This is a partial working XML, not the final primary or a readiness claim.
"""
from pathlib import Path
from lxml import etree as E
import json,hashlib,re,os
from collections import Counter
R=Path(__file__).resolve().parent.parent;D=R/'delivery_final'
h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,indent=2)+'\n')
review=json.load(open(R/'reviewer/phase3_review.json'));cs=review['correction_targets']
source=Path('/inputs/source_agent/UNVERIFIED_source.musicxml');assert h(source)==review['candidate_sha256']
xml=E.parse(str(source));nodes={n.get('id'):n for n in xml.findall('.//note')}
structural={'events','event','replace_events','delete_event','delete_events','chord/pitch','add_chord_member','kind/pitch'}
rebuild_targets={t for c in cs if c['attribute'] in structural for t in c['targets']}
# Exclude every note in a rebuilt staff/bar, including newly addressed chord members.
rebuild_regions={tuple(re.match(r'm(\d+)-s(\d+)-',t).groups()) for t in rebuild_targets if re.match(r'm(\d+)-s(\d+)-',t)}
allowed={'pitch','pitch/accidental','accidental','voice','notations/ornaments','notations/articulations','notations/fermata'}
records=[];pending=[]
def put(n,tag,val):
 old=n.find(tag)
 if val is None:
  if old is not None:n.remove(old)
 else:
  if old is None:old=E.SubElement(n,tag)
  old.text=str(val)
def setpitch(n,p):
 m=re.fullmatch(r'([A-G])([#b]*)(-?\d+)',p);assert m,p
 x=n.find('pitch');assert x is not None,n.get('id')
 put(x,'step',m[1]);alter=m[2].count('#')-m[2].count('b');put(x,'alter',str(alter) if alter else None);put(x,'octave',m[3])
def child(n,t):
 x=n.find(t)
 if x is None:x=E.SubElement(n,t)
 return x
for index,c in enumerate(cs):
 attr=c['attribute'];targets=c['targets'];a=c['after']
 eligible=attr in allowed and all(t in nodes and tuple(re.match(r'm(\d+)-s(\d+)-',t).groups()) not in rebuild_regions for t in targets)
 if not eligible:pending.append({'index':index,'id':c['id'],'attribute':attr,'reason':'Requires timing/event rebuild or dependent endpoint/beam application' if attr not in allowed else 'Target region has pending event rebuild; apply afterward'});continue
 before={t:E.tostring(nodes[t],encoding='unicode') for t in targets}
 for i,t in enumerate(targets):
  n=nodes[t];v=a[i] if isinstance(a,list) else a
  if attr=='accidental' and isinstance(v,dict):v=v[t.split('-')[-1]]
  if attr=='pitch':setpitch(n,v)
  elif attr=='pitch/accidental':setpitch(n,v['pitch']);put(n,'accidental',v.get('accidental'))
  elif attr=='accidental':put(n,'accidental',v)
  elif attr=='voice':put(n,'voice',v)
  elif attr=='notations/fermata':
   no=child(n,'notations');f=E.SubElement(no,'fermata',type=v.get('type','upright'));f.text=v.get('shape','normal')
  elif attr=='notations/articulations':
   ar=child(child(n,'notations'),'articulations');typ=v if isinstance(v,str) else v['type'];el=E.SubElement(ar,typ)
   if isinstance(v,dict):
    for k in ['placement','orientation']:
     if k in v:el.set(k,v[k])
  elif attr=='notations/ornaments':
   ar=child(child(n,'notations'),'ornaments');el=E.SubElement(ar,v['type'])
   if 'placement' in v:el.set('placement',v['placement'])
   if v.get('accidental-mark'):
    ac=v['accidental-mark'];el=E.SubElement(ar,'accidental-mark',placement=ac.get('placement','below'));el.text=ac['value']
 after={t:E.tostring(nodes[t],encoding='unicode') for t in targets}
 records.append({'index':index,'id':c['id'],'attribute':attr,'targets':targets,'before_xml':before,'after_xml':after,'source_inspection':c['inspection_record'],'source_evidence':c['source_evidence'],'print_reason':c['print_reason'],'status':'APPLIED_TO_PARTIAL_WORKING_XML','interpretation_status':c['status']})
# Correct element order without changing payload; required MusicXML note sequence.
order=['grace','cue','chord','pitch','unpitched','rest','duration','tie','instrument','footnote','level','voice','type','dot','accidental','time-modification','stem','notehead','notehead-text','staff','beam','notations','lyric','play','listen']
for n in nodes.values():
 kids=list(n)
 for e in kids:n.remove(e)
 for _,e in sorted(enumerate(kids),key=lambda it:(order.index(it[1].tag) if it[1].tag in order else len(order),it[0])):n.append(e)
for p in xml.findall('.//pitch'):
 kids=list(p)
 for e in kids:p.remove(e)
 for e in sorted(kids,key=lambda e:['step','alter','octave'].index(e.tag)):p.append(e)
f=D/'UNVERIFIED_working_partial.musicxml';xml.write(str(f),encoding='utf-8',xml_declaration=True,pretty_print=True)
# Reparse and compare musical fields for every applied simple operation.
out=E.parse(str(f));outnodes={n.get('id'):n for n in out.findall('.//note')};assert set(outnodes)==set(nodes)
checks=[]
for rec in records:
 c=cs[rec['index']];a=c['after'];attr=c['attribute']
 for i,t in enumerate(c['targets']):
  n=outnodes[t];v=a[i] if isinstance(a,list) else a;ok=True
  if attr=='accidental' and isinstance(v,dict):v=v[t.split('-')[-1]]
  if attr in ['pitch','pitch/accidental']:
   p=v if attr=='pitch' else v['pitch'];m=re.fullmatch(r'([A-G])([#b]*)(-?\d+)',p);ok=n.findtext('pitch/step')==m[1] and int(n.findtext('pitch/alter','0'))==m[2].count('#')-m[2].count('b') and n.findtext('pitch/octave')==m[3]
  if attr in ['accidental','pitch/accidental']:ok=ok and n.findtext('accidental')==(v if attr=='accidental' else v.get('accidental'))
  if attr=='voice':ok=n.findtext('voice')==str(v)
  assert ok,(rec['id'],t);checks.append({'change_id':rec['id'],'target':t,'passed':ok})
# Prove identity and timing preservation for untouched musical dimensions.
base=E.parse(str(source));bn={n.get('id'):n for n in base.findall('.//note')}
for t,n in outnodes.items():
 for tag in ['duration','type','dot','chord','grace','staff','time-modification','tie']:
  assert [E.tostring(e) for e in n.findall(tag)]==[E.tostring(e) for e in bn[t].findall(tag)],(t,tag)
write(D/'correction_batch_01.json',{'schema':'astra_correction_batch.v1','complete':True,'primary_complete':False,'source_xml_sha256':h(source),'working_xml':f.name,'working_xml_sha256':h(f),'audit_sha256':h(R/'reviewer/phase3_review.json'),'applied':records,'pending':pending})
write(D/'correction_batch_01_checks.json',{'schema':'astra_correction_batch_checks.v1','scope':'Batch application only; not Phase5 validation','working_xml_sha256':h(f),'applied_changes':len(records),'pending_changes':len(pending),'checks':checks,'note_ids_unchanged':True,'timing_and_chord_membership_unchanged':True,'source_candidate_unchanged':h(source)==review['candidate_sha256']})
write(D/'correction_inventory.json',{'schema':'astra_correction_inventory.v1','frozen_targets':len(cs),'attribute_counts':dict(Counter(c['attribute'] for c in cs)),'applied_batch01':len(records),'pending':len(pending),'working_xml':f.name,'working_xml_sha256':h(f),'primary_ready':False})
p=json.load(open('/output/worker-progress.json'));p['units'].append({'id':'corrections:batch-01','status':'COMPLETE','evidence':{str(n.relative_to(R)):h(n) for n in [D/'correction_batch_01.json',D/'correction_batch_01_checks.json',f]}});p['units'].append({'id':'corrections:primary','status':'PARTIAL','evidence':{'delivery_final/correction_inventory.json':h(D/'correction_inventory.json')}});p['next_action']='Continue pending correction IDs from delivery_final/correction_batch_01.json; rebuild exact event timelines, then apply dependent spans/beams/directions and finalize minimal voice topology';write('/output/worker-progress.json.tmp',p);os.replace('/output/worker-progress.json.tmp','/output/worker-progress.json');print(len(records),'applied;',len(pending),'pending')
