# Phase 2 reader-evidence freeze

Frozen after Phase 1; candidate and ensemble evidence unopened. Current allowlisted hashes and nested question-packet freeze hashes match. All five system packets read: every reader claim list is empty. The supplied correspondence maps all 144 reader/region slots to empty lists; these packets cannot substantiate agreement. Raw reader_claims.json nevertheless supplies the reader element contents and is expressly allowlisted. Derived reviewer correspondence is saved in phase2_correspondence.json; prepared maps are untouched.

## Correspondence and coverage

All 48 physical regions of the five systems were compared to raw reader event sequences. SmartScore has 48 elements in EACH of P1 and P2 (96 records, not 96 physical bars); PlayScore has 48 grand-staff elements; Audiveris has 48 grand-staff elements numbered 0–47. For each reader/part, ordinal n corresponds to Pnnn. This is supported by the opening pickup, each local melodic contour, both key boundaries, the double bar at 29, second pickup at 30 and final three-eighth chord/rest pattern at 48. A missing/malformed event or overflow inside a reader bar is not automatically a shifted bar. Audiveris P018 is particularly damaged (a lone C5 whole-bar claim); its slot is identified from its neighbors and key boundary, not certified by that note. Full raw event digest retained for all 48 bars and all readers. This map does not certify any individual musical claim.

All 32 published priority questions have individual print answers in phase2_priority_answers.json. Several frame questions compare raw labels 0/1 or 47/48 and therefore compare different physical bars. Their assertions that a pitch difference must be a clef or octave sign are rejected: no such sign is printed. Polyphonic note-presence questions often falsely present simultaneous voices as mutually exclusive alternatives. Printed C3 at P003/P011, E4 at P015, A4 at P022, lower A3/C4 at P031, inner A4 at P037/P039, E3 at P038, and the multiple P045 voices must all be preserved.

## Independent controls

question_packets/controls.json is empty: zero three-reader deterministic controls. This is lack of control evidence, not a pass. The three parent controls were independently inspected. Control-1 passes for the P001 G#4 eighth. Control-2 FAILS: P024 E5 is an eighth, not a quarter. Control-3 FAILS: P048 bass is A1/A2, not E2. Original pass verdicts remain in the source and are explicitly contrasted with reviewer findings in phase2_controls.json. A failed control does not discredit every claim from that source but prevents trusting its calibration.

## Omissions, disagreements and shared blind spots

S1/P001–009: readers identify the melodic patterns but PlayScore omits C3 at P003 and substitutes/duplicates G#3 for the sustained E3 at P006; SmartScore corrupts cross-staff P005 and inserts triplet values at P007. Audiveris loses the sharp and sustained line at P006 and drifts lower events at P008/P009. P009 D#4 accidental is clear enough to require direct checking, not majority vote.

S2/P010–019: cross-staff handoffs remain vulnerable. P011/015 omissions, P013 wrong bass durations/pitches, P016 dotted duration, P017 accidental/chord membership and P018/P019 rests and sixteenths need candidate review. Audiveris almost entirely omits P018; all-reader comparison based on raw numbers is misleading.

S3/P020–029: verify every sixteenth at P021 and every inner sustained line. P021 cross-staff last A4 is not a rest; P022 inner A4 omitted by PlayScore; P023 durations and A#4 line damaged; P024 invented triplet is not printed. P026/P027 voice splits and P028 double-stem/unison events cannot be merged merely because pitch agrees. All readers mishandle part of P029 lower rhythm; its capacity is 3/2, not 2 or 5/2. No numeric fingerprint substitutes for the actual printed count.

S4/P030–039: PlayScore pads P030 with rests and omits its lower chord and P031 lower chord. Cross-staff P032/P034, bass P035, inner P037, missing bass P038 and P039 inner dyad need independent audit. P030→P031 lower D4→C4 is a SLUR, not a tie: this refines the provisional Phase 1 curve classification. Same-pitch ties and unlike-pitch phrase arcs must be distinguished at both ends.

S5/P040–048: SmartScore inserts triplet interpretation in P040 and overflows P042; Audiveris duplicates upper E5 at P040 and F4 at P042; SmartScore P044 C6 is a gross cross-staff pitch error. P045 contains multiple independently moving lines; PlayScore's voice fragments/rests are not a legitimate topology. P047/P048 need complete upper chord and bass octave membership. Parent E2 control is contradicted even by reader pitches but the printed bass-clef positions, not agreement, establish A1/A2.

## MARKS against the print inventory

All reader direction, notation, tie and barline claims were extracted by region; full digest retained. SmartScore splits/corrupts opening tempo text, attaches title as in-score words, starts/ends many slurs on wrong inner notes, adds nonprinted tenutos, P007/P040 tuplets, and a spurious P023 fermata. Its bass P003→P004 tie is not supported where D3 changes to C3 and back; do not connect nonadjacent D3 attacks as a sustain. PlayScore omits many accents and textual cresc./dim./ritard. and shifts wedge offsets negative by 1/12; sparse marks are not evidence of absence. Audiveris converts cresc./dim. into f/p, adds an unprinted turn at P032 and isolated tenuto/staccato/accent noise; it retains useful cross-staff slur clues but also false/duplicate attachments. The print contains arpeggiation at P009/P017, which not every reader retains. Cross-system P009→P011 and P039→P042 phrases must be joined despite reader breaks. Slur endpoints at P003/P004 and P044/P046 need direct paired-note verification. All fingerings are excluded, including substitution arcs that readers may mistake for tuplets/ornaments.

## ROUTE

SmartScore and Audiveris encode P029 light-light double bar and final light-heavy bar. PlayScore does not preserve the P029 section bar in the claims but retains the final. No repeat/navigation is supported by the print or reviewed reader barlines. Route remains P001–P048 once, 92 quarter units under explicit capacities; this is independent of any candidate schedule.

## Freeze scope

Reader phase complete with disclosed content omissions and attachment ambiguities. No candidate or ensemble source is used here. Baseline claimed agreement, proper=true, voice counts or ear1_ready are not accepted as PDF-accuracy proof. Candidate phase must verify every note/rest and all marks, including the all-reader blind spots above. No correction has been applied. Human outcomes remain null.
