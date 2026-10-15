Primary technical gates pass on the final XML. No production code was changed.

MARKS v0 emits warnings for fz (P8/16/38/60) and ppp (P68), so its standalone layer readiness is BLOCKED even though actual Apply retains exact slur notehead endpoints, placement/orientation and articulation placement. See consumer/check.json and layer_readiness.json. This is a layer limitation, not a primary playback or display failure.

CORE’s header calls the20-pitch lower-staff melody intersection a likely artifact. The print confirms those20 pitches are part of voice1; removing the lane would delete music. The four exported intersections represent two continuous voices. CORE rebuild preserves all sounding events and actual Apply is byte-exact.

Below-staff cresc. words initially appeared inside the staff because the adapter anchors below the lowest notehead. ERRATUM_001 provides XML relative-y=-30 and italic styling atP25/P47. Final production images demonstrate the resolved placement. The original render is retained as superseded evidence.

The essential probe’s automatic collision scan covers only its built-in focused bars. It was supplemented by the full production render, all730 installed buildNoteMap mappings,72 OSMD durations/timestamps,162 VexFlow voice records and visual review of every changed context and connected span. Passing results are scoped to the captured1350px layout. Grace runs remain audible and sequential with no subsequent timing drift.

One-sharp key signature is preserved without inventing a printed mode. CORE labels its default Gmajor while ScoreAnalyzer infers Eminor. Likewise80bpm is an analyzer fallback, not printed tempo. Score interpretation remains subject to human verification.
