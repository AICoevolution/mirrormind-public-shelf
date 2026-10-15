# UNVERIFIED delivery — Vaterländisches Lied

The independent 32-bar print review and supported corrections are complete. Import [the primary MusicXML](delivery_final/UNVERIFIED_Grieg_Op12_08_Vaterlaendisches_Lied_Astra_import.musicxml). [Rendered score](delivery_final/rendered_score.png) and [printed source](delivery_final/printed_source.pdf) are included. Human listening, visual verification and publication remain outstanding.

## Final human attention
Two unresolved questions remain in [human_attention.json](human_attention.json):
- **HA-WEDGES:** P011–012/P023–024 wedge endpoint timing. Provisionally ends at onset 3; ink extends toward the final beat.
- **HA-STACCATO:** P014/P018/P026/P030 final dot. Attached to the printed upstem chord; whether bass should share its performance articulation remains for verification.
No human answer or signature has been inferred.

## Changes
Corrected P001 extra C5, P003 dotted rhythms, P007 A-natural, missing/incorrect lower chord members in P015/P019/P027/P031, and P032 terminal whole chord. Restored all directions, dynamics, articulations, six slurs and printed beams. Removed unprinted padding rests. Traced two continuing outer voices across staves and retained the independent inner voice only in P010/P022; opening opposing-stem unisons remain two voices. Exact before/after records are in [correction_ledger.json](correction_ledger.json), with [frozen Phase 3 specifications](reviewer/phase3_target_spec.json). Two frozen engraving errata position hand words clear of staff and accent ink.

## Validation
The exact final XML passes PROPER, the independent 348-event playback schedule and linear route, all 352 note/rest member staff/timing checks, all VexFlow durations, and all 348 production cursor mappings at 1400px/1 and 1000px/0.9 layouts. [Production report](validation/final_v2/production/report.json) and [focused visual recheck](validation/final_v2/focused_visual_recheck.json) bind the final hash. Rendered directions, rest lanes, connected chords, beams and every slur span inspected.

[Layer readiness](validation/final_v2/layer_readiness.json): CORE musical rebuild is exact and actual Apply is byte-exact. MARKS Apply preserves exact slur-member endpoints/placement/orientation and articulation placement; ROUTE Apply preserves events. CORE alone changes staff packaging and omits MARKS, so its rebuilt XML is not the primary delivery. The primary XML remains authoritative.

[Phase 1](reviewer/PHASE1_FREEZE.md), [Phase 2](reviewer/PHASE2_FREEZE.md), and [Phase 3](reviewer/PHASE3_FREEZE.md) remain frozen. The controller released later context only after the completed Phase 3 freeze and hash validation. Full historical source-freeze closure subsequently validated. No source candidate or production code was modified.
