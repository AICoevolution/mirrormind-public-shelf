# Phase 2 freeze - reader evidence reviewed

Status: COMPLETE_WITH_EXPLICIT_PRINT_UNCERTAINTIES. No candidate, ensemble, model adjudication, provenance, or Phase 3 packet has been opened before this freeze.

The current human authorization binds handoff acc9fed8a397e06669c0cbd25655e4c03edce45e1e19a6d3463a94d4a1bd1215. All 65 Phase 2 allowlisted hashes pass again at freeze. The unchanged Phase 1 is carried forward under RESUME_BINDING.json. Historical blocked workspaces remain untouched.

## Coverage and evidence

- Direct print pitch/rhythm comparison: all 194 physical bars, four canonical staves, 39 systems, eight pages; 4,643 explicit note/rest/grace/member observations in phase2_print_core.json. Phase 2 does not certify inherited OMR voice labels, beams, written-type metadata or final rendering.
- All three readers: 582 reader-region comparisons. Raw XML note/rest element counts match normalized source mappings in every region (582/582). Audiveris contextual parts P1-P4 correctly supply bars88-91; outside that context P5-P7 supply the three canonical parts. SmartScore ordinal108 duplicates P107, and ordinal109 resumes P108. Audiveris raw labels diverge after ordinal164; physical ordinals remain stable.
- All 3,197 supplied priorities answered by exact ID in phase2_priority_answers.json: 3,107 pitch/onset questions, 64 frame questions, 21 printed sequence/offset questions, and five tie questions. Native-label alternatives are preserved where they differ from physical addresses. Reader majority did not determine any answer.
- Three deterministic root controls independently assessed; all 23 failed controls retained and linked to answers. Counts/frame validation are not musical certificates.
- MARKS: 777 explicit note-mark records (467 slurs, 83 member ties, 190 staccato attacks, 32 trills, five turns), plus 37 directions. Compared all extracted note marks, including orphan slurs and raw XML extras; 2,196 note-mark comparison entries and 159 direction/route claim reviews. Slur/member and direction-placement details remain mandatory in the candidate and production-render audits.
- ROUTE: backward repeat after P078, forward repeat before P079, backward repeat after P194. Playback regions 1-78,1-78,79-194,79-194. No printed endings, segno/coda, octave lines, pedal or hairpins. Reader claims for these are rejected; SmartScore omits the first backward repeat.

## Corrections to the initial narrative inventory

The original Phase 1 files remain unchanged. Numbered PRINT_INVENTORY_ERRATUM_1/2/3 artifacts bind the more precise note-level findings: three-note grace groups, different-pitch slurs misnamed ties, omitted violin legato at P026, and focused arc/dot endpoints. The structured Phase 2 print observations supersede imprecise narrative descriptions at those locations. Focused source-derived PNGs are retained in phase2_evidence/.

## Remaining print uncertainty

1. P033 piano upper: tiny opening arc's second endpoint is unclear.
2. P047 violin: long lower arc begins near q2 A4/q2.5 F#4; working choice F#4 is medium confidence.
3. P065 piano lower q3: small glyph above the middle bass octave is damaged/ambiguous.
4. P102 piano upper: ascending arc begins near q2 Ab4/q2.25 Bb4; working choice q2 is medium confidence.
5. P193 cello q3: speck after F#4 quarter is not silently promoted to a duration dot.

These are explicit musical/print uncertainties, not permission to omit review or alter capacity. Phase 3 must inspect every candidate event and mark, test the printed answers again, resolve or preserve these locations, and freeze exact corrections. No technical delivery or accuracy approval is claimed here.
