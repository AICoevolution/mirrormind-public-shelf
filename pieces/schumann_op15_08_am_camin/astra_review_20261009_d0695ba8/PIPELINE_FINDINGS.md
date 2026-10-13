# Pipeline findings

The candidate passed duration arithmetic while retaining duplicated lower voices, wrong pitches, wrong dotted rhythms and no expressive marks. Physical correspondence is intact; controls 1, 4 and 5 incorrectly passed pickup/clef claims. See reviewer/controls_assessment.json.

The five final musical lanes are justified in voice_topology.json. A global source-label merge would mix different musical roles; corrections were scoped to actual bar/voice contexts.

Primary XML passes duration, independent playback, viewer mapping, VexFlow duration/cursor and focused rendering checks. It remains UNVERIFIED for musical attention items.

CORE is a reference export, not a lossless standalone rebuild. Actual CORE Apply is byte-exact, but rebuild shifts the pickup and extends unprinted voice endings at P011/P015/P026/P030. MARKS is a reference export: actual Apply preserves sounding events and member attachments but drops orientation=over on the three alternate-ending slur endpoints P022/P025/P026. Text fixpoints do not prove fidelity. Exact differences are preserved in validation_sealed/layer_readiness.json. ROUTE export/Apply passes and independent playback confirms the 49-region route. These layer limitations are not waived or promoted to a primary pass. Do not replace the primary XML with reconstructed layers.

Production rest defaults placed an upper bass-staff line below the bass. Explicit rest positions and text displacement resolve the primary rendering without changing consumer code. Three numbered engraving errata preserve before/after evidence. No supervisor, control, authorization, policy or production code was changed.
