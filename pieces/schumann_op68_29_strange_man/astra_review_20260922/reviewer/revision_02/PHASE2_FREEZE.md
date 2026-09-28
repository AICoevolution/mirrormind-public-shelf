# PHASE 2 FREEZE

Reader-only evidence reviewed after Phase 1 freeze; no candidate, model content, ensemble provenance or disagreement file accessed. All Phase 2 allowlisted hashes match. The nested question-packet freeze also matches all 19 referenced files. This is not approval of the baseline or reader correctness.

## Correspondence and coverage

The prepared reader_correspondence.json leaves all 321 reader/physical-bar map entries empty. All 15 question-system packets contain zero reader claims, although priorities are present in several. Raw reader_claims.json is sufficiently complete to reconstruct content correspondence in this workspace without changing prepared evidence. The resulting reader_correspondence_reconstructed.json records every physical region, reader ordinal, raw label, opening fingerprint, page/system evidence and scope.

Direct musical sequence checks establish: PlayScore ordinal p = Pp throughout; SmartScore ordinal p = Pp through P034, its ordinal35 is an extra empty/signature element, and ordinal p+1 = Pp from P035 through P107. Audiveris ordinal p = Pp through P086, P087 is omitted, and ordinal p-1 = Pp from P088 through P107; raw labels resume at 88. All mappings were assessed against actual systems, including repeated sections, cadences, half-note sequences, changes of key, and closing figures. Equal measure counts were not used as proof. The 321 records include Audiveris's explicit P087 omission. Correspondence confirmation is not confirmation of each reader event.

System coverage: 1: P001–006; 2:007–013; 3:014–020; 4:021–027; 5:028–034; 6:035–042; 7:043–050; 8:051–059; 9:060–065; 10:066–071; 11:072–077; 12:078–083; 13:084–090; 14:091–099; 15:100–107. Both staves and every reader were included. No physical frame change is needed for this local reader mapping.

## Priorities and controls

All 37 priorities have individual answers in priority_answers.json. Many frame detectors compare unmatched raw measure numbers after SmartScore's inserted empty element. Their categorical claim that a constant offset must be a clef/octave sign is not justified. The print has no octave-transposition sign. The reconstructed map resolves which musical region each claim actually concerns. Clef timing must distinguish boundary cautionaries and system reprints from changes affecting notes.

All three parent controls labelled pass fail direct print review; exact before/printed values are in controls_recheck.json. The opening top pitch is D4, not A4, and its chord is eighth, not quarter. P053 starts with E5+G5 sixteenths, not A4 eighths. P107 LH octave is D2+D3 eighth, not D3 quarter. question_packets/controls.json is empty. These failures remain evidence and are not converted to successful calibration.

## Reader CORE weaknesses and shared blind spots

SmartScore's extra empty35 shifts subsequent raw-number comparisons by one. Audiveris misses P087, misses several mid-score clefs, inflates full rests/extra phantom notes, and sometimes changes dotted values. PlayScore supplies strong rhythmic context but misses notes and has wrong clef-derived LH pitches at P039–042. The actual G-clef transition is P038 end, effective P039. Audiveris also misreads LH P055–059 after missing the bass return and LH P104–107 after the final bass change.

Specific print-checked disagreements: P022 RH q1 A3+C#4+E4 eighth, no phantom sustained F4; P025 RH printed F# must not follow SmartScore's natural; P030 LH sustained A3+D4 under moving F4/G4, not A2 or Bb3; P031 treble continuation must precede mid-bar bass change; P051 LH F4+A4 half chord, PlayScore missing F4; P083 RH F# at both q0 and q1.75, PlayScore natural wrong. Audiveris P084 dotted figure loses a dot and advances its second-beat attack. SmartScore P088 contains an excessive duration that pushes an attack to q2. PlayScore P030/P088 replaces a printed dotted eighth in the upper moving line with eighth plus rest. P094 has a genuine sustained inner LH note, unlike all-rest voice fragments elsewhere. None of these can be resolved by bar-sum arithmetic alone.

## MARKS comparison against frozen print inventory

All raw direction, articulation, tie/slur and barline claims were inspected by reader ordinal after correspondence reconstruction. Phase1 inventory supplies the complete print answer; reader omission or consensus never overwrites it.

All three miss the opening metronome declaration quarter=126. PlayScore misses the tempo text; Audiveris reads V1goroso, SmartScore appends a dash. All three miss cresc. at P093 and ff at P101. Several fingerings/specks become spurious staccato or word directions; do not copy those into MARKS. All readers omit some real accents (e.g. RH P020 q1 and LH P101 q0). SmartScore and PlayScore omit RH P025 q0 despite the printed pointed accent. Audiveris recognizes only some levels of multi-note ties, treating others as slurs.

P013/P014 and P071/P072 sf placements differ from raw offset positions: a dynamic serialized at previous bar end is not automatically attached to that previous attack. P017 q1 is ff, not PlayScore f, and omitted by the other readers. P037 is pp, not SmartScore fp+p or PlayScore ppp; Audiveris omits the dynamic. P041 is pp, not Audiveris p. Hairpin onsets frequently move to q0.75 or q1.75 in readers despite print anchors around q1; cross-system LH crescendos at P006/007 and P065/066 are truncated to the source system by readers. P083/084 hairpin is also truncated or lost. P038/P054 swells require both wedges; one is missing or wrongly ordered in some readers.

SmartScore frequently encodes phrase slurs as ties joining equal-pitch endpoints across intervening attacks (P037, P041–042, P053–054, P093–094). These must remain slurs through the internal notes. Conversely RH P030/031 and P088/089 sustained inner-note arcs are ties, not PlayScore/Audiveris generic slurs. Their lower chord continuity is independent of the moving upper line. Do not retain fabricated upper-voice ties where pitches differ across those boundaries.

PlayScore omits all printed pedal pairs. SmartScore and Audiveris retain pedal with timing differences: printed releases near q1.5 are often mapped q1 by Audiveris; SmartScore P042 depress is delayed. Audiveris also introduces an unsupported pedal at P051. Only the five pairs frozen in Phase1 are printed. Pedal at P098–099 is present in SmartScore/Audiveris and missing in PlayScore. P095 arpeggio and P095–096 staccato groups are real; other isolated staccatos must be checked against pixels rather than inherited from OCR fingerings.

## ROUTE comparison

Printed route: 1–12,1–11,13;14–33,14–31,34;35–42 twice;43;44–59,44–57,60;61–107. First-ending P032–033 and P058–059 each span two physical regions. SmartScore mislabels P034 ending as 1,2 and omits the forward repeat at P044. Audiveris omits the backward repeat after P042 and after P059 and mislabels P060 second ending as 1. PlayScore omits the P060 second-ending declaration and changes the P090 thin-thin double barline to light-heavy. Endpoint handling for several endings is incomplete. Coda is printed text at P091, sequentially reached: SmartScore fabricates a coda symbol at P092; PlayScore omits text, while Audiveris captures Coda at the correct physical location. There is no navigation jump there.

## Evidence closure and readiness

Raw reader claims remain unchanged. Newly generated correspondence, priority answers, and control verdicts are reviewer artifacts only. The five Phase1 source/configuration JSONs, page images and PDF remain the only print inputs. All uncertainty about exact between-attack hairpin tips remains visible from Phase1. Phase2 freeze permits candidate inspection; it does not endorse baseline readiness flags, parent confidence, or the three failed controls. Human outcomes remain null.
