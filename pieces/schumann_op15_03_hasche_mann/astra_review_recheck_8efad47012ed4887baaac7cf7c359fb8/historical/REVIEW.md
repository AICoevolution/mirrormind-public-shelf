# Independent Astra review — technically blocked

All 21 physical regions and 336 original note/rest members were independently audited; 378 correction records are frozen. The corrected UNVERIFIED MusicXML is in delivery_final/. It is not ready for human delivery: the production renderer draws only one of the two required beams in ten cross-staff sixteenth groups and omits the P016 crescendo.

[Technical blockers](gates/technical_blockers.json) and [focused comparisons](gates/focused_visual_recheck.json) bind the exact XML. Production-code changes are outside this job. Preserve this workspace and use the Stage 5 consumer-recheck protocol after repair; do not change the primary XML or the phase freezes as part of a consumer repair.

The installed PROPER checker passes. The independent 32-bar, 406-attack playback schedule matches exactly, including member ties and source times. Production buildNoteMap maps all 406 attacks correctly; all 21 bar durations and all VexFlow note durations match. CORE rebuild preserves sounding semantics and actual Apply preserves the full projection and bytes. ROUTE roundtrip passes. MARKS Apply preserves exact member slur endpoints/styles and all eight sfp dynamics, but v0 export cannot express sfp: standalone MARKS is PARTIAL.

Final human musical attention remains unresolved: **HAIRPIN-P016** (precise crescendo start anchor) and **VOICE-P015** (shared notehead and overlapping printed rest representation). See [human_attention.json](human_attention.json) and its print evidence. These musical questions do not cause the technical stop, and no human answer has been inferred.

Corrections restore missing cross-staff notes, remove false doubled/sustained tones and unsupported rests, restore the P013–016 ties and chromatic run, and add all missing marks and beams. Four notated voices are provisionally retained with explicit P015 rest-based justification; at most three lines sound simultaneously. Fingering alone is omitted. The printed frame and repeat route remain unchanged.
