# Volksweise — independent review complete; delivery technically blocked

The print audit and supported corrections are complete. **The candidate is UNVERIFIED and is not ready for human delivery.** The production renderer places pedal-release stars on top of “Ped.” in P004, P013, P020, P021, P025, P029, P036, P037 and P041. See [blocker](reviewer/consumer_blockers.json), [measured geometry](validation/pedal_geometry.json) and [P004 detail](validation/pedal_collision_P004.png). Repair the consumer, then recheck Stage 5 in a new workspace with this exact XML and Phase 1–3 evidence preserved.

## Final human attention, after the technical repair
- **TRIPLET-P020** and **TRIPLET-P036**: confirm initial triplet interpretation where the printed numeral resembles fingering.
- **PEDAL-HAIRPIN-TIMING**: confirm spatial pedal-release and diminuendo endpoint timing.
- **P009-INNER-PITCH** is resolved by print enlargement: its second chord contains A3/F#4 only.

Questions, provisional treatments, evidence and null human outcomes are in [human_attention.json](human_attention.json). No human answer or signature is inferred.

## Candidate and checks
[Corrected primary MusicXML](delivery_final/UNVERIFIED_Grieg_Op12_05_Volksweise_Astra_import.musicxml). Four continuous musical lines, five staff/voice lanes, 495 note/rest members and 473 sounding attacks. Printed 3/4, one-quarter pickup and complete final bar retained. All 41 regions, 367 provenance records and 122 disagreements were reviewed, including unanimous claims. Missing melody, grace notes, beams, directions, slurs and accompaniment errors were corrected from print. [Change ledger](change_ledger.json) preserves exact before/after XML; [frozen specification](reviewer/correction_spec.json) states musical decisions.

PROPER, CORE rebuild and actual Apply, MARKS exact member endpoints/placement, independent playback schedule, all 473 production viewer mappings and VexFlow duration checks pass. Cross-staff slur geometry passes at 1350/1 and 1000/0.9 layouts, with screenshots visually inspected. CORE and MARKS readiness do not override the failed notation-rendering and focused-visual gates. The generic essential-notation probe incorrectly permits the pedal collisions; its nominal PASS is retained as limited evidence, not adopted as delivery readiness.

A redundant sound-only pedal carrier initially made OSMD drop 21 measures after the production adapter removed its direction type. Numbered [technical erratum 001](reviewer/ERRATUM_001.json) removed only redundant sound carriers, preserving pedal symbols, times and staves. The primary now renders every measure, but the separate pedal-position failure remains. No production code was modified.
