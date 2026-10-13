CORE rebuild is not lossless for this score. P012 D4 and P016 A4 sustained dotted quarters become halves, and the terminal P017 C4 grace disappears. The stored XML and unchanged actual Apply preserve them; a byte-exact no-op does not certify edited reconstruction. Evidence: validation/layer_readiness.json and validation/CORE_rebuilt.musicxml.

MARKS Apply preserves exported text but relocates two grace-slur stops from the intended lower sustained member to a different note and changes their side. Exact endpoint/style comparison catches this. Evidence: validation/MARKS_applied.musicxml and validation/layer_readiness.json.

The serializer presents seven staff lanes for five musical voices. The cross-staff voices are not seven independent lines; voice_topology.json records the distinction. No unsafe global source-label merge was applied.

OSMD gives P017’s terminal grace a half-quarter layout slot. The installed production mapping removes that specific drift, and every later cursor bar address was checked against an independent physical timeline. VexFlow sounding note durations match. This narrow layout behavior is not a primary playback exception.

The plain essential-notation probe alone does not exercise all production adapters. The final probe applies the installed volta, cross-staff slur, cross-staff beam and essential-notation adapters in ScoreViewer order, and executes the extracted installed buildNoteMap. Its console exit and raw status are supplemented by exact schedule/bar checks and beam-member geometry.

Initial visual checks exposed shared-rest duplication and wrong default tie sides. Frozen ERRATUM_004 and ERRATUM_006 correct the XML representation; the final evidence was regenerated afterward. Original candidate and frozen staged evidence remain unchanged.
