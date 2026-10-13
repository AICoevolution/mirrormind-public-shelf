# Schumann Op. 68 No. 24 — Astra review

Status: corrected primary delivery ready for Juan's verification; not published. Primary file: [UNVERIFIED MusicXML](delivery_final/UNVERIFIED_schumann_op68_24_harvest_song.musicxml). Exact SHA-256: `9b09ef0fe10f6aaf59ff6097613be23f1a80822dcb6d3fa8df3faf873b28f29c`.

The repaired frame was independently reviewed in three frozen phases: 2 pages, 5 systems, 28 physical regions. All 384 candidate note/rest elements were audited; the final score has 369 elements (263 rhythmic events), with 25 removals and 10 insertions. The review includes 512 detailed issue records, all 187 ensemble disagreements, the reader controls and all printed marks/routes. Source inputs, authorization, prepared candidate and production code were not modified. All 47 distinct allowlisted/launch files were rehashed and copied into inputs/prepared_snapshot for self-contained evidence.

Seven source lanes become four justified musical lanes: continuous melody and bass, plus the genuinely simultaneous upper melody P14-16/P19-20 and upper bass P19-20. There are no unexplained fragments, empty lanes or cross-staff duplicates. Printed 6/8 is unchanged; P1/P10 are half-quarter pickups and P9/P28 are 5/2-quarter closes.

Corrections are traceable through reviewer/phase3_review.json, application_history.json, ERRATUM_002.json and erratum_002_application.json. The focused recheck covers every physical region and all connected spans. Both rendered pages and SVGs are under rendered/.

PROPER, exact capacity checks, ScoreAnalyzer, an independent repeat/schedule comparison, installed production viewer mapping and VexFlow durations pass. The route has 56 played regions, 156 quarter-note units, and 644 sounding playback events. Every event maps to the correct printed region through both passes.

Layer readiness is deliberately separate. CORE has exactly four justified lanes and an unchanged Apply preserves the primary XML, but rebuilding it is not lossless: the grace before the P15 tie continuation is unsupported and the rebuild creates padding representations. MARKS exports without warnings and actual Apply preserves its statements and CORE; it rewrites mark XML and is not advertised as byte-lossless. ROUTE exports and applies correctly, preserving notes and MARKS statements. See delivery_final/layer_readiness.json and the actual gate reports.

Juan's musical attention: P25 last eighth/P26 entrance for **più lento**, and P26 last eighth/P27 entrance for **a tempo**. Exact anchoring remains medium confidence; no numerical slowing or fermata dwell was invented. Listening and visual/structural verification remain yours. The production render has local engraving quirks listed in reviewer/focused_recheck.json; the primary XML's musical data and span endpoints remain the reference.

Use FINAL_FREEZE.json and artifact_manifest.json to verify the immutable package. Human outcomes remain null.
