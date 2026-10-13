# Astra review — technically blocked

The independent print review and supported corrections are complete. Delivery is **not ready**: the production viewer delays the lower-staff treble clef in P001 until the end of that bar. Notes that must be shown under treble are engraved under bass, and the P001–P002 G3 tie slopes between incorrect positions. This is a consumer defect, not an unresolved printed-music question. No production code or source candidate was modified.

## Human attention, retained for final verification
- **UNISON-P007** and **UNISON-P019**: final upper-chord G4 appears as adjacent unison-looking heads. The candidate's single G4 is retained provisionally. See [human_attention.json](human_attention.json) and its print evidence. No human answer is inferred.

## Corrected primary
[UNVERIFIED MusicXML](delivery_final/UNVERIFIED_Schumann_Op15_09_Ritter_vom_Steckenpferd_Astra_import.musicxml), SHA-256 `3df9d121d88541bda1678fe135b75a5d76ecc3be9076d477b08e7a84e3a85847`.

All 24 bars and three source systems were reviewed. Source had 327 note/rest members; final has 323. Corrections remove an erroneous three-sharp key signature, repair local pitches/accidentals, restore the missing P010 eighth-note C5, restore all 10 ties, four slurs, 24 accents and two dynamics, remove five unprinted rests, and consolidate six labels to three continuous musical lines. Exact before/after records are in correction_ledger.json; the print-grounded specification is frozen in reviewer/phase3_target_events.json and phase3_review.json. Voice topology is bound in voice_topology.json.

## Validation
- PROPER passes: no overfull/short bars or cursor slips.
- ScoreAnalyzer passes independent playback comparison: 560 notes, exact pitch/voice/onset/duration/source onset; 48 bar visits, 108 seconds at the analyzer's default 80 bpm. No tempo is printed.
- Actual production mapping locates all 560 playback notes in the correct printed bars. VexFlow duration ticks match source lengths and the notation timeline spans 24 complete 3/4 bars.
- CORE export has exactly three justified lanes; rebuild and real Apply preserve pitched events and member ties. MARKS real Apply preserves exact member endpoints, placement and orientation.
- ROUTE real Apply introduces an explicit forward repeat at P001. The primary retains the correct implicit beginning. Exact printed ROUTE round-trip is blocked; its output is only a test artifact.
- Essential notation and focused visual recheck are blocked by P001's misplaced clef. The generic adapter probe reports passed but does not test this clef, so that exit/status is not promoted to readiness.

[Production render](validation/production_render/full_score.png), [source opening](reviewer/p1.png), [technical blocker](validation/technical_blockers.json), [focused recheck](validation/focused_visual_recheck.json), [playback](validation/primary_playback.json), [layer tests](validation/layer_roundtrip.json).

Consumer repair must preserve the printed opening bass glyph and the following treble glyph, while making treble effective before the first P001 notes. Recheck in a NEW workspace, preserving this primary XML and all Phase 1–3 hashes. Frozen evidence is not to be overwritten. Ordinary unison uncertainty remains for final human verification; it is not the reason for this technical stop.
