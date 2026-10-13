# Humming Song — UNVERIFIED delivery

The three isolated review phases, correction application, real consumer validations and final visual recheck are complete. The prepared run is unchanged; all44 authorized evidence hashes still match. No queue, orchestrator, production code or publication was touched.

Primary file: delivery_final/UNVERIFIED_Schumann_Op68_03_Humming_Song_Astra_import.musicxml
SHA-256: b46563ee38828112483987b04742a662a688d90dca0d187ada63c0d85360def6

24 full common-time bars, five source systems, no repeats. The final score has308 note/rest elements (304 pitched,4 rests) in three justified musical voices. The frozen candidate had356 elements, including false lower-staff melody duplicates and displaced material. Corrections restore printed pitches/rhythms, chord membership, shared-head durations, stems, beams, tempo100, dynamics and26 slur/9 hairpin spans. The full audit includes every candidate event, all316 ensemble disagreements and354 provenance entries. Exact before/after measure XML and source review IDs are in applied_corrections.json.

Technical outcome: PASS for primary XML structural checks, ScoreAnalyzer, independent note schedule, installed production viewer mapping, VexFlow durations and every pitched onset cursor bucket. 304/304 playback entries map;183/183 cursor buckets pass. Final rendered score and source evidence are under render_checks/final and reviewer/evidence.

Human attention:
- Bars13–15: white masking interrupts interstaff curves; an additional swell cannot be confidently separated from the high lower phrase slur. The ambiguous source ink is preserved and explicitly unresolved, not asserted as a fabricated dynamic.
- Hairpins, especially full-bar endings4/20 and damaged5–8/17–18: confirm exact expressive endpoints against the supplied print. All chosen anchors are recorded in print_expected_marks.json.
- Bar16 when using SEP: actual CORE/MARKS Apply moves chord-specific slur attachments and loses opposing placement detail. The delivered XML retains the separate printed arcs. Use it as the authoritative import.

CORE, MARKS and ROUTE were freshly exported from this exact XML and tested with the real consumers. Note multisets and span times survive Apply; this is not a lossless engraving claim. CORE-only rebuilding omits expression/tempo, and MARKS cannot encode the metronome. ROUTE Apply passes without this loss. technical/TECHNICAL_SUMMARY.json and chord_slur_representation_exception.json separate these limitations from successful primary playback/cursor checks.

Observed account quota:90% to93% used in the weekly window (+3 percentage points,7% remaining). This is a coarse account-shared observation, not task-exclusive token usage. Historical source cost$0.08064675 belongs to preparation; no new source-model API calls were made.

Human outcome remains null. Listening, musical approval and publication remain yours.
