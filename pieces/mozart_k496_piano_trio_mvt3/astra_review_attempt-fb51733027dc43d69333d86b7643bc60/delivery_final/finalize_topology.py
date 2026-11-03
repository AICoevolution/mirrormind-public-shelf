from pathlib import Path
from lxml import etree as E
from fractions import Fraction as F
from collections import Counter,defaultdict
from copy import deepcopy
import json,hashlib
R=Path(__file__).resolve().parent.parent;D=R/'delivery_final';h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
src=D/'UNVERIFIED_notation_partial.musicxml';tree=E.parse(str(src));ns={n.get('id'):n for n in tree.findall('.//note')};changes=[]
def edit(t,tag,value,why):
 n=ns[t];e=n.find(tag);before=E.tostring(n,encoding='unicode')
 if e is None:e=E.SubElement(n,tag)
 if e.text==str(value):return
 e.text=str(value);changes.append({'id':t,'attribute':tag,'before_xml':before,'after_xml':E.tostring(n,encoding='unicode'),'reason':why})
def census():return {p.get('id'):dict(Counter('staff'+n.findtext('staff','1')+'/voice'+n.findtext('voice','1') for n in p.findall('.//note'))) for p in tree.findall('part')}
pre=census();er=json.load(open(D/'ERRATUM_001.json'))
for c in er['changes']:
 for t in c['ids']:edit(t,'voice',c['voice_after'],'ERRATUM-001: '+c['reason'])
# Chord members are the same sounding event and must share their base voice.
for t,n in ns.items():
 if n.find('chord') is not None:
  base=t.split('-p')[0];assert base in ns
  edit(t,'voice',ns[base].findtext('voice'),'Propagate frozen parent event voice to every chord member; retain exact member ties/stems.')
# Preserve cross-staff voice1 only in P061, independently documented in system13.
for t,n in ns.items():
 part=n.getparent().getparent().get('id');bar=int(n.getparent().get('number'));v=n.findtext('voice');st=n.findtext('staff')
 if part in ['P1','P2']:edit(t,'voice','1','Single printed string line; remove OMR restart label, including inserted rest.')
 elif st=='2' and v=='1' and bar!=61:edit(t,'voice','5','Continuous lower piano line; preserve upper voice1 as independent simultaneous line.')
 elif st=='1' and v=='5':edit(t,'voice','1','Continuous upper piano melody; OMR restart label at closing passage.')
# Source-supported CORE-P070-S4-VOICES names exactly G3/B3: eliminate obsolete third head.
t='m070-s4-v1-e01-p3';n=ns.pop(t);changes.append({'id':t,'attribute':'delete_chord_member','before_xml':E.tostring(n,encoding='unicode'),'after_xml':None,'reason':'Complete CORE-P070-S4-VOICES pitches=[G3,B3]; old third member was not removed by the partial event updater.'});n.getparent().remove(n)
# P044 consecutive eighth + two sixteenths, no tuplet. Insert exact cursor correction before latter two notes.
for t,on in [('m044-s1-v13-e11',F(7,2)),('m044-s1-v13-e12',F(15,4))]:
 n=ns[t];m=n.getparent();cur=F(0)
 for e in m:
  if e is n:break
  if e.tag=='note' and e.find('chord') is None:cur+=F(int(e.findtext('duration','0')),96)
  elif e.tag in ('backup','forward'):cur+=F(int(e.findtext('duration')),96)*(-1 if e.tag=='backup' else 1)
 delta=on-cur
 if delta:
  sh=E.Element('forward' if delta>0 else 'backup');E.SubElement(sh,'duration').text=str(int(abs(delta)*96));m.insert(m.index(n),sh)
 changes.append({'id':t,'attribute':'onset_q','before':str(cur),'after':str(on),'reason':'CORE-P044-S1-FINAL-GROUP consecutive printed eighth/sixteenth/sixteenth; no triplet spacing.'})
# Correct written type when a duration-only proposal requires a half note.
for t in ['m049-s3-v2-e04']:edit(t,'type','half','CORE-P049-S3-LOWER explicitly sets D4 duration2; half-note glyph retained from print.')
# Frozen VOICE-P071-S4 includes merging simultaneous B2/G3 into one chord.
n=ns['m071-s4-v2-e02'];m=n.getparent();prev=n.getprevious();assert prev.tag=='backup' and prev.findtext('duration')=='96'
before=E.tostring(n,encoding='unicode');m.remove(prev);n.insert(0,E.Element('chord'))
changes.append({'id':n.get('id'),'attribute':'chord','before_xml':before,'after_xml':E.tostring(n,encoding='unicode'),'reason':'VOICE-P071-S4 explicitly requires shared chord at onset0; retain both member slur endpoints.'})
# Reparse onset ledger, detect inconsistent chord attachment and timeline overlaps for follow-up.
def timeline():
 out={}
 for part in tree.findall('part'):
  div=1
  for m in part.findall('measure'):
   cur=F(0);last=None
   for e in m:
    if e.tag=='attributes' and e.find('divisions') is not None:div=int(e.findtext('divisions'))
    elif e.tag in ('backup','forward'):cur+=F(int(e.findtext('duration')),div)*(-1 if e.tag=='backup' else 1)
    elif e.tag=='note':
     dur=F(int(e.findtext('duration','0')),div);on=out[last]['onset'] if e.find('chord') is not None else cur
     out[e.get('id')]={'part':part.get('id'),'measure':int(m.get('number')),'onset':on,'duration':dur,'voice':e.findtext('voice'),'staff':e.findtext('staff'),'chord':e.find('chord') is not None}
     if e.find('chord') is None:cur+=dur;last=e.get('id')
 return out
tl=timeline();lanes=defaultdict(list)
for t,v in tl.items():
 if not v['chord'] and v['duration']:lanes[(v['part'],v['measure'],v['voice'])].append((v['onset'],v['onset']+v['duration'],t))
overlap=[]
for lane,es in lanes.items():
 es.sort()
 for prev,cur in zip(es,es[1:]):
  if cur[0]<prev[1]:overlap.append({'lane':lane,'first':prev[2],'second':cur[2],'first_end':str(prev[1]),'second_start':str(cur[0])})
f=D/'UNVERIFIED_topology_partial.musicxml';tree.write(str(f),encoding='utf-8',xml_declaration=True,pretty_print=True)
save(D/'correction_batch_04.json',{'schema':'astra_correction_batch.v1','scope':'Topology reconciliation and application fidelity fixes','complete':True,'primary_complete':False,'source_xml_sha256':h(src),'working_xml':f.name,'working_xml_sha256':h(f),'erratum_sha256':h(D/'ERRATUM_001.json'),'changes':changes})
save(D/'topology_application_checks.json',{'schema':'astra_topology_application.v1','working_xml_sha256':h(f),'pre_census':pre,'post_census':census(),'overlaps_requiring_resolution':overlap,'timeline':{t:{**v,'onset':str(v['onset']),'duration':str(v['duration'])} for t,v in tl.items()},'scope':'Correction consistency; not Phase5 validation'})
print('changes',len(changes),'overlaps',json.dumps(overlap));print(census())
