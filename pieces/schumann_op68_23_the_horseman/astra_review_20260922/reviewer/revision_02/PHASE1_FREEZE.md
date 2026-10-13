# Phase 1 frozen checkpoint, revision 02

Status: BLOCKED_SOURCE_FRAME. Phase 2 and Phase 3 have not been accessed. No candidate, reader claim, ensemble provenance, or production code was inspected. This is a blocked checkpoint, not a completed MARKS inventory or an accuracy certificate. The user asked to continue during preparation of this checkpoint; the explicit requirement to stop before Phase 2 for an unsafe clef frame still applies.

## Launch gate and prior repairs

Authorization schema astra_human_authorization.v1, decision AUTHORIZE, and handoff hash be7ee91faa9e4ef9ccba0cc4dba0cc62a575526d4eecae24ad2d46866f1cd117 match. Duplicated allowlists agree. All 15 Phase 1 allowlisted inputs were hashed successfully. The six frame_verification files newly listed in Phase 1 were hashed only; their contents were not used as musical authority. The direct print remains the basis of the findings.

P001=1/2 and P018=5/2 quarter-unit capacity repairs remain correct. The nine earlier clef evidence-box repairs are now correct. All 14 declared clef boxes were independently viewed against source pixels in this revision, with exact boxes drawn in green. The complete check is in clef_repair_contact.png; raw detail images and source rectangle metadata are retained. Previous checkpoints remain unchanged.

## Remaining blocker: P052 clef onset

Physical address: page 3, system 11, P052, staff 1. All three frame declarations now specify the treble-clef onset as 3/2 quarter units. The print shows an undotted quarter-note chord before the clef, followed by an eighth-note chord, a quarter-note chord, and an eighth-note chord. The clef therefore applies at onset 1. The later quarter-note chord is at onset 3/2; it is not the first treble-clef event.

Evidence: p052_clef_onset.png is an unaltered pixel crop of source_crops/page-3.png, page rectangle x=1310, y=540, width=350, height=385. It contains both staves across the bar. The first RH chord has a stem and no flag or augmentation dot; the next chord has an eighth flag and occurs after the printed treble clef. The lower staff's dotted rhythm must not be used to assign the upper staff's clef timing.

Exact required frame repair: P052/staff1/G2 onset_q 3/2 -> 1. Keep the repaired evidence box, region ID, clef sign and line, MID_REGION placement, printed 6/8, and full region capacity of 3. Update dependent references as needed and refresh affected freezes, handoff hashes, and human authorization. No padding, trimming, pitch decision, or meter change is justified by this finding.

## Checked framing context

Three pages, printed 37-39; twelve systems; 57 physical regions. System region ranges remain 1-5, 6-9, 10-14, 15-18 / 19-23, 24-27, 28-31, 32-36, 37-41 / 42-47, 48-52, 53-57. Key signature is one flat. Printed meter is 6/8. Pickup capacities P001/P010/P019=1/2; closing partial P018=5/2; terminal P057=3/2. Other locked capacities are 3.

Other effective clef onsets: staff1 P001 F4 at 0; P003 G2 at 5/2; P005 F4 at 5/2; P007 G2 at 5/2; staff2 P014 G2 at 5/2; P018 staff2 cautionary F4 refers to the next governed region; staff1 P019 F4 at 0, P021 G2 at 5/2, P023 F4 at 5/2, P025 G2 at 5/2, P027 F4 at 5/2, P028 G2 at 1, P037 F4 at 5/2. P052 must be G2 at 1.

The unchanged print has backward repeats after P009 and P018, a forward repeat before P010, and final double barline after P057. The complete mark-by-mark inventory and all reader/candidate correspondence checks remain pending until the frame passes. No frozen source, authorization, handoff, queue, or pipeline file has been modified. All work in this revision is confined to the reviewer directory.
