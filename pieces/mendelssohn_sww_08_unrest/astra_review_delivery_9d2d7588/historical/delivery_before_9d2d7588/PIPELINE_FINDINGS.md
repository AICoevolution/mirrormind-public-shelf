# Technical findings

1. Missing mandatory attention_policy module prevents canonical index build/validation. No supervisor code was changed.
2. The bundled schema path was missing; official W3C v4.0 schemas were downloaded into review evidence. This exposed out-of-range dashes/wedge identifiers. A serialization-only renumbering fixed them; old XML/reports remain in historical/delivery_encoding_v2 and validation_encoding_v2. Final schema PASS.
3. The legacy consumer helper core_edit omits Pickup and therefore corrupts this no-op edit fixture. Including the accepted Pickup directive gives byte-identical Apply.
4. MARKS Apply changes 287 note payload trees only by child ordering, empty notations and slur number normalization. Endpoint styles and musical projection pass; retain primary authority.
5. Sparse staff-lane CORE warnings reflect two real cross-staff lines, not extra musical voices. Six staff-lanes represent four musical lines.
6. Shared viewer checker fails only P040 dim. lane geometry. Exact identity/mapping and negative controls pass; bound human presentation issue retains the raw BLOCKED report. Local guide/fingering and word/dashes issues are human publication questions.
7. Candidate metadata is empty; current renderer says Untitled Score. Reviewed namecard is supplied for pipeline metadata-only export. No invented composer/instrument credit.
8. A supplemental screenshot attempt used viewport clipping outside the viewport; its raw failure is preserved in validation_encoding_v2/full_render. The corrected full-page capture helper completed both layouts.
