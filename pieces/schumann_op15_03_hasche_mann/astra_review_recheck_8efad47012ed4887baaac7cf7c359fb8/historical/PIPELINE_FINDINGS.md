# Pipeline findings
The source passes duration arithmetic while carrying wrong pitches, duplicated tones, missing cross-staff events and no expressive marks. Reader majority and fused confidence do not establish print truth. Phase1 control-1 explanatory rhythm was wrong while numeric capacity was right; preserved as a partial control failure.

Current production crossStaffBeamRendering.ts draws one polygon per cross-staff group regardless of the two MusicXML beam levels. Ten groups are affected; all four members attach to the primary beam, so checking mere beam existence/member continuity would miss this error. The P016 offset crescendo is encoded but absent visually. Repair consumers outside this bounded review job, then rerun all readiness gates against the unchanged frozen primary XML.

MARKS v0 has no sfp token; export warns for all eight occurrences. Actual MARKS Apply preserves sfp in existing XML, but a standalone reconstruction is not lossless. This layer limitation is separate from primary playback and rendering gates.
