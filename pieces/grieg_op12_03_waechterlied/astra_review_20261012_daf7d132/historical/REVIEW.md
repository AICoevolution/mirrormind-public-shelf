# Independent review: technical delivery blocked

The complete print audit and supported corrections are finished. The UNVERIFIED primary retains 53 physical bars, 584 printed note/rest members and four continuous musical voices. Stage 5 remains blocked by production-renderer hairpin collisions; this is not ready for human delivery.

Juan’s unresolved musical question is **PEDAL-RELEASE** at P027, P031, P035 and P039. The printed release star follows the bass attack and precedes the upper entry; its exact rhythmic offset remains uncertain. Offset zero is provisional, not a confirmed correction. See [human_attention.json](human_attention.json). Human listening, visual verification and approval remain outstanding.

The exact primary is [delivery_final/UNVERIFIED_Grieg_Op12_03_Waechterlied_Astra_import.musicxml](delivery_final/UNVERIFIED_Grieg_Op12_03_Waechterlied_Astra_import.musicxml). PROPER passes with the printed quarter-note pickup. Independent playback matches all 518 attacks over 209 quarters. All 584 rendered members match the frozen pitch/rest, duration, onset and voice specification; all VexFlow ticks and 53 measure positions match. The installed production viewer maps all 518 attacks.

The focused visual check fails: below-staff hairpins collide with notation, particularly the A#3 notehead in P049 and A3+B3 chord in P052. Explicit vertical-offset trial XML produced an identical image. See [blocker evidence](validation/final/hairpin_placement_diagnostic.json). Production code was not changed.

CORE export is diagnostic only: rebuild and actual Apply are not lossless, and Apply changes the pickup to two quarters. MARKS and ROUTE actual Apply preserve the tested musical and member-level tie/slur projections. Layer readiness does not waive the primary rendering failure.

All 685 priority answers, 513 provenance records and 157 disagreements were reviewed before Phase3 release. The completed phase freezes remain unchanged. Corrections follow the frozen target specification and numbered ERRATUM_001; the change ledger retains every before/after bar. The erratum’s pedal sound encoding restores eight previously blank measures; its high rest-display positions match the print. See [PIPELINE_FINDINGS.md](PIPELINE_FINDINGS.md).
