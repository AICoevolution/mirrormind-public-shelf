# Consumer findings

1. Generated sound-only damper-pedal attributes made OSMD omit entire measures. Removed only these synthesized attributes; retained all frozen pedal directions. Initial failing evidence remains in application_initial and render_initial.
2. Reusing a slur number within one measure across independently serialized voices produced erroneous long spans. Delaying reuse until a later measure fixed those associations without changing any printed endpoint.
3. The P026/P027 same-staff, cross-voice slur still crosses the upper staff. This is a blocking ownership defect requiring a production-consumer repair; see consumer_blockers.json.
4. CORE Apply rejects P006 anchor preservation. CORE rebuild/Apply and MARKS/ROUTE results are separately retained in validation_final/layers.json. Do not simplify authoritative notation to force a layer pass.
5. The shared geometric member/cursor report passes even with the slur-shape defect. Independent visual inspection remains mandatory.


## Current consumer recheck
The P026–P027 lower-staff ownership blocker is resolved in all three fresh production layouts. Historical failures above remain historical. Shared geometry and negative controls pass; final readable presentation findings are in human_attention.json. CORE Apply remains a reported representation limitation, never a replacement for the primary XML.
