# PHASE 3 — FROZEN

Frozen UTC: 2026-09-22T08:19:33.330511+00:00

All 48 physical regions in five systems were checked against their actual printed locations. Direct transcription contains 560 note/rest objects (522 pitched), 31 tie pairs, 90 beam groups, 60 slurs, 16 accents, two arpeggiated chords, ten directions, ten wedges. Fingerings alone are excluded. No printed grace notes or tuplets. Printed meter remains 2/4; partial capacities are P1/P30=1/2 and P29/P48=3/2. Route is P1–P48 once, with double bar after29 and final bar48; no repeats/endings/navigation.

The 582 candidate objects are individually crosswalked in phase3_event_coverage.json, including unchanged claims. All 555 provenance records and all 283 disagreement entries (resolved and unresolved) have a per-entry recheck. The candidate packets cover every XML ID and agree on pitch/onset/duration. Ledger discrepancies: 41. Source selection/candidate mismatches: 0. Models are evidence about selection, never musical authority. Referenced raw model sources outside the allowlist were not opened.

Correction inventory: {'other': 396, 'extra_event': 34, 'pitch_error': 43, 'duration_error': 15, 'missing_event': 12, 'mark_error': 102, 'route_error': 2, 'provenance_error': 43}. phase3_review.json gives exact before/after fields, IDs, staff, bar, system and evidence. print_transcription.json and print_marks.json are the frozen complete target, including beam, tie, chord, voice and accidental decisions. These are reviewer readings, not a pitch vote. The source's zero duration discrepancies and PROPER result did not prevent wrong notes, phantom rests, broken ties, missing bass notes, wrong durations, or missing expression. No padding or trimming is approved.

Voice topology: four independent continuous lines, with a staff1 and staff2 segment for line3. Source5 restarts line1 and source6 restarts line2; neither is an extra line. Context-scoped source-role changes are recorded before application. Bass notes in P4/P5/P13/P34 cannot be globally merged by OMR label. Explicit gaps are unnotated time, not fabricated printed rests. Shared unison pitches in independent rhythms (notably P24/P28/P29/P42) remain independent.

MARKS refinements of Phase1: P7/P9/P15/P36 accents attach to lower E4; earlier approximate inner-staff addresses are replaced by these exact anchors. P30 D4→P31 C4 is a slur, not a tie. Three medium-confidence concerns remain in print_marks.json: P21–22 cross-staff slur start, P44–46 long slur end, expressive text anchoring P20/P23/P47. They are retained as uncertainty, not structural facts. Both ends of every listed span were read in the complete system images; connected cross-system spans were checked in both systems.

All phase3_allowlist hashes match. Earlier phase freezes remain untouched. Stage5 may now copy the candidate and apply this frozen correction plan. Human outcome remains null. This freeze is not Juan's publication verification.
