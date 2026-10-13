# PHASE 3 FREEZE

Status: FROZEN_CORRECTIONS; source candidate NOT APPROVED. All phases remained separated. All Phase3 allowlisted hashes match. Nested candidate packet and source freezes match all references within the allowlist. References outside the allowlist were not opened.

Candidate reviewed: source_agent/UNVERIFIED_source.musicxml SHA-256 968507923b036706c3170e163b037127b815f3b939db6ccc2651c4b48ca9a0d1. Candidate has 1,388 XML note/rest elements, across all 107 physical regions and 15 systems. The print-grounded replacement target has 1,332 note/rest elements. printed_core_frozen.json is the exact frozen correction specification, with pitch, onset, duration, staff, minimal musical voice, written accidental, stem, beam, grace/tuplet status, ties, 244 mark records, and route. The specification is not a rendered delivery or final export.

phase3_review.json contains 450 addressed records: exact before/after regional CORE replacements, missing mark records, route repair, and five ledger/provenance mismatches. candidate_event_coverage.json covers every candidate note/rest, including agreement claims and events absent from disagreement reports. New/missing printed events are explicitly present in each regional replacement. Musical transcription was checked against the full print in both staves; repeated passages were inspected in their actual systems. Every candidate region was compared with the frozen printed target, not merely a list of disagreements.

## Principal findings

The candidate loses almost all printed MARKS: no dynamics, articulations, tempo, phrasing slurs, wedges or pedal survived as usable directions. Some ties survive with mismatched musical/engraving endpoints. MARKS.sep states none. The final directions/notations must be regenerated from the frozen print inventory, not ensemble confidence.

CORE includes copied adjacent regions, octave/clef errors, accidental errors, omitted chord members, duration changes, phantom voices and missing beams. Examples: P035 LH is the high Bb3+D4 half-note dyad, not a low three-note chord; P038/P039 require their own distinct figures; P049 first RH chord contains B-natural, not B-flat; P058 RH second chord includes D4 and F-natural as well as G4+B4+D5; P060 has no whole-bar F2 phantom; P064 is not P063; P066–070 bass figures must follow their actual locations; P091 is a half-note coda opening, not the prior cadence; P098 is a RH half-note chord over a full-bar LH rest, not two eighth-note attacks; P101–104 retain repeated single-note pitches in their sixteenth/quarter figures. P004's apparent flat is fingering 5/3: E4 is natural.

The candidate second-ending bracket incorrectly extends P060 through P090. The print stops it at the end of P060. Coda is a word at P091, not a coda symbol or navigation jump. The physical repeat traversal totals 158 regions and preserves the complete 2/4 capacities. Printed 2/4 must not change.

## Minimal musical topology frozen before application

Four musical voices are necessary and sufficient. Voice1 is RH principal line; voice2 is the simultaneous RH sustained inner line/chord at P025–026, P030–031, P083–084, P088–089. Voice3 is LH principal line through all bass/treble changes; voice4 is the simultaneous sustained LH chord at P030–031 and P088–089 and the held G#2 in P094. P030 and P088 require both independent RH lines and both independent LH lines at the same time: reducing below four would erase genuine simultaneity. The secondary lines are justified only where printed; no all-rest lanes are added in other bars.

The candidate's nine lanes cannot be repaired with one blanket Map. Source voice1/5/6 alternately carry RH principal and inner functions; source LH3/15 restart the same line, while LH4 mixes real inner material and incorrect notes. Use context-scoped replacements from printed_core_frozen.json. No cross-staff line is counted twice; clef changes do not create voices. Global role labels 1/2/3/4 are reviewer identities, not retained OMR numbers. Printed stem/beam and tie/slur endpoints are included in the correction target.

## Provenance and disagreement recheck

All 769 provenance entries were compared with candidate pitch groups; their candidate pitch sets occur in the recorded alternatives, but source attribution is not proof of correctness. All 351 disagreement entries, resolved and unresolved, were rechecked at their physical print locations; ensemble_disagreement_recheck.json preserves each original entry plus candidate/printed values and review record. Selection policy uses capacity-valid topology and weighted evidence; neither can authorize a changed rhythm or an invented mark.

Five note IDs have ledger/XML onset discrepancies: m007-s1-v2-e03, m011-s1-v2-e03, m060-s2-v6-e05, m067-s1-v3-e03, m072-s1-v2-e05. Their ledger positions do not describe their actual XML placement. All five are unprinted phantom claims removed by frozen corrections; preserve the original mismatch and regenerate final ledgers. This is a provenance/traceability issue despite matching file hashes.

The prepared source structural report says PROPER and no duration discrepancies, yet lists 19 broken tie-engraving issues and a phantom voice; its own preflight suggests mechanical merges. The score cannot be approved on that basis. No silent padding or trimming was accepted. All rhythm corrections follow visible note/rest shapes. Source coverage reports 494 uncertainties while uncertainties.json holds 495 items; neither count is a completion certificate. The refreshed manifest's GEMINI record list is empty despite reported eight historical API calls: no claim of independent Gemini coverage is made. Only the allowlisted provenance trail was inspected; unallowlisted observation files remain unopened.

## Remaining uncertainty and delivery conditions

Printed hairpin endpoints can lie between attacks. Musical anchors in the target are explicit, with medium confidence and source pixels preserved for focused recheck. A small dot near fingering3 at P102 LH q0.75 could be an isolated staccato or a scan/fingering speck; it is not added pending Juan. This uncertainty is not used to waive any playback or cursor failure.

Stage5 must copy the candidate, apply these frozen regional corrections only, regenerate all layers/ledgers from the exact final XML, render and inspect changed contexts, and execute real installed consumer gates. Any new musical interpretation after this freeze requires a numbered immutable erratum before application. No delivery is yet certified; no publication is authorized.
