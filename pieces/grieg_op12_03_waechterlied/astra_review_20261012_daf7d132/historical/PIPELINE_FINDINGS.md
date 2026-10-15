# Consumer findings

1. **Unresolved: hairpin placement.** Below-staff wedges collide with noteheads, stems, beams and ties. P049 and P052 provide unambiguous examples against print. `default-y=-100` plus `relative-y=-40` on diagnostic wedge endpoints has no rendered effect. Repair the production consumer and recheck all hairpin contexts; primary musical content must remain frozen.
2. **CORE application is not lossless.** Actual Apply expands the printed one-quarter pickup to two quarters. Rebuild and Apply fail member-level projection, including voice/tie comparisons. The layer is blocked independently of primary MusicXML readiness; no claim of losslessness is made.
3. **Resolved in primary encoding: missing bars after pedal preprocessing.** The essential-notation preprocessor removed pedal markup but retained a sound-only direction; OSMD then produced zero-duration blank bars at26,27,30,31,34,35,38,39. Moving the same pedal sound to a standalone measure child restores53 bars and518 mappings without changing music. Original failing renders and ERRATUM_001 are retained.
4. **Rest placement corrected.** Explicit display-step A/display-octave3 restores high moving-voice rests at26,30,34,38. All member tick durations pass, including triplets and septuplets.
5. **Playback precision.** Initial four-decimal expected comparisons differed from analyzer millisecond rounding. Comparison at the actual consumer precision passes all518 attacks; the failed diagnostic is retained, not used as a readiness gate.

No production code, source candidate, authorization or frozen phase evidence was modified. The renderer’s generic process success flag is insufficient: both missing bars in the first render and remaining hairpin collisions require direct graph and visual checks.
