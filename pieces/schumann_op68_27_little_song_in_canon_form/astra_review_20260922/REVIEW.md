# Corrected Astra delivery — UNVERIFIED

Primary file: `delivery_final/UNVERIFIED_Schumann_Op68_No27_Astra.musicxml`

SHA-256: `f0d0625b21aa700edfc2797b76644fb277d938cf004aec1200e4f30648288f9f`

Current review: `reviewer/revision_02/`. Earlier blocked files at reviewer root remain historical evidence; they do not describe this repaired run. Current authorization and all phase allowlist hashes matched. Three phase freezes precede correction application. The prepared run, candidate, handoff, authorization, queue and production code were not modified.

Reviewed all 48 printed regions in five systems, all 582 candidate note/rest objects and all 283 disagreement entries. Corrected delivery has 560 objects: 522 pitches and 38 printed rests, four continuous musical lines (five staff-specific SEP lanes), 31 tie pairs, 60 slurs, 90 beam groups, 16 accents, two arpeggiated chords, ten directions and ten hairpins. Meter remains 2/4; total physical capacity is 92 quarter units. There are no repeats, endings, navigation signs, tuplets, graces, pedal or ornaments. Fingerings alone are omitted.

Structural/duration and ScoreAnalyzer checks pass. Independent playback agrees within 1ms serialization rounding; all 491 playback events map in the installed production viewer. All 522 VexFlow pitched durations and 185 onset cursor checks pass. Focused visual recheck covers every changed bar and connected span.

**Delivery limitations:** CORE is exported for inspection but full rebuilding is not lossless. MARKS Apply retains musical anchors but loses explicit P41 wedge spread layout. ROUTE is ready. Primary XML retains the corrected data. The installed preview omits cross-staff slur geometry and mishandles cross-staff beam geometry; exact locations and screenshots are preserved. These are engraving limitations, not waived playback/cursor failures. See `delivery_final/layer_readiness.json` and `PIPELINE_FINDINGS.md`.

**Juan's focused attention:** P21–22 lower slur handoff; P44–46 long lower slur endpoint; horizontal text anchors at P20 cresc., P23 dim., and P47 pp. All uncertain interpretations retain human_outcome=null. Please also judge cross-staff engraving from the source/primary XML, since the installed preview is incomplete at those spans. Listening, visual/structural verification and publication remain yours; nothing was published.

`correction_history.json` gives every frozen correction and ERRATUM_002. `evidence/` contains hashed authorized inputs. `checks/` contains actual consumer results; failed earlier checks and disposable probes are evidence, never delivery alternatives. `render_checks/final01/` has the complete render and six focused contexts. `voice_topology.json` is included in the immutable artifact manifest. Final freeze and manifest hashes close this workspace.
