# Pipeline findings

- Prepared PROPER/duration count0 did not certify musical accuracy. Clef-glyph false pitches and gross upper-register/rhythm errors survived structural fusion.
- Reader correspondence maps were empty. Candidate packets consequently had empty reader arrays and comparison listed all candidate events as candidate_only; no unanimous comparison can be inferred from that output. Reviewer reconstructed all34 correspondences using source geometry and local sequences.
- Two of three parent controls were false. Opening A4 sixteenth passed;17 half-note and34 A5-sharp quarter failed.
- All300 pitch provenance entries trace to candidate ledger pitches, but225 ledger records differ from assembled candidate packet voice/explicit-accidental fields. Exact ledger name is misleading for these fields. Final ledgers regenerated from exact final XML.
- Candidate MARKS was entirely empty. Source fusion cannot replace independent marks/route review.
- music21 flattens monophonic lower measures and loses raw voice3, splitting the exported bass into an extra v1 lane. Exact label-only s2v3->1 removes the fragment. Standard remap_voices rebuilds measures and normalizes stems, unsafe here for opposed stems and mid-bar clefs; it was not used. An attempted Map command through the CORE Apply API refused before any write.
- End-of-partial9 bass clef was deferred into11 by installed rendering. Equivalent start10 boundary encoding restored display at end9 without changing absolute onset or pitch.
- Installed OSMD/VexFlow fails to draw cross-staff beam/slur spans8->9,21->22,33->34. Their pitches, local timestamps, VexFlow durations and cursor buckets pass. This narrowly disclosed representation issue is not used to waive primary timing checks.
- CORE rebuild is not event-preserving; CORE/MARKS actual Apply refuses precise voice addresses. ROUTE actual Apply preserves the checked fields. Five-lane CORE is useful evidence, not a lossless replacement for primary XML.
- Analyzer playback uses quarter80 despite printed eighth88; rit/a tempo semantics are encoded but human expressive listening remains necessary.

No production code fixes, orchestrator communication, queue updates or publication performed.
