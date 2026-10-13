# PHASE 3 FREEZE

Candidate SHA-256 eed8f541a9a53b8ac99ac718e381e0a29c1c09a5fbbb1cd42173d6cdb04bc0de. Handoff 5870554da56a525d94384249f667bd98682dd140b40e0d2b73ccb093673b4c73. Phase 2 was frozen before Phase 3 access. All current allowlist hashes match. Candidate packet freeze and allowlisted source-freeze dependencies match. References outside the allowlist were not opened, even when named by a manifest. Direct model source packets and raw API response were not accessed.

## Complete coverage and frozen corrections

All 564 XML note/rest elements, including chord members, were reviewed against the seven printed systems on both pages. Every physical region is covered in phase3_event_coverage.json. Exact before/after changes, IDs, physical addresses, evidence, provenance/disagreement identifiers, confidence and null human outcomes are in phase3_review.json. The machine-readable intended score is phase3_proposed_score.json. This is a proposal, not an applied delivery. All 118 ensemble disagreements, including the 13 unresolved entries, are individually rechecked in phase3_disagreement_recheck.json. Unanimous and unflagged events were included equally.

The source has 557 pitched elements and seven rests. Proposal removes three unprinted rests and four unprinted pitches, leaving 557 total elements (553 pitched plus four printed rests). The P008 shared-head bass and moving-line entries are preserved because their printed stems and durations are independently meaningful. No grace notes or tuplets are printed or introduced.

Principal CORE corrections: F-double-sharp4 must have alter=2 in P004 and P028 (not merely a glyph); P019 opening E4/E5 must last a dotted quarter, so remove the false eighth rest; replace P019 closing G2/G3 with E4/E5; P022 opening D2/D3 becomes C4/C5 with C5 joined to upper A4 and C4 completing the independent inner line; remove P022 extra A5 and phantom rest; remove P032 unprinted A4/C5/G4 half-note chord. Restore printed stem directions and every beam level/hook directly from the print. P010 already has the correct dotted-sixteenth/thirty-second rhythm and is retained unchanged.

Accidental glyphs are independently rebuilt at exact noteheads. This removes propagated/misattached sharps/naturals at P023/P030/P033 and redundant repeated glyphs, restores printed naturals at lower B3/C4 in P006/P007/P030/P031, lower G3 in P020 and B-natural in P022 both staves, and preserves high C-natural6 in P031. Glyph and sounding alteration are treated as separate fields.

MARKS: candidate has no expressive marks. Restore all tempo/dynamic/text/articulation/slur/tie inventory entries with exact onsets and endpoints specified in the proposal. Both ends of the P004–P005 chord ties, P018–P020 phrases and P020–P022 cross-system phrases are included. All three chord ties P002→P003 and P004→P005 require sounding tie and visible tied elements. No invented hairpins, pedal, ornament, fermata, tuplets, or fingering marks. ROUTE remains the three correct repeat boundaries; playback sequence is P001–P009 twice, then P010–P033 twice.

## Minimal topology frozen before application

Three musical lines, four (staff,voice) lanes:

- Voice 1: continuous upper melody, including unified upper chords; source s1v5 resumes s1v1 in P018–20. P018 opening chord belongs to this line rather than an unrelated restart.
- Voice 2: continuous lower bass/accompaniment; in P008 it retains the quarter-note bass under the separately beamed inner line.
- Voice 3: intermittent independent inner accompaniment. It occupies staff 2 in P008, then staff 1 in P018–P022. It is not a fourth musical voice merely because it changes staff. P022 C5 rejoins the melodic chord and C4 finishes the inner phrase at onset 0 with an eighth.

Source labels change role locally: global s1v6→1 would overlap the real melody and is prohibited. Global s2v3→2 is also insufficient at P008. Use explicit note-ID/context relabels from the proposal. No source label 4/5/6 remains as an unexplained fragment. No all-rest lane remains. Four printed lower rests in P024/P025 belong to the continuing accompaniment. No padded rests may be added to complete short inner-line occupancy.

## Provenance and diagnostics

The packet event stream matches exact XML onsets for all 564 elements. The event ledger disagrees with XML for all three P032 extra-chord members: ledger onset 3/2, XML onset 0. phase3_ledger_xml_comparison.json preserves the discrepancy. Other selected-source/provenance disagreements are explicitly included in phase3_review.json. Pitch provenance is not complete field provenance: it does not justify beams, accidentals, marks, or topology. exact_mark_ledger.json contains only the three repeat barlines and therefore is not a complete printed MARKS inventory. candidate comparison labels events candidate-only because source correspondence arrays were empty, not because the notes lacked reader evidence.

The zero duration-discrepancy report misses the wrong P019 dotted-quarter/rest interpretation. The passing structural report is not a print certificate. Its suggested voice merges could conflate simultaneously sounding lines. Source CORE warns it cannot Apply P003 ties, and exposes seven lanes due to staff/voice rebucketing; neither warning is waived.

No damaged-print ambiguity presently prevents these frozen corrections. Retain Juan verification at P008 shared noteheads, P018–P022 inner-line/phrase connections, and P031 peak/dotted rhythm. Consumer validation, render/recheck, and final artifact closure remain Stage 5 work. Do not call this freeze a completed delivery.