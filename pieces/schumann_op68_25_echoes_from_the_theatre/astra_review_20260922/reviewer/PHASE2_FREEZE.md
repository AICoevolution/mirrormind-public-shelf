# PHASE 2 FREEZE

Completed under restored AUTHORIZE (authorization hash 11884931500f6b4de926ebf77cf8df2fd3bd17efc8a9f62dfd76e3a744948440), handoff 5870554da56a525d94384249f667bd98682dd140b40e0d2b73ccb093673b4c73. The renewed Phase 1 checkpoint is reviewer/resume_01/PHASE1_FREEZE.md, incorporating the unchanged original print inventory. The previous blocked freeze is historical and preserved. All 24 Phase 2 allowlist hashes and the repaired question-packet freeze dependency hashes pass. No Phase 3 candidate, model content, provenance, or disagreements accessed before this freeze.

## Correspondence: 33 regions / seven systems / two pages

phase2_correspondence_review.json records every region, direct printed melodic/rhythmic anchor, page/system, and each reader part/ordinal/raw label. SmartScore has 33 measures per part (P1 upper and P2 lower), hence 66 serialized part-measure records, not 66 physical bars. PlayScore and Audiveris have a single two-staff part. All map ordinal n to physical Pnnn after direct sequence inspection; SmartScore/PlayScore raw label=n, Audiveris raw label=n-1. Both actual locations of repeated music were inspected. No region split, omission, or merge was required to establish these correspondences. This confirms location, not note correctness.

All seven system packet claim arrays are empty, reflecting the supplied unmapped configuration. The allowlisted reader_claims.json supplies the actual evidence used here. The source maps and packets were not modified. They must not be mistaken for evidence of no notes or of reader agreement.

## Questions and independent controls

phase2_priority_answers.json answers all 24 priority questions by original ID. Missing raw m0/m33, opening declaration differences, and broad onset-drift claims conflate unlike raw labels. P015 upper chord at both closing attacks is E4 G4 C5 E5 natural: reject PlayScore flats. P028 lower A3 remains natural at all five questioned attacks: upper A#4 does not propagate to lower A3.

phase2_controls_review.json preserves original controls and all three failed verdicts:

- control-1: P001 upper first pitch E5, not F5; its sixteenth duration is correct.
- control-2: P017 upper opening E4/C5/E5 is an eighth, not a quarter.
- control-3: P033 upper opening G#4/B4 quarter, not C#5.

There are zero intersection controls in question_packets/controls.json. Parent controls are independent claims, not successful calibration. Baseline chooses PlayScore and calls it structurally proper; that does not validate its pitches, voices, or marks. Baseline state and questions were inspected; the selected 24 priorities are all resolved above. Additional baseline questions remain corroborating reader evidence, not majority-vote answers.

## CORE observations by physical system

1 (P001–4): all readers locate the pickup and main patterns. SmartScore invents G6 in P002; Audiveris adds an upper phantom rest. Audiveris misses F-double-sharp in P004. Held lower chords and their ties must be checked individually.
2 (P005–9): SmartScore invents tuplets in P006, corrupting durations. P008 has a sustained lower bass plus independent moving chord line; duplicate same-pitch attacks from shared noteheads require musical interpretation, not indiscriminate lane merging. Both phrase contours at P008 and closing P009 are printed.
3 (P010–15): every reader supports the directly seen dotted-sixteenth/thirty-second P010 pickup. Framing prose is wrong but capacity correct. Audiveris P011 lower dotted note is shortened. PlayScore P015 flats are unprinted.
4 (P016–20): Audiveris shortens P016 upper dotted pair and misplaces the later attacks of P017. SmartScore P018/P020 serializes concurrent voices as sequential and overruns capacities. Sustained E4/E5 at P019 starts as a dotted quarter in print; PlayScore and Audiveris omit its dot and introduce a gap or malformed rhythm. Audiveris P020 omits lower upper-staff chord tones. A passing duration check cannot repair these facts.
5 (P021–25): upper moving and sustained lines are independent in P021 and join in P022. SmartScore invents lower tuplets in P021/P023. Audiveris shortens sustained and dotted material in P021, omits C4 in P022. PlayScore P022 creates unnecessary voice fragments and an overlong C5. Lower rests in P024/P025 are printed; an all-rest extra voice elsewhere is not justified by these rests.
6 (P026–29): check actual repeated passages, not copies. SmartScore omits C4/E4 at P026 onset 3/2. PlayScore incorrectly sharpens lower A3 in P028. All-reader upper motifs still need independent candidate audit.
7 (P030–33): P031 peak is C-natural6 with dotted-sixteenth duration, then E5 thirty-second; P032 has different ending from P008. Audiveris loses G#4 and adds a spurious long chord in P032. Final P033 slurs are phrases, not ties.

## MARKS and ROUTE comparison

Full reader event/notation/direction/barline evidence inspected is retained in phase2_reader_evidence_reviewed.json; the print inventory remains PHASE1_FREEZE.md. Readers have complementary omissions. SmartScore misses many short slurs (P002/3/4/6/7/27/28/30/31), invents a wedge in P004 and tuplets from fingerings, corrupts tempo words, mistakes cresc. for f in P006, and splits or shifts long phrase endpoints at P020–22. PlayScore omits the opening tempo/metronome, most horizontal accents, P003 slur, cresc./dim. text, some peak staccatos (P008/P031/P032), and misattaches P018 p at onset 0 instead of the beamed entry; its P019 moving-line staccato is not printed. Audiveris loses metronome and ff, most cresc. text, misreads augmentation dots as staccatos in P018–21, converts P020–22 upper phrase to a tie, and introduces an ornament near P026 accidental. No reader supplies a reliable complete MARKS layer. Printed crescs at P006 and P030 and dim. at P024 must be retained even when all readers omit them. Do not duplicate one printed chord articulation on every chord member merely because SmartScore does.

All readers' ordinal repeat locations match print: backward after P009, forward before P010, backward after P033. No endings/navigation elsewhere. Printed playback route is 1–9 twice then 10–33 twice. SmartScore expresses the same barlines in both staff-parts; those are one route, not repeated route instructions.

Long slurs at P018 onset 1/2→P020 onset 0 and P020 onset 1/2→P022 onset 0 on each staff must be preserved as connected spans. Lower ties P002→P003 and P004→P005 require all three chord members. Unanimity is not a print certificate; the Phase 3 audit must cover all events and omissions, not merely these identified disagreements.

Freeze decision: Phase 2 complete for correspondence, selected priorities, independent controls, reader evidence/omissions, and MARKS/ROUTE comparison. Proceed to Phase 3 only after hashing this file. Human outcomes remain null.