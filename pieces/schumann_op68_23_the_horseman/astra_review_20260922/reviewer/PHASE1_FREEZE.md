# Phase 1 frozen stop: clef evidence addressing

Status: BLOCKED_SOURCE_FRAME. This is a frozen blocker checkpoint, not completion of the required full MARKS audit. Phase 2 and Phase 3 have not been accessed. No candidate was inspected or corrected. Stages 4 and 5 remain incomplete.

## Launch gate and repaired findings

The current authorization uses schema astra_human_authorization.v1 and decision AUTHORIZE. Its handoff SHA-256 matches 5117bc9568c7a6a39392daa81f1beb911b27b0677538e10684e026829f766e9a. The duplicated phase allowlists agree. All nine Phase 1 inputs match their declared hashes.

The earlier P001 and P018 capacity blockers are repaired in all three frame files: P001=1/2 and P018=5/2 quarter-note units. These agree with the directly viewed, unchanged print. The printed meter remains 6/8. Earlier frozen review artifacts are retained unchanged under astra_review_20260921.

## Structural observations

The unchanged source has three pages, printed 37-39, with 12 systems and 57 physical regions. Region counts are 5+4+5+4 on page 1, 5+4+4+5+5 on page 2, and 6+5+5 on page 3. The revised system y extents are wider than in the prior frame. Full-page image hashes are unchanged from the earlier print viewing.

Physical address map: P001-P005 S1, P006-P009 S2, P010-P014 S3, P015-P018 S4, P019-P023 S5, P024-P027 S6, P028-P031 S7, P032-P036 S8, P037-P041 S9, P042-P047 S10, P048-P052 S11, P053-P057 S12. Key signature is one flat; no printed meter change. Pickups P001, P010, P019 have capacity 1/2; closing partial P018 has 5/2; terminal P057 has 3/2. Other locked capacities are 3 quarter units.

ROUTE visible on the unchanged pages: backward repeat after P009, forward repeat before P010, backward repeat after P018, terminal double barline after P057. No ending bracket, segno/coda, D.C., or D.S. was seen in the earlier full-page viewing. This checkpoint does not certify reader/playback correspondence.

## Complete declared-clef evidence-box check

Every one of the 14 declared clef-change boxes was checked against a new crop directly derived from the allowed full-page PNG. No prepared system crop or reader evidence was read. Coordinates in the lock are system-crop coordinates; crop x is full-page x, and crop y is offset by the system's current y_bounds_on_page[0]. The coordinate transforms are recorded in clef_crop_metadata.json. Red rectangles in the annotated evidence reproduce the exact locked coordinates. Raw companion PNGs preserve original source pixels.

Nine boxes fail to enclose their claimed glyphs:

|Issue|Page/system/region/staff|Locked box|Printed finding|Effective onset, quarter units|
|---|---|---|---|---|
|FRAME-1|1/1/P001/1|[318,116,358,201]|Box covers meter; bass clef is to the right.|0|
|FRAME-2|1/1/P003/1|[1055,104,1095,211]|Box covers sixteenth notes; treble clef is to the left.|5/2|
|FRAME-3|1/1/P005/1|[1415,111,1460,206]|Box covers first chord; bass clef is after the second tied chord.|5/2|
|FRAME-4|1/2/P007/1|[1009,83,1049,190]|Box covers sixteenth notes; treble clef is to the left.|5/2|
|FRAME-5|2/5/P021/1|[1002,80,1042,187]|Box covers sixteenth notes; treble clef is to the left.|5/2|
|FRAME-6|2/5/P023/1|[1394,87,1439,182]|Box covers first chord; bass clef is after the second tied chord.|5/2|
|FRAME-7|2/6/P025/1|[940,75,982,187]|Box covers sixteenth notes; treble clef is to the left.|5/2|
|FRAME-8|2/6/P027/1|[1369,86,1414,181]|Box covers first chord; bass clef is after the following quarter note.|5/2|
|FRAME-9|2/7/P028/1|[360,58,420,173]|Box covers sixteenth-note figure; treble clef is to the left.|1|

The other five declarations cover their actual glyph: P014 staff 2 treble; P018 staff 2 cautionary bass; P019 staff 1 bass; P037 staff 1 bass; P052 staff 1 treble. Their note-level correspondence remains for later phases.

This is not evidence that the printed clef signs themselves are wrong, and the system/physical-region identities are retained. It is a specific failure of the declared evidence addressing, which the user explicitly makes a stop condition before Phase 2. The P005/P023/P027 textual descriptions also need to identify the correct intervening quarter-note event before the clef, rather than suggest the clef follows immediately after the opening chord.

## MARKS and remaining scope

The prior full-page reading established tempo Allegro vivace, dotted-quarter=100; pp/mf/ff/sf/p/mp dynamic text; poco a poco piu p and dim. sempre; staccatos, accents, tenutos, slurs, ties, hairpins and final fermatas. These observations are not promoted to a complete inventory here. Every mark attachment and connected endpoint still requires the full print-only freeze after the frame is safe. Fingerings remain excluded. No musical ambiguity is resolved from reader agreement or model confidence.

## Required repair and preserved boundaries

phase1_blockers.json gives one issue per independently repairable rectangle and proposed corrected coordinates. A frame owner must confirm the proposed boxes against the same pixels, synchronize the framing files and dependent packets, regenerate affected hashes, and obtain fresh matching human authorization. The reviewer must not alter these source artifacts.

All new evidence and reports are confined to astra_review_20260922/reviewer. The prepared run, source files, handoff, authorization, queue, pipeline and prior checkpoints are unchanged. The shell sandbox again failed before reading files; approved elevated PowerShell was used for scoped reads and reviewer artifact creation. No musical subagent was launched. No delivery or publication is claimed.
