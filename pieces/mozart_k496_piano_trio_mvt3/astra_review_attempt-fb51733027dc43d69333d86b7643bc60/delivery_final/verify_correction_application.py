from pathlib import Path
from lxml import etree as E
from fractions import Fraction as F
import json,hashlib,re
R=Path(__file__).resolve().parent.parent;D=R/'delivery_final';h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();cs=json.load(open(R/'reviewer/phase3_review.json'))['correction_targets'];f=D/'UNVERIFIED_topology_partial.musicxml';x=E.parse(str(f));ns={n.get('id'):n for n in x.findall('.//note')};tl=json.load(open(D/'topology_application_checks.json'))['timeline'];checks=[]
def check(cid,t,attr,want,got):checks.append({'change':cid,'target':t,'attribute':attr,'expected':want,'actual':got,'passed':want==got})
def pv(n):
 if n.find('rest') is not None:return 'R'
 a=int(n.findtext('pitch/alter','0'));return n.findtext('pitch/step')+('#'*a if a>0 else 'b'*(-a))+n.findtext('pitch/octave')
def spec(cid,s):
 t=s['id'];n=ns.get(t)
 if s.get('delete'):check(cid,t,'deleted',False,t in ns);return
 check(cid,t,'exists',True,t in ns)
 if n is None:return
 ps=s.get('pitches',s.get('pitch'));ps=ps if isinstance(ps,list) else [ps] if ps is not None else None
 if s.get('rest'):ps=['R']
 if ps:
  for j,p in enumerate(ps):
   nt=t if j==0 else t+f'-p{j+1}';check(cid,nt,'pitch',p,pv(ns[nt]) if nt in ns else None)
 for key,tag in [('type','type'),('written_type','type'),('accidental','accidental'),('stem','stem')]:
  if key in s:check(cid,t,key,s[key],n.findtext(tag))
 for key,tag in [('onset_q','onset'),('duration_q','duration'),('metrical_duration_q','duration')]:
  if key in s:check(cid,t,key,str(F(s[key])),tl[t][tag])
 if 'dots' in s:check(cid,t,'dots',s['dots'],len(n.findall('dot')))
 if 'grace' in s:check(cid,t,'grace',s['grace'],dict(n.find('grace').attrib) if n.find('grace') is not None else None)
for c in cs:
 a=c['after'];at=c['attribute'];ts=c['targets'];cid=c['id']
 if at in ['events','replace_events'] and a:
  specs=a if isinstance(a,list) else a.get('events',sum([v for k,v in a.items() if k.startswith('voice') and isinstance(v,list)],[]))
  for s in specs:spec(cid,s)
 elif at in ['pitch','pitch/accidental','accidental']:
  for j,t in enumerate(ts):
   v=a[j] if isinstance(a,list) else a
   if at=='pitch':check(cid,t,'pitch',v,pv(ns[t]))
   elif at=='pitch/accidental':spec(cid,dict(v,id=t))
   else:
    if isinstance(v,dict):v=v[t.split('-')[-1]]
    check(cid,t,'accidental',v,ns[t].findtext('accidental'))
 elif at in ['insert_before']:
  for s in a if isinstance(a,list) else [a]:spec(cid,s)
 elif at in ['kind/pitch','duration/type','duration/dots','onset/duration/type','duration/rest']:
  for t in ts:spec(cid,dict(a,id=t))
 elif at=='notations/slur':
  for typ,t in [('start',a['start']),('stop',a['stop'])]:
   els=ns[t].findall('notations/slur');ok=any(e.get('type')==typ and all(e.get(k)==a[k] for k in ['placement','orientation'] if k in a) for e in els);check(cid,t,'slur_'+typ,True,ok)
 elif at in ['beam/stem','beam[2]','beam[2,3]']:
  if at=='beam/stem' and 'groups' in a:continue
  levels={}
  if at=='beam/stem':
   levels={int(k[5:]):v for k,v in a.items() if k.startswith('level') and k!='levels'}
   if 'levels' in a:
    for l in range(1,a['levels']+1):levels[l]=a['values']
  elif at=='beam[2]':levels={2:a['values'] if isinstance(a,dict) else [a]*len(ts)}
  else:levels={l:a['values'] for l in a['levels']}
  for l,vs in levels.items():
   for j,t in enumerate(ts):
    v=vs.get(t) if isinstance(vs,dict) else vs[j];e=ns[t].find(f"beam[@number='{l}']");got=e.text if e is not None else None
    # A later explicit secondary hook overrides an earlier beam group null.
    later=[z for z in cs[cs.index(c)+1:] if z['attribute']==f'beam[{l}]' and t in z['targets']]
    if later:continue
    check(cid,t,'beam'+str(l),v,got)
failed=[c for c in checks if not c['passed']];out={'schema':'astra_correction_application_verification.v1','scope':'Frozen payload application verification only; not Phase5 validation','working_xml_sha256':h(f),'checks':checks,'checks_count':len(checks),'failures':failed,'passed':not failed};(D/'correction_application_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(len(checks),'checks;',len(failed),'failures');print(json.dumps(failed,indent=2)[:5000])
