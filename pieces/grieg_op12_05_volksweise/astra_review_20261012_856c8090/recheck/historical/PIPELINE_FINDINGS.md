# Pipeline findings

1. Candidate structural success masked missing melody in P020/P036, false pitches/accompaniment in P004/P019/P032/P037, lost ornaments, fragmented voice labels and a completely empty marks layer. Do not promote arithmetic success to musical accuracy.
2. Regional provenance summary index 0 is valid without an event_id. Retained and audited as a regional cross-staff claim. Some ledger/CORE pitch discrepancies (P022/P038) make live XML/member checking essential.
3. Frame and control prose reverses quarter/half order at P041 and invents a fermata. Capacity 3 remains correct; no frame repair needed.
4. essentialNotationRendering removes pedal direction-type children but retains redundant sound-only carriers; this caused OSMD to drop every affected measure. A valid encoding without redundant carriers avoids that issue (erratum 001).
5. **Blocking:** pedalPlacement falls back to a preceding lower-staff attack for release stars whose time has no new attack in that staff. Thus 11 start/stop overlap pairs occur across nine regions. Bound DOM rectangles and screenshots prove the failure. A renderer repair must interpolate the encoded onset, retain lower-staff vertical placement, and handle both sustained notes and accompaniment that changes staff. Do not insert unprinted notes/rests or move pedal events to another staff as a workaround.
6. The generic essential-notation probe says passed even when measures are blank or pedal glyphs collide. Full source-duration, viewer-map and focused geometry checks are necessary. Broad production checks caught both problems here.

No publishing or production code changes were performed. Frozen inputs and Phase 1–3 artifacts remain unchanged.
