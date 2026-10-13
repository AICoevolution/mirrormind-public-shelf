# Phase 1 print-only freeze — repaired run, revision 02

2026-09-22. Only launch-gate files and current Phase 1 allowlisted files accessed. Matching authorization hash: fa0ec8e4a9983e2d61a5ec64f2c9f800c912fe7ba56e80a874c4f07c1fa8b7ed. Matching handoff: 0ae46e8bad574521faeda627af8f8d7ca0272b22bbe01636aeb3eb0793f01b71. All seven allowed evidence hashes pass. This checkpoint precedes all reader access. Previous blocked checkpoint remains immutable; ERRATUM_001 corrects its P029 reading.

## Physical frame and capacities

One printed page, page label 43, plate 41459, title 27. Little Song in Canon-form. Five two-staff systems: P001–009, P010–019, P020–029, P030–039, P040–048 (9+10+10+10+9 = 48). Count includes physical pickup/partial regions. Source page is 1760 by 2295 pixels. System page-y ranges: [0,608), [608,1006), [1006,1402), [1402,1798), [1798,2295). The reviewer-generated print_system_N.png files preserve those full-width regions. No prepared system crops were accessed.

Printed meter 2/4, no changes. Upper clef G2, lower F4, no changes; system-start repetitions are not changes. Opening key signature has zero accidentals. P018 introduces F#, C#, G# on both staves. The S3 opening repeats this signature. Three cancellation naturals after the P029 light-light double bar restore zero sharps for P030. No other signature change.

Capacities in quarter units: P001=1/2; P029=3/2; P030=1/2; P048=3/2; every other physical region=2. P001 upper sounding eighth versus lower eighth rest. P030 sounding eighth on both staves, lower chord. P029 three moving eighths against dotted-quarter lines. P048 sounding eighth chords/octaves followed by two eighth rests on both staves. These capacities agree with the repaired primary lock and physical_bars entries. Meter declarations remain separate. Total written duration 92 quarter units. No rhythmic padding is justified by this frame.

The derived reviewer_phase1_frame_lock.json mistakenly includes the P029 partial-bar description in printed_key_changes and omits it from pickup_or_partial_bars. Its physical_bars P029 capacity and primary physical_score_lock are correct. This is a metadata classification defect, not an additional printed key change or an ambiguous physical boundary. Use the two actual signature changes P018 and P030 and the explicit capacity table; report the derived metadata defect during audit. No reader correspondence has yet been asserted.

## MARKS inventory: point marks and wedges

Addresses are physical bars; q is onset in quarter units within the region. Fingerings, including curved finger-substitution marks over adjacent numerals, are excluded. All observations below come from page pixels, not from prepared musical claims.

| ID | Page/system/region | Printed finding |
|---|---|---|
| M01 | 1/1/P001 | Andante molto espressivo; quarter=60; p |
| M02 | 1/1/P002 | crescendo wedge under upper staff, approx page x400–507 |
| M03 | 1/1/P003 q0 | upper accent > |
| M04 | 1/1/P004 q0 | inner/lower upper-staff accent > |
| M05 | 1/1/P006 q0 | upper accent >; crescendo wedge x1030–1121 |
| M06 | 1/1/P007 q0 | inner upper-staff accent > |
| M07 | 1/1/P008 q0 | upper accent >; diminuendo wedge x1325–1435 |
| M08 | 1/1/P009 q0 | arpeggiation at upper chord; accent under chord |
| M09 | 1/2/P011 q0 | upper accent > |
| M10 | 1/2/P012 q0 | inner upper-staff accent > |
| M11 | 1/2/P014 q0 | upper accent > |
| M12 | 1/2/P015 q0 | inner upper-staff accent > |
| M13 | 1/2/P016 q0 | upper accent > |
| M14 | 1/2/P017 q0 | arpeggiation at upper chord |
| M15 | 1/2/P018 q0 | mf between staves |
| M16 | 1/3/P020 | cresc. between staves; textual extent approximately late bar, not a wedge |
| M17 | 1/3/P023 | dim. between staves, toward end of bar |
| M18 | 1/3/P026 | crescendo wedge x1122–1206 |
| M19 | 1/3/P027 | diminuendo wedge x1245–1322 |
| M20 | 1/3/P028–029 | crescendo wedge x1416–1566, crosses barline |
| M21 | 1/4/P030 q0 | p |
| M22 | 1/4/P032 q0 | upper accent > |
| M23 | 1/4/P033 q0 | inner upper-staff accent > |
| M24 | 1/4/P035 q0 | upper accent > |
| M25 | 1/4/P036 q0 | inner upper-staff accent > |
| M26 | 1/4/P037 q0 | upper accent > |
| M27 | 1/4/P039 | crescendo wedge x1528–1625 |
| M28 | 1/5/P040 q0 | sf |
| M29 | 1/5/P041 | diminuendo wedge x447–529 |
| M30 | 1/5/P043 | crescendo wedge x736–837 |
| M31 | 1/5/P045 | diminuendo wedge x1080–1169 |
| M32 | 1/5/P046 | ritard. beneath upper staff; continues musically toward close, no drawn endpoint |
| M33 | 1/5/P047 | pp, carries into P048 |

No pedal or release sign, fermata, trill, turn, mordent, octave line, breath sign, repeat-derived tempo text, or other navigation text seen. No explicit detached staccato series seen. Isolated specks are not promoted to articulations without glyph/context confirmation. Duration dots belong to CORE. Exact attachments of text and wedges will be audited against candidate onset positions, retaining the visible x extent above.

## Curve inventory and ambiguity register

The following records locate visible musical curves by system, staff and physical region. A phrase arc is a slur, not an automatic tie. Curves returning to the same pitch are provisional ties until both printed noteheads are matched. Inter-staff arcs can follow cross-staff voices; their vertical position alone does not identify a voice. Endpoint coordinates use the full-width system crop, with approximate x to distinguish overlapping curves. Pixel extents are the primary Phase 1 inventory for ambiguous attachment.

| Group | Visible curve locations (left x to right x) and print addresses |
|---|---|
| S1 upper phrasing | x350–550 P001→P003 first note; x665–940 P003 last→P005 third eighth; x968–1250 P005 last→P007 third eighth; x1278–1564 P007 last→P009 third eighth; x1607→right edge P009 last, continues S2 to P011 first. |
| S1 between-staff phrasing | x500–717 P002 last lower staff→P004 first upper inner line; x807–1100 P004 last upper inner line→P006 lower moving line; x1130–1435 P006 last lower moving line→P008 lower moving line; x1435→right edge P008 last lower moving line→S2 P010 lower moving line. Exact endpoints of the two long cross-staff curves are ambiguous where stems and curves meet; preserve both and resolve with enlarged pixel/event matching. |
| S1 lower phrasing | x500–810 below lower staff P002 last→P004 last; x810–1030 below lower staff P004 last→P006 first. |
| S1 short ties | upper P006 last→P007 first (x1127–1175); lower sustained P006→P007 (x1038–1188); lower moving P007 last→P008 first (x1285–1328); lower sustained P008→P009 (x1328–1500). |
| S2 upper phrasing | continuation from S1: x200–385 P010→P011 first; x474–704 P011 last→P013 third eighth; x724–967 P013 last→P015 third eighth; x984–1024 P015 last→P016 first; x1090–1228 P016 last→P017 moving notes; x1478–1608 P018 last→P019 later note (attachment near upper last note requires enlargement). |
| S2 between/lower phrasing | x200–302 P010 first→third lower moving notes (incoming S1 span); x334–509 P010 last lower→P012 upper inner first; x580–823 P012 upper inner last→P014 lower moving notes; x854–1070 P014 last→P016 lower third; x1102–1150 P016 last→P017 lower first; x1270–1436 P017 lower last→P018 lower third; x1618→right edge P019 lower last outgoing to S3/P020. Lower arcs x464–508 P011 last→P012 first and x580–775 P012 last→P014 first. |
| S2 short ties | upper P014 last→P015 first; lower sustained P015→P016→P017 (two arcs); lower moving P015 last→P016 first. |
| S3 upper phrasing | P020 last→P021 interior (x398–509); P021 high note→P022 later note (x530–636); P022 last→P023 later note (x665–765); P023 last→P024 later note (x795–890); P024 last→P025 later note (x916–1036); P025 last→P028 first (x1065–1365); P028 interior→P029 final (x1400–1565). Exact endpoints at the closely spaced sixteenths in P021/P022 are retained as ambiguity, not guessed from meter. |
| S3 lower phrasing | Incoming P019→P020 lower first phrase through late P020 (x247–404); P021 lower first→last (x424–550); P022 lower first→late P023 (x577–758); P023 last→P024 lower third (x797–890); P024 last→P027 lower third (x917–1324); P028 upper inner/lower context long descending arc→P029 lower last (x1414–1565). Bottom slur x1098–1280 P026→P027, endpoint assignment ambiguous between moving inner/lower voices. |
| S3 short ties | upper inner within P021 sixteenth context; upper inner P021→P022→P023→P024; lower sustained P021→P022→P023→P024; upper melody P026 late→P027 first; upper inner P027→P028 and P028→P029; lower moving P025→P026, P026→P027, P027→P028, P028→P029. These closely adjacent ties must be matched to pitches individually in CORE; phrase arches do not substitute for ties. |
| S4 upper phrasing | P030→P032 first (x247–449); P032 last→P034 third (x557–832); P034 last→P036 third (x864–1150); P036 last→P038 third (x1187–1437); P039 first→outgoing system edge, continuing S5/P040–P042 first. |
| S4 between/lower phrasing | lower P031 last→P033 upper inner first; P033 upper inner last→P035 lower moving line; lower P035 last→P037 third; lower P037 last→P039 third. Below-staff P031 last→P033 first; P033 last→P035 first. Short lower P030→P031 tie. |
| S4 short ties | upper P035 last→P036 first; lower sustained P035→P036, P037→P038; lower moving P036 last→P037 first and P038 last→P039 first. |
| S5 upper phrasing | incoming from S4 P039, continuing x204–574 P040→P042 first; x673–1080 P042 last→P045 first; x1102–1228 P045 interior→P046 first. |
| S5 between/lower phrasing | x216–727 P040 lower first→P043 lower first; x515–882 below lower staff P041 lower last→P044 first; x882–993 P044 first→last lower moving line; x1034–1211 P045 lower/upper crossing line→P046 upper inner first; x1252–1390 P046 upper inner second→P047 upper inner first. |
| S5 short ties | lower P040 last→P041 first; lower P044 last→P045 first. Some overlapping P044/P045 curves may belong to slur rather than tie where pitches differ: this classification is explicitly unresolved pending exact paired-note audit. |

Print ambiguities requiring scrutiny, all page 1: S1/P002–006 cross-staff slur endpoints; S1/P009–S2/P011 incoming/outgoing phrase; S2/P018–S3/P020 phrase endpoints and sixteenth beams; S3/P021–024 short ties near simultaneous voices; S3/P026–029 overlapping curves and hairpin; S4/P039–S5/P042 long slur; S5/P044–047 nested/cross-staff curves; textual onset of cresc./dim./ritard. Approximate curve endpoints above are uncertainty records, not authority to rewrite the print.

## ROUTE inventory

No repeat boundaries, volta brackets, segno, coda, D.C., D.S., Fine or navigation text. P029 light-light section double bar followed by cancellation naturals. P048 thin-thick final barline. All other barlines ordinary; system beginnings are not repeat starts. Written route P001→P048 once. No playback schedule has yet been accessed.

## Gate decision

The repaired primary physical frame can safely address all 48 regions, printed clefs and partial capacities. Metadata classification defect noted above does not change the explicit frame. Remaining print ambiguities concern musical attachment, not physical addressing. Phase 1 frozen before reader evidence access. Full candidate event verification, final curve-to-note attachment and consumer validation remain future work; this freeze is not a PDF-accuracy certificate.
