# Stage 5 consumer recheck — BLOCKED

The shared cross_staff_phrase.v1 test passes all three layouts: all assigned spans are present, all curves pass shape and filled beam/notehead clearance, and all 31 cross-staff beam groups retain exact membership. Fresh production viewer mapping and duration/cursor checks also pass.

Visual inspection finds a remaining essential rendering defect: outgoing phrase segments cross melody stems at P007 (1000px, zoom 0.9) and P005 (900px, zoom 1) when the phrase crosses a system break. See [focused visual evidence](gates/focused_visual_recheck/report.json) and [blocker](recheck_blockers.json). The shared checker does not test stem intersections; its PASS does not certify visual readiness. Same-system opening-beam collisions from the previous review are resolved.

The exact primary XML and original Phase 1–3 evidence are preserved byte-for-byte. The original musical reviewer attribution remains unchanged. This review owns consumer rechecking only; no music or production code was changed. Previously passing PROPER, playback and layer gates are retained under the scoped consumer-only recheck contract.

Final human questions **PHRASE-ENDPOINTS**, **FINAL-PHRASE**, and **ARPEGGIO-TIES** remain unresolved in [human_attention.json](human_attention.json), with their original provisional treatments. They are distinct from the technical blocker. Delivery remains UNVERIFIED and technically blocked.
