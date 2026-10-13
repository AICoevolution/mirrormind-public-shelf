# Phase 3 completed independent audit

The historical partial records and checkpoint remain byte-identical. The completed correction specification is **phase3_completed_event_spec.json**, with member addresses, exact durations/pitches, logical voices, stems, beam memberships, ties, slur endpoints and placements, words, dynamics, wedges, fermatas and route. Its complete candidate comparison is phase3_completed_review.json; the historical phase3_review.json remains a partial record and must not be applied.

All 25 physical regions and both staves have been examined on their actual system images, including repetitions. Every one of the 408 candidate members is addressed. Grace figures were examined in focused crops. Full provenance and disagreement rechecks are in separate indexed files. The duration report has no arithmetic discrepancies, but it is not musical proof. Candidate omission of all expressive notation is corrected. No tuplets, pedal, articulations or unprinted navigation are added; fingerings are omitted.

Five musical lines are required by simultaneous independent timing in P011/P015. Exact context-specific assignments and overlap checks are in phase3_topology_spec.json. Cross-staff beams retain one logical voice. No source-label fragment or all-rest phantom lane is justified.

Refinements from the historical working inventory: P009 B-natural3 and C5 grace; P015 independent F5 quarter; P017 inner beam crosses to lower staff, separate G4 eighth at onset 3/2, and C4 grace after the final quarter; P024 sustained C-flat4 resolved from its ledger-line position; P025 separate Bb3 quarter and C3 shared durations. Source P010 has no sustaining tie through the following P011 rest. P005/P021 final C4 is the melody pickup continuation.

Ordinary uncertainties are explicit in ../human_attention.json: small-note/open-head overlap in P003/P007/P019, selected chord-member curves, shared C3 durations in P025 and close phrase endpoints. These are provisional choices for an UNVERIFIED delivery, not confirmed corrections or technical blockers. No human answer has been invented.

phase3_completion_freeze_hashes.json binds the final specification, complete comparison, provenance/disagreement coverage, topology and attention list. Original phase3_hashes.json continues to bind every current allowed input; resume_integrity_verification.json confirms authorization and all historical/current hashes. No later-phase request was accessed and no candidate was modified before this freeze.
