# Current technical findings

CORE pitch-only payload preservation is independently verified. The prior CORE blocker is resolved. No production code was modified by this reviewer.

Production beam geometry remains unsafe at P078: all members connect but one head is intersected and earlier stems reverse their encoded direction. This illustrates why membership and cursor counts alone cannot certify notation rendering. See current_validation/stage5_blockers.json for the bounded consumer repair.

Historical reproduction marks_preservation_failure.json retains its unconditional BLOCKED label; marks_current_verdict.json evaluates the actual empty differences without rewriting that raw report. Standalone CORE reexport and MARKS projection warnings are retained honestly. Historical freezes and release request are preserved byte-for-byte.
