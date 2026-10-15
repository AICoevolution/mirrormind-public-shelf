# Consumer and source findings

The exact final primary passes all required delivery gates. No production or supervisor code was changed.

- CORE rebuild preserves pitch, onset, duration, grace and member ties. Actual CORE Apply fails exact event and musical projections: the P001 upper B4 pickup moves from onset0 to0.5q and gains a preceding rest. Chord ordering also changes. The applied XML is not a delivery artifact. Evidence: consumer_checks.json, layer_difference_evidence.json, core_applied.musicxml and core_rebuilt.musicxml.
- MARKS export warns about the repeated pedal start at P009. Apply does not preserve the MARKS text fixpoint or every exact slur member endpoint/placement/orientation. Event projection and articulation placement do remain equal. This layer has BLOCKED readiness; use primary XML for import. Evidence: consumer_checks.json, layer_difference_evidence.json and marks_applied.musicxml.
- ROUTE is straight1–57 and passes. No repeat, ending, cadenza, cross-staff beam or tuplet exception is required.
- Initial production rendering crowded rests, omitted the unsupported pedal-change symbol and placed fz on a high bass note. Frozen errata use explicit printed rest lanes, hidden silence carriers, repeated printed pedal start and an interstaff fz attachment. Final rendering has no detected rest collisions, 21 graces, seven pedal symbols, exact durations and 533 visible mapped attacks. Direct visual inspection confirms the final courtesy naturals and stems as well.
- The phase2 pickup control claimed a quarter where the print is an eighth. Its failure is preserved; it never authorized a frame change. Historical SmartScore P008 attribution and Audiveris duplicated label are documented in the frozen audit. Readers and provenance were evidence, not authorities.

The primary playback check certifies the attack schedule, tie merges and grace realization, not sustain-pedal interpretation or human expression. GRACE-ARCS and PEDAL-OPEN remain final human questions.

ERRATUM_002_REFERENCE_ADDENDUM.json corrects two missing underscores in the frozen erratum’s evidence filenames without rewriting it.
