# Stage 5 recheck complete — UNVERIFIED delivery

The consumer pedal-line repair passes independent runtime checks and visual inspection in four layouts. The exact [primary MusicXML](delivery_final/UNVERIFIED_Mendelssohn_Venetian_Boat_Song_No1.musicxml) is unchanged: SHA-256 `c5b5e1ac8fc2254864ab59a542350fd7349257bad90ba37586af63b98b608a57`. The completed musical audit belongs to the prior review `astra_review_20261015_7b779b3b04c5`; this job owns the Stage 5 recheck only. All protected prior files and copied reviewer evidence were verified unchanged.

Final human questions remain unresolved in [human_attention.json](human_attention.json):

- **P022-OVERLAP**: dotted E-flat5 overlap with the final A4/F-sharp4 inner chord remains provisional.
- **P031-CURVE**: curve into P032 remains provisionally a slur.
- **P044-046-CURVES**: repeated D4 connections remain provisionally ties.
- **PEDAL-ENDPOINTS**: exact P010/P032/P033 print alignment remains provisional.

No human answer or approval is inferred. Prior review covered 46 bars, 10 printed systems and 744 candidate event members; delivery retains 736 note/rest members and 603 playback attacks. The correction ledger, two errata and three-line voice topology remain unchanged.

PROPER, exact playback, note/member/cursor mapping, essential notation rendering and focused visual recheck pass. [Current combined report](recheck/full_render/report.json) checks 62 pedal marks, 95 segments, all note/rest members, 118 ordinary beams, 446 stems, and hairpins in four layouts. The four screenshots in `recheck/full_render/` were visually inspected (byte-identical to the separately generated scoped acceptance screenshots). Missing-mark, missing-segment, flattened-change and wrong-time negative tests all detect failures. The sign-pedal interpolation regression also passes.

[Layer checks](layer_roundtrip_report.json) retain separate limitations: CORE Apply passes; CORE rebuild fails on a tie from silence, and MARKS Apply fails on unmatched wedge spans. MARKS v0 also omits pedal changes. These layers are not lossless replacements for the primary XML. Narrow layouts clip the long title, without omitting score notation.

Current evidence is under `recheck/`, with current root technical reports and [visual observations](focused_visual_recheck.json). Copied viewer_validation directories and reviewer/stage5_blockers.json are historical evidence of the prior failure, not current gate results. No source, frozen phases, production code or primary XML was changed. Publication remains a human action.
