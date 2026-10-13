# Stage 5 recheck complete

All required primary delivery gates pass on the exact unchanged UNVERIFIED MusicXML. The production opening-clef defect is resolved: bass then treble appear before the lower-staff notes, those notes use treble positions, and the G3 tie into P002 is level.

**Final human attention remains:** UNISON-P007 and UNISON-P019 retain the existing single G4 provisionally. No duplicate note or extra voice was added and no human decision is inferred. See [human_attention.json](human_attention.json) and its frozen source images.

[Primary MusicXML](delivery_final/UNVERIFIED_Schumann_Op15_09_Ritter_vom_Steckenpferd_Astra_import.musicxml), SHA-256 `3df9d121d88541bda1678fe135b75a5d76ecc3be9076d477b08e7a84e3a85847`.

The original independent 24-bar, three-system print review and corrections remain attributed to astra_review_20261009_770422d0. This job owns only the Stage 5 recheck. All copied reviewer evidence is byte-identical; all 93 phase-input hashes and the current authorization match. No music, correction decision, topology, or production code was changed.

Fresh PROPER and ScoreAnalyzer checks pass. Independent repeat expansion and tie merging match all 560 playback notes over 48 visits (108 seconds at the default 80 bpm). Current production mapping locates every playback event; all VexFlow note ticks and source-measure timestamps match. Fresh CORE export has three justified lanes; actual CORE rebuild/Apply and MARKS Apply checks pass, including member ties and slur endpoints/placement/orientation.

ROUTE exact print roundtrip remains BLOCKED_EXACT_PRINT_ROUNDTRIP: Apply adds a forward repeat at P001 where the print uses an implicit beginning. This isolated layer test is not the primary delivery. The unchanged primary route and playback pass.

[Focused visual recheck](validation/focused_visual_recheck.json) covers all 24 bars, connected ties/slurs, accidentals, accents, dynamics, rests and repeats against frozen source crops. [Fresh production render](validation/production_render/full_score.png) and [consumer hashes](validation/production_render/consumer_hashes.json) bind the evidence. The long duplicated title clips in this fixed-width diagnostic screenshot; musical staves remain visible. This cosmetic export issue does not alter the musical gates.

Historical blocked reports are retained under historical/. The final freeze and supervisor manifest bind the new reports. Human listening, musical verification and publication remain pending; REVIEW_COMPLETE is not musical approval.
