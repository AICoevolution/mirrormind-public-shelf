# Phase 1 frozen checkpoint — BLOCKED_SOURCE_FRAME

Date: 2026-09-22. Reviewer: Astra task, independent direct inspection of the allowed printed page. No musical-review subagent. This is a blocked checkpoint, not certification that Phase 1 or the musical review is complete.

## Launch gate and access boundary

The authorization has schema astra_human_authorization.v1 and decision AUTHORIZE. Its reviewer_handoff_sha256 matches the current handoff: c3829eed7ae5e12cf1bdc25370b8e83e45ab2500394167ae00fa84232f7fd5c7. The authorization hash is aebab6199a5386925c77db24f62baee39c6dabd07d025e30009db330632e1297. All seven Phase 1 allowlisted file hashes match. See phase1_hashes.json.

Only the launch-gate files and Phase 1 allowlisted source files were read or hashed. The movement directory was listed to locate the gate. No Phase 2 or Phase 3 evidence file was opened or hashed. Later-phase filenames/hashes and summary fields are present in the authorized handoff itself; they were not used as musical evidence. The PDF was hashed; musical inspection used its frozen full-page PNG, plus reviewer-created lossless rectangular extracts. Referenced prepared system crops were NOT opened because they are not in the Phase 1 allowlist. No existing prepared-run file was changed.

Write access initially failed for the new child folder. After an approved parent-folder permission grant, the reviewer workspace and hash log were created successfully. All writes inside the movement directory are confined to astra_review_20260922.

## Direct print structural survey

The complete page was inspected, followed by all five grand-staff extracts and focused closing-region extracts. Printed page number 43; title “27. Little Song in Canon-form”; plate number 41459. One page, five systems, two staves throughout. Physical regions by system: S1 P001–P009 (9); S2 P010–P019 (10); S3 P020–P029 (10); S4 P030–P039 (10); S5 P040–P048 (9). Total 48, including the two pickup regions and the terminal partial. Region numbering includes pickups and is not conventional full-measure numbering.

Both opening staves show 2/4. No later meter declaration was seen. Staff 1 uses G clef on line 2; staff 2 F clef on line 4. System-start clefs repeat these; no mid-system clef change was seen. The opening has no key signature; the sharp before its first upper note is an accidental. P018 introduces three sharps on both staves; S3 repeats that key. Cancellation naturals follow the P029 double bar, with no key signature at S4/P030. No other printed key-signature change was seen.

P001 has one eighth in the upper staff and an eighth rest in the lower staff: capacity 1/2 quarter unit. P030 has one eighth in each staff (a chord in the lower staff): capacity 1/2. P048 has a sounding eighth followed by two eighth rests in each staff: capacity 3/2. The other regions have the full 2/4 capacity of 2 quarter units. The printed meter must remain 2/4; partial capacity is a separate property. These observations support the main capacity table but contradict redundant frozen evidence at P048, as detailed below. Arithmetic pairing of remote pickups and a closing partial is not independent evidence of a playback route or musical phrase completion.

The provided five page-space vertical crop bounds preserve complete grand staves. Reviewer crops use these same bounds, independently extracting pixels from the allowed page image. No reader correspondence can be certified in this phase; its evidence remains unopened.

## Frame blockers and exact evidence

### FRAME-1 — page 1, system 5, P048, both staves

The frozen special-barline evidence in physical_score_lock.json, reviewer_phase1_frame_lock.json, and frame_visual_verification.json says: “Last region is a complete 2/4: RH half rest against LH half E2 under pp.” The main capacity table and partial-bar descriptions in the same frame instead say 3/2, with an eighth followed by two eighth rests.

Direct pixels support the latter. The upper staff has an eighth chord followed by two eighth rests. The lower staff has an eighth octave followed by two eighth rests. The closing thin-thick barline follows those three eighth-note units. There is no half rest above and no half note below. This is both an incorrect printed claim and an internal conflict about rhythmic capacity. Choosing one machine field silently would conceal the contradiction in the frozen source frame.

Evidence: FRAME-1_P048.png, extracted from page-1.png at x=1450, y=1850, width=240, height=340. P048 lies to the right of the internal barline in that crop; the small left portion belongs to P047. The full context is print_system_5.png.

Required repair: preserve printed 2/4 and capacity 3/2, reconcile the stale special-barline descriptions across the frame files, then regenerate affected frozen metadata, handoff hashes, and human authorization. Do not add a fourth eighth unit to the final region.

### FRAME-2 — page 1, system 3, P029, both staves

The frozen special-barline evidence in all three frame files describes P029 as “a complete 2/4 of half notes.” A capacity-check evidence entry repeats this description. The printed upper line instead has four beamed moving eighths, with a dotted-quarter inner note; the lower staff also has moving material. The terminal light-light double bar and following cancellation naturals are present as claimed. The full 2-quarter-unit capacity remains consistent with the print.

Evidence: FRAME-2_P029.png, extracted from page-1.png at x=1330, y=1016, width=340, height=350. The left portion includes P028; P029 starts at page x=1458 and ends at the double bar near x=1579. The full context is print_system_3.png.

Required repair: change the erroneous rhythm description everywhere it is used as frame/capacity evidence; retain P029 capacity 2, numbering, and double bar. This issue does not independently require a duration change. It is separately repairable from FRAME-1.

## Print-only MARKS observations preserved at the stop

These are direct observations, not reader or model claims. Fingerings are omitted. This survey is retained to support a resumed review; it is NOT a complete event-attached spanner inventory. Exact endpoints of every slur/tie must still be frozen before Phase 2 may open on a repaired frame.

- Opening: “Andante molto espressivo”, quarter note = 60. Dynamic p at P001 between staves.
- S1: crescendos under P002 and P006; diminuendo under P008. Upper melodic accents at P003 and P006; lower/inner accents at P004, P007, and P009. An arpeggiation sign precedes the upper-staff chord at P009. Multiple phrase arcs above the upper melody and between/below the staves, plus lower sustained-note ties through P006–P009 and a short upper tie at P006–P007. The upper phrase at the right edge continues into the next system and requires joint endpoint inspection.
- S2: melodic accents at P011, P014, and P016; inner accents at P012 and P015. An arpeggiation sign precedes the P017 upper chord. Dynamic mf at P018. Legato arcs recur at the actual printed locations, including cross-staff contexts; short repeated-pitch ties are visible at P014–P015 and lower-staff P015–P017. These are observations of the printed curves, not an instruction to preserve a particular OMR voice label.
- S3: “cresc.” in P020 and “dim.” in P023. Crescendo under P026, diminuendo under P027, and a crescendo spanning late P028/P029. Upper and lower phrase arcs run through the system. Several inner sustained notes tie across barlines, including the passage P021–P024; additional upper/lower ties appear in P026–P029. Accidental naturals and sharps in this passage are pitch evidence, not expressive marks. The three terminal naturals are cancellation-key glyphs.
- S4: dynamic p at pickup P030. Upper accents at P032, P035, and P037; inner accents at P033 and P036. Crescendo in P039, leading into S5. A lower-staff tie crosses P030–P031. Further lower sustained-note ties occur through P035–P038. Phrase arcs span the upper, lower, and cross-staff lines, including a phrase continuing from P039 into S5.
- S5: sf at P040, diminuendo under P041, crescendo under P043, diminuendo under P045, “ritard.” through the P046/P047 area, and pp in P047 (carrying to P048). Long upper and lower phrase arcs must be checked jointly with S4 endpoints; additional lower-staff ties and phrase arcs occur in P040–P047.
- No pedal text, pedal-release sign, trill/turn/mordent symbol, fermata, or explicit octave-shift marking was seen in the complete-page survey. No explicit staccato-dot inventory has been certified: isolated small dots must be distinguished from duration dots and print damage at event level. Exact tie/slur endpoints, the precise ritardando attachment, and any isolated articulation remain unfinished at this frame stop.

## ROUTE inventory from the whole print

No repeat dots/barlines, volta brackets, segno, coda, D.C., D.S., Fine, or other navigation instruction was seen on any of the five systems. There is a light-light section double bar after P029, followed by key cancellation naturals. P048 ends with a thin-thick final barline. Neither is a repeat. The observed route is the 48 physical regions in written order, with no duplicated passage implied. This is a print observation only; no candidate playback metadata has been inspected.

## Frozen status and next gate

BLOCKED_SOURCE_FRAME. Phase 2 accessed: false. Phase 3 accessed: false. Stage 5 not started. No candidate copy, correction, export, validation, delivery XML, or publication was produced. A complete MARKS endpoint inventory and candidate event audit remain outstanding. No claim of full musical coverage or consumer readiness is made.

The machine-facing phase1_blockers.json contains one issue per repair, with human_outcome null. The reviewer did not repair the prepared frame, authorization, handoff, queue, or pipeline. Resume only after the source-frame owner reconciles the claims and supplies a freshly hashed handoff with matching human authorization. The existing hashes pass; the blocker is the contradictory printed evidence, not a hash mismatch.
