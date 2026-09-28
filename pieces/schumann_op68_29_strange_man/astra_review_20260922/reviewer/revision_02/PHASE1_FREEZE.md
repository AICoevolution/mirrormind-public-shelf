# PHASE 1 FREEZE — repaired run, revision 02

Print-only review. Phase 2 and Phase 3 not accessed. The earlier blocked checkpoint remains immutable in the parent reviewer directory. New handoff ed651f5b80d1693279b45de4d766f62b6a7b2d5e28f1b73dc46d452589947d85; matching AUTHORIZE file f3e237bf649be775eb3d7364ef4c320db5a75a5e2e9f92bcf26e65521c14af58. Both allowlist representations agree; all nine source hashes match.

## Address convention and complete physical census

Pnnn = physical printed region, one-based. q = onset in quarter-note units from the left barline, not a change to printed meter. RH/LH = staff 1/2. Chord-attached articulation applies to its printed attack, not once per chord member. A span endpoint described by q is attached to the event at that onset unless explicitly stated as release or bar end. Each derived print_system_NN.png uses x offset 70 from its source full page; y offset is the corresponding locked page-system boundary. No pre-existing system crop was accessed.

| Page / printed folio | System | Regions | Count |
|---|---:|---|---:|
|1 / 45|1|P001–006|6|
|1 / 45|2|P007–013|7|
|1 / 45|3|P014–020|7|
|1 / 45|4|P021–027|7|
|1 / 45|5|P028–034|7|
|2 / 46|6|P035–042|8|
|2 / 46|7|P043–050|8|
|2 / 46|8|P051–059|9|
|2 / 46|9|P060–065|6|
|2 / 46|10|P066–071|6|
|3 / 47|11|P072–077|6|
|3 / 47|12|P078–083|6|
|3 / 47|13|P084–090|7|
|3 / 47|14|P091–099|9|
|3 / 47|15|P100–107|8|

Directly counted: 107 musical regions, 15 grand-staff systems, three pages. No pickup, terminal partial, split-capacity region, printed meter change, tuplet, or grace group. Every physical region has capacity 2 quarter units. Opening declaration is 2/4 on both staves, never to be replaced by inferred arithmetic. Half-note regions are complete bars. Full-bar rests at RH P059 and LH P098 occupy the declared capacity; their whole-rest glyph does not mean four quarter units. Final P107 is eighth + eighth rest + quarter rest, not quarter + rest as the old prose claimed. This descriptive error does not change the correct 2-quarter capacity or addressing.

The supplied x boundaries coincide with the musical barlines in the system images. Signature-only areas do not count as bars. P035 starts after the forward repeat; P055/P056 are separate half-note bars; P084 is a single bar. No physical/capacity blocker remains.

## Key and clefs

Opening one flat; two flats effective P035 through P059 inclusive, with cautionary two flats at the end of page 1. One flat effective P060, with cautionary at system 8 end. No mode inferred as a framing constraint. RH G2 throughout. LH opening F4. Printed lower-staff changes:

- P029 q1 to G2; P031 q1 to F4.
- G2 glyph at P038 end, after the last rest, effective P039 q0. Repaired FRAME-1 confirmed directly.
- F4 glyph at P042 end, effective P043 q0 (and bass is re-established for the repeat to P035).
- G2 glyph at P050 end, effective P051 q0.
- F4 before the P055 first chord, effective P055 q0; glyph visually precedes the boundary at the right of P054. REGION_START in the lock is usable as an effective-time convention, not literal glyph-side placement.
- P087 q1 to G2; P089 q1 to F4.
- P096 q0.5 to G2, after its first eighth.
- F4 before the first P104 chord, effective P104 q0; glyph visually precedes its barline at P103 end. Same distinction between printed glyph position and effective time applies.

System-start clef repetitions are not new changes. The P055/P104 effective clefs are safe; preserve the printed boundary-side placement in any rendering work. Lock prose saying a bass quarter plus rest after P031/P089 q1 is inaccurate: the remaining beat is an eighth and eighth rest. The numeric clef onset remains correct.

## MARKS inventory

No fingerings are included. No fermata, trill, mordent, turn, octave line, or other ornament was found. No tempo change follows the opening Vigoroso con forza, quarter=126. Coda is a section label, treated with ROUTE below. All marks below were read at their actual printed locations.

Dynamics/text (q0 unless specified; between staves unless placement noted):

|System|Printed marks|
|---|---|
|1|P001 f; opening tempo text and metronome above RH.|
|2|P013 sf below LH.|
|3|P014 sf above RH; P017 sf at q0 and ff at q1 between staves.|
|4|P021 sf at q0, f at q1.|
|5|P029 sf between staves; P033 sf below LH.|
|6|P035 mf; P037 pp; P039 mf; P041 pp. Pedal pairs separately below.|
|7|P043 ff.|
|8|P051 p; P053 pp; P055 p; P057 pp; P058 sf at q1; P059 ff. No pedal marks on this system.|
|9|P060 f.|
|10|P071 sf below LH.|
|11|P072 sf above RH; P075 sf at q0, ff at q1.|
|12|P079 sf at q0, f at q1.|
|13|P087 f; P088 sf at q1.|
|14|P091 p; P093 cresc.; P095 mf; P097 f; P098 pp; P099 f.|
|15|P101 ff.|

Articulations: ^ denotes printed pointed marcato, > the horizontal accent. Every listed onset is a separate glyph. Absence of a repeated articulation is intentional in this inventory.

|System|RH|LH|
|---|---|---|
|1|^ P001:0; P002:0,1; P003:0; P004:0; P005:0; P006:1|^ P001:0; P002:0,1; P003:0; P004:0,1; P005:0|
|2|^ P009:0; P010:1|^ P009:0|
|3|> P018:0,1; P019:0,1; P020:0,1|none|
|4|^ P022:0,1; P024:0,1; P025:0; P026:1|^ P022:0,1; P023:0; P024:0,1; P025:0,1|
|5|none|none|
|6|> P035:0; P036:0; P039:0; P040:0|> P035:0; P036:0; P039:0; P040:0|
|7|^ P043:0; P044:0,1; P045:0; P046:0,1; P047:0; P048:0,1; P049:0; P050:0,1|same as RH|
|8|> P051:0; P052:0; P055:0; P056:0|^ P059:0|
|9|^ P060:0; P061:0,1; P062:0; P063:0,1; P064:0; P065:1|^ P060:0; P061:0,1; P062:0; P063:0,1; P064:0|
|10|^ P068:0; P069:1|^ P068:0|
|11|> P076:0,1; P077:0,1|none|
|12|> P078:0,1; ^ P080:0,1; P081:0; P082:0,1; P083:0|^ P080:0,1; P081:0; P082:0,1; P083:0,1|
|13|^ P084:1; > P087:0|> P087:0|
|14|> P091:0; P092:0; P095:0. ^ P094:0; P097:0,1; P099:0,1. Staccato P095 and P096 at all four eighth attacks.|^ P094:0; P097:0,1; P099:0,1. Staccato P095 and P096 at all four eighth attacks.|
|15|^ P100:0,1; P101:0; P102:0; P103:0; P104:0; P105:0; P106:0; P107:0|same as RH|

Additional articulation: RH P095 q0 has an arpeggiation vertical wavy line before the chord. Numerals 1–5 are fingerings, including those near sixteenth groups; none is a tuplet number. At P101–104 the rests in the short gaps are sixteenth rests, not staccato marks.

Hairpins, with their visual ends and musical attachment neighborhoods:

- RH P005 q1 → P006 q1 crescendo; LH P006 q1 → P007 q1 crescendo, split across systems.
- RH P009 q1 → P010 q1 crescendo; LH P010 q1 → P011 q1 crescendo.
- Between staves P015 q1 → end P016 crescendo, ending before P017 sf.
- RH P025 q1 → P026 around q0.75 crescendo; LH P026 q1 → P027 q1 crescendo.
- Between staves P029 q1 → P030 around q0.75 crescendo.
- P038 RH/between: crescendo over the first two sixteenths (q0 to about q0.5), diminuendo from about q0.5 through the eighth attack at q1. Preserve separate wedges and the gap near the middle.
- P054 between: same local swell around its sixteenth/eighth figure; no extrapolation from P038 pedal.
- RH P064 q1 → P065 q1 crescendo; LH P065 q1 → P066 q1 crescendo, split across systems.
- RH P068 q1 → P069 q1 crescendo; LH P069 q1 → P070 q1 crescendo.
- Between P073 q1 → end P074 crescendo, ending before P075 sf.
- RH P083 q1 → P084 around q0.75 crescendo across systems; LH P084 q1 → P085 q1 crescendo.
- Between P087 q1 → P088 around q0.75 crescendo, ending before P088 sf at q1.
- Between P095 q0 → end P096 crescendo.
- Between P100 q0 → end P100 crescendo before ff at P101.

Exact hairpin tip/extent can lie between attacks. Approximate neighborhoods above must be reconciled against pixels when encoding attachment; they are not a license to quantize ambiguities without recording them.

Slurs (different-pitch phrase curves; none carried across systems): both staves P037, P038, P041, P042, P053, P054, P057, P093 and P094 each have a single local slur from first attack q0 through the eighth at q1. Upper/lower placement follows stems and the print. P094 LH also has a sustained lower note under the moving group; do not interpret the phrase slur as a tie for that independent line.

Ties (each chord member with an arc must be preserved):

- RH P006 q1 → P007 q0: three-member chord, cross-system.
- RH P010 q1 → P011 q0: three-member chord.
- RH P025 q1 → P026 q0: sustained lower note; LH same on both octave members.
- RH P026 q1 → P027 q0: three-member chord.
- RH P030 q1 → P031 q0: inner sustained note below moving upper voice; LH same boundary has two lower sustained chord members under moving upper notes.
- RH P065 q1 → P066 q0: three-member chord, cross-system.
- RH P069 q1 → P070 q0: three-member chord.
- RH P083 q1 → P084 q0: sustained lower note, cross-system; LH same on both octave members.
- RH P084 q1 → P085 q0: three-member chord.
- RH P088 q1 → P089 q0: inner sustained note; LH same boundary has two lower sustained members.

Pedal: printed Ped. at LH P037 q0, P038 q0, P041 q0, P042 q0; each release star lies near the final rest at q1.5 of the same bar. Ped. at P098 q0, release at P099 q0. These are the complete five printed depress/release pairs. No pedal inferred in analogous unmarked bars.

## ROUTE inventory and intended traversal

- Opening has no forward-repeat glyph; backward repeat closes P012. First ending P012 only; second ending P013 only, closing with thin-thin double barline.
- Forward repeat before P014. First ending P032–P033 inclusive, backward repeat after P033. Second ending P034 only; following two-flat signature is cautionary for P035.
- Forward repeat before P035; backward repeat after P042. Clef must resolve to bass on return to P035.
- P043 precedes the forward repeat before P044. First ending P058–P059 inclusive; backward repeat closes P059. Second ending P060 only, with one-flat key restored.
- Thin-thin double barline after P090. Printed word Coda at P091; no coda navigation symbol, segno, D.C., D.S., To Coda, or Fine anywhere. Coda is reached sequentially and continues through P107, not only through P099.
- Thin-thick final barline after P107. No repeat or new movement beyond it.

Expected physical traversal: 1–12, 1–11, 13; 14–33, 14–31, 34; 35–42 twice; 43; 44–59, 44–57, 60; 61–107. This is the print-grounded route to be independently compared with reader and candidate route claims later.

## Print ambiguities and evidence limits

Hairpin tip positions in the neighborhoods above are between attacks and should not be over-specified from rhythmic convenience. Small adjacent tie arcs in the three-note chords (especially cross-system P006/007 and P065/066) are crowded but three levels are visible. P094 lower staff contains a longer sustained bass note under its slurred line; it is a voice-topology concern to inspect in CORE, not a frame defect. No damaged region prevents use of this physical frame. Print bears small specks below systems that are not automatically staccato marks; event-attached marks must be checked locally.

Frame status: usable with documented effective-time versus glyph-side distinctions at P055/P104. Reader correspondence itself has not been opened. Phase 1 is frozen before its exposure. All printed regions and both staves have been covered for framing, marks and route; subsequent phases may record numbered print-grounded errata if finer inspection changes an interpretation.
