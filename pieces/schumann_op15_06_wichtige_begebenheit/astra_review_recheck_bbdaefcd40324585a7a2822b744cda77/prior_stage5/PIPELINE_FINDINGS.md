# Pipeline findings

1. The installed renderer's dense polyphonic spacing shifts sequential inner eighths into overlapping noteheads at P007. Numerically ordered voices improve bass beaming but do not solve all collisions. See phase5_blockers.json and final screenshot; passing glyph counts and duration checks cannot certify visual accuracy.
2. Empty-upper-staff hairpins rendered at incorrect horizontal positions with staff1/below. Equivalent staff2/above carriers, frozen in erratum2, now locate them correctly.
3. The ensemble loses every expressive mark and beam, adds spurious upper-staff events, retains fragmented voices and phantom rests, and fuses incorrect chords despite PROPER. See all 27 complete bar specifications.
4. Current authorized reader evidence differs from the historical ensemble manifest's reader-claims hash. This was preserved as PROV-1 and not used as musical authority.
5. Frozen Phase1 inventory had an incorrect P007 crescendo reading, and the review's Phase2 transcription had A1+A2 instead of printed A1+E2 at P009/P027. Subsequent print-supported findings/errata correct these without rewriting historical evidence.
6. Standalone CORE rebuild preserves sounding projection but adds absent-lane rests and fails PROPER. Actual Apply is byte-identical; do not equate the two operations or promote layer status into primary readiness.
