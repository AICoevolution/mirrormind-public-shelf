# Astra review — technical rendering block

The complete print review and supported musical corrections are finished. Delivery is **not ready**: the installed production renderer overlaps the two inner eighth-note heads at **P007, staff 2, onsets 2 and 2.5**. See [focused evidence](viewer_delivery/P007_inner_collision.png) and [technical blocker](reviewer/phase5_blockers.json). P025 has related cramped spacing. A consumer repair and new Stage 5 recheck are required; preserve this exact XML and all review freezes.

Corrected primary: [UNVERIFIED_schumann_op15_06.musicxml](delivery_final/UNVERIFIED_schumann_op15_06.musicxml). This remains UNVERIFIED pending Juan's visual, structural and listening verification.

Unresolved musical questions for Juan: exact chord-member attachment of six slurs (HA-SLUR), and precise time endpoints of four hairpins (HA-WEDGE). Their explicit provisional treatments are in the **final** [human attention file](delivery_final/human_attention.json). The root human_attention.json is preserved historical Stage 4 evidence, superseded for delivery by the final file and numbered errata. P007's hairpin direction is resolved by focused print as diminuendo; it was mistakenly called crescendo in the inherited inventory.

All 27 physical regions, four systems, 472 candidate members and every expressive/route element were reviewed. All 322 priorities and all 131 ensemble disagreements were checked. The primary contains 443 members (441 pitched notes and two printed quarter rests). Three continuous musical lines use five staff-specific SEP lanes: principal voice1, brief independent inner voice2, bass voice3. Source voice fragments and unprinted rests were removed; simultaneous independent notes were not merged.

Corrections and exact before/after values are in change_ledger.json and the two supplemental erratum ledgers. ERRATUM-001 preserves printed courtesy accidentals; ERRATUM-002 corrects P007 diminuendo and upward inner eighth stems and relocates equivalent interstaff hairpin carriers; ERRATUM-003 applies top-to-bottom voice numbering and readable title metadata. Earlier frozen evidence is unchanged.

PROPER passes with printed 3/4 and declared pickup/partial capacities. The independently expanded 36-region route has 96 quarter-note beats; all 582 scheduled attacks match pitch, voice, onset, duration and source time at the analyzer's documented millisecond serialization precision. Installed viewer mapping covers all 582 attacks; all 27 measure durations and all 443 VexFlow note/rest durations match. These successes do not waive the visual failure.

CORE actual Apply is byte-exact and its independent rebuild preserves sounding pitches/timing/member ties; however the standalone rebuild adds absent-lane rests and is NOT PROPER. CORE rebuild readiness is partial, separately reported. MARKS Apply preserves exact slur-member endpoints, placement/orientation, articulation placement and core projection. ROUTE Apply preserves core and route. Diagnostic rebuild files are not alternative primary deliveries.

No production code, authorization, source candidate, controller state or historical review was modified. No publication performed.
