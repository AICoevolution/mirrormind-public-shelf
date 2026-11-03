# Incomplete review — engineering repair required

Released primary: `delivery_final/revisions/UNVERIFIED_revision01.musicxml` (SHA256 `6cc7bfa0a58b5974ade04bd721116139214b9c7a4a32a1af2c307f5ebaa7c047`). This is UNVERIFIED and not delivery-ready.

Revision01 applied 22 source-supported note-local changes after a validated host release. PROPER passes; no broken engraving findings remain. Independent playback matches 5,606 attacks across 283 played bars. All four required layouts have complete note mapping and zero VexFlow timing mismatches. The original accepted XML and audit remain unchanged.

**DELIVERY-FINAL-BAR-REPEAT blocks delivery.** All four layouts show an unprinted backward repeat at bar174. [Diagnosis](validation/revision01/route_display_diagnosis.json) and [visual evidence](validation/revision01/visual_checks.json) isolate a barline serialization/viewer interaction. A separate diagnostic normalization removes the dots; that file is not a delivery candidate. Structural barline edits exceed the host-authorized note-local revision scope.

Detailed all-layout visual coverage remains incomplete. Preserve the existing audit; after an authorized repair rerun required checks and complete changed-context, connected-span, beam-member, rest-lane, and text-placement comparisons. P105 flag-stroke and P122 label-placement checks remain open.

**DELIVERY-SEP-MARKS remains unresolved.** Apply now succeeds but renumbers/reorders some slur payloads; unsupported ornament/text warnings remain. Full XML stays authoritative. See [fresh checks](validation/revision01/marks_payload_checks.json).

Human interpretation questions retained (no human answer inferred):

- **GRACE-P025-S3-TIMING** — How should the unslashed D5 grace before tied D6 be realized in playback? Retained treatment: Encode the printed unslashed sixteenth as grace with zero metrical duration; do not prescribe steal-time percentages. Preserve D6 half value and its tie.
- **GRACE-P034-S3-TIMING** — How should the unslashed D5 grace into tied D6 be realized? Retained treatment: Zero metrical duration grace with printed sixteenth type, no steal-time percentage. Keep D6 quarter tied to next eighth.
- **GRACE-P049-S1-TIMING** — How should the three small unslashed notes before G5 be realized? Retained treatment: Retain printed F#5/G5/A5 small 32nd group with zero metrical duration, no steal-time fraction.
- **GRACE-P074-P079-S1-TIMING** — How should the repeated small unslashed 32nd notes be realized in Variation IV? Retained treatment: Keep printed F4 grace at P074–P078 and Eb4/D4 graces at P079 as zero-metrical-duration 32nds with no steal-time percentage.
- **GRACE-P080-P087-S1-TIMING** — How should these small unslashed notes be timed? Retained treatment: Keep C4/C4 graces in P080 and F4 grace in P087 as zero-duration 32nds, with no invented steal-time value.
- **GRACE-P088-P092-S1-TIMING** — How should the small unslashed notes in this continuation be realized? Retained treatment: Preserve F4,F5,Eb5/D5,C5/C5,Bb4 grace pitches as zero-duration32nds before the dotted eighths, no invented time allocation.
- **GRACE-P093-P096-S1-TIMING** — How should the small unslashed notes before dotted figures be timed? Retained treatment: Keep Bb3,F4,Eb4/D4,C4/C4 small notes as zero-duration32nds, without invented steal-time.
- **SLUR-P098-S1-ENDPOINT** — Does the final F#4 slur continue to the first B4 of Variation V? Retained treatment: Provisionally connect P098 final F#4 to P099 B4 below, keeping this interpretation unresolved.
- **GRACE-P100-S3-TIMING** — How should the unslashed three-note grace group be realized? Retained treatment: Retain three32nds at zero metrical duration, with no steal-time fraction.
- **GRACE-P157-P163-PERFORMANCE** — How should the small unslashed thirty-seconds take time from the surrounding sustained/main notes? Retained treatment: Encode small notes as zero-metrical-duration unslashed grace32nds; retain main printed values; human listening to determine realization.
- **GRACE-P164-P170-PERFORMANCE** — How should the closing unslashed grace32nds be timed? Retained treatment: Zero metrical duration, unslashed 32nd written types, no invented steal-time percentages. Preserve main printed durations.
- **FINGERING-P033-S3** — Is the small stroke below the lower D5 a printed fingering 1 or a broken curve/print blemish? Retained treatment: Retain no fingering provisionally; do not treat the reader-reported 1 as confirmed print.
- **DELIVERY-SEP-MARKS** — Review MARKS normalization and unsupported ornament/text warnings before accepting a layer edit. Retained treatment: Keep released full XML authoritative. Diagnostic Apply preserves anchored ornaments, technical notation, arpeggiation and member ties; exact slur comparison remains nonidentical.
- **METADATA-UNPRINTED-CREDITS** — If fuller catalog credits are desired, provide an authoritative title/composer/instrument-credit page; these movement pages print Allegretto. and W. A. M. 496. only. Retained treatment: Use Allegretto. as the printed movement title; leave composer, arranger, lyricist, rights and printed part-name strings empty. Preserve frame instrument roles separately.
- **DELIVERY-FINAL-BAR-REPEAT** — Engineering: repair the barline serialization/viewer interaction that adds a false P174 repeat in all layouts. Retained treatment: Preserve released revision01; retain diagnostic normalization only as evidence, never delivery. Stop at essential-notation gate until host-authorized repair.

All 22 stable attention IDs are retained in [human_attention.json](human_attention.json). Resolved technical items retain their prior evidence and source-supported resolution. No publication or final handoff approval is claimed.
