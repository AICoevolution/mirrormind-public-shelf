# UNVERIFIED — Allegretto., K496 movement III

Independent review is complete for human verification. Use [revision03 MusicXML](delivery_final/revisions/UNVERIFIED_revision03.musicxml), SHA-256 `1453c505d1bdd9c40f84f7f3ef946cd9833c0147ad5cadef83fc376e686fc30b`. Earlier XML files and Apply/rebuild diagnostics are history; the full revision03 XML is the notation authority. No publication or human acceptance is authorized.

The print-only orientation covers eight pages and 38 systems. The accepted candidate audit covers all 174 physical bars and four staves (696 bar/staff units). Final direct visual comparisons cover all 222 systems across widths/zooms 1350/1, 1000/1, 1000/0.9 and 900/1. See [visual observations](validation/revision03/visual_inspections.json) and [accepted audit](reviewer/candidate_audit.json).

The exact primary is PROPER. Independent repeat/ending expansion and tie handling agree with ScoreAnalyzer: 283 bar visits and 5,606 sounding attacks, with no missing or extra attacks. All four production layouts have no missing/extra mapped events or VexFlow tick mismatches. These checks establish usable timing and rendering, not a performance interpretation or proof that every uncertain printed reading is correct.

Three explicit delivery issues remain: **DELIVERY-SEP-MARKS**, **VISUAL-P122-LABELS**, and **VISUAL-P037-LEGATO**. They block publication pending review. Primary playback and mapping pass. MARKS readiness is LIMITED and presentation readiness is REVIEW_REQUIRED. Musical reading and grace-performance questions below also remain open.

The correction chain is preserved in [correction history](delivery_final/revisions/correction_ledger_revision03.json). Revision01 resolves touching slur numbers, implicit triplet rendering and four piano stem directions at bar5. Revision02 normalizes barline containers at the four ending pairs without changing their musical children. Revision03 sorts unchanged beam children at two violin notes in bar105, eliminating the extra flag. All revisions received host release. Final bar174 now renders the printed double bar without repeat dots.

Six continuous musical lines are retained: violin, cello, principal upper piano (crossing staff at bar61), an independent upper held/inner line, lower accompaniment, and an independent lower held/inner line. Seven SEP staff/voice columns represent those six lines because the principal piano line crosses staves. All 573 primary beam groups are closed; bar61 changes staves between complete four-note beam groups. The engraving checker’s odd voice-phantom warning there is retained and explained by [member evidence](validation/revision03/beam_membership_checks.json) and [topology](delivery_final/voice_topology.json).

CORE Apply is byte-exact on the primary. A fresh standalone CORE rebuild preserves sounding event semantics after tie-child ordering normalization, but does not preserve the complete notation/voice/route payload and is not a replacement score. MARKS Apply completes but changes exact slur numbering/order at 32 anchored notes. Protected ornaments, fingering/technical payloads, arpeggiation and member ties remain exact. ROUTE Apply preserves musical and notation projections but normalizes XML bytes. See [raw layer checks](validation/revision03/layer_checks.json), [MARKS detail](validation/revision03/marks_payload_checks.json), and [eight-category checks](validation/primary_revision_checks.json).

The reviewed [namecard](delivery_final/namecard.json) uses the printed title “Allegretto.”. Full composer, arranger, lyricist, rights and printed instrument labels are not supplied on these movement pages; no fuller credits are inferred from the footer initials. Frame roles remain violin, cello and piano.

## What to check

Read each item with its close source crop and current render. Compare the retained interpretation and alternatives, then listen/read the primary. Record decisions manually; all human outcomes below remain null. Physical bar numbers refer to the approved frame.

### GRACE-P025-S3-TIMING

**Address:** {"part": "Pianoforte", "bar": 25, "staff": "3", "note": "m025-s3-v1-e04"}

How should the unslashed D5 grace before tied D6 be realized in playback?

**Retained:** Encode the printed unslashed sixteenth as grace with zero metrical duration; do not prescribe steal-time percentages. Preserve D6 half value and its tie.

**Why open:** The print specifies small unslashed notation and slur but no unique performance duration.

**Alternatives:** Short appoggiatura drawn from following D6; Longer expressive appoggiatura determined by human performance review

**Evidence:** [reviewer/crops/system_05_bar25_piano.png](reviewer/crops/system_05_bar25_piano.png)

### GRACE-P034-S3-TIMING

**Address:** {"part": "Pianoforte", "bar": 34, "staff": "3", "note": "m034-s3-v2-grace01"}

How should the unslashed D5 grace into tied D6 be realized?

**Retained:** Zero metrical duration grace with printed sixteenth type, no steal-time percentage. Keep D6 quarter tied to next eighth.

**Why open:** Print defines grace notation, not unique performance duration.

**Alternatives:** Short appoggiatura; Longer expressive appoggiatura

**Evidence:** [reviewer/crops/system_07.png](reviewer/crops/system_07.png)

### GRACE-P049-S1-TIMING

**Address:** {"part": "Violino", "bar": 49, "staff": "1", "note": "m049-s1-v1-grace01"}

How should the three small unslashed notes before G5 be realized?

**Retained:** Retain printed F#5/G5/A5 small 32nd group with zero metrical duration, no steal-time fraction.

**Why open:** Written grace group does not uniquely prescribe performance duration.

**Alternatives:** Short lead-in; More sustained appoggiatura realization

**Evidence:** [reviewer/crops/system_10_bar49.png](reviewer/crops/system_10_bar49.png)

### GRACE-P074-P079-S1-TIMING

**Address:** {"part": "Violino", "bars": [74, 75, 76, 77, 78, 79], "staff": "1", "note": "small notes before dotted-eighth figures"}

How should the repeated small unslashed 32nd notes be realized in Variation IV?

**Retained:** Keep printed F4 grace at P074–P078 and Eb4/D4 graces at P079 as zero-metrical-duration 32nds with no steal-time percentage.

**Why open:** Three small flags and unslashed stems establish notation but do not specify unique performance timing. Reader grace types disagree; enlarged print supports 32nds.

**Alternatives:** Short ornamental lead-in; Longer appoggiatura-style realization

**Evidence:** [reviewer/crops/system_17_73_75.png](reviewer/crops/system_17_73_75.png), [reviewer/crops/system_17_76_77.png](reviewer/crops/system_17_76_77.png), [reviewer/crops/system_17_78_79.png](reviewer/crops/system_17_78_79.png)

### GRACE-P080-P087-S1-TIMING

**Address:** {"part": "Violino", "bars": [80, 87], "staff": "1"}

How should these small unslashed notes be timed?

**Retained:** Keep C4/C4 graces in P080 and F4 grace in P087 as zero-duration 32nds, with no invented steal-time value.

**Why open:** Print supplies grace pitches and flags but not a unique performance realization.

**Alternatives:** Short lead-in; Appoggiatura-style realization

**Evidence:** [reviewer/crops/system_18_80_83.png](reviewer/crops/system_18_80_83.png), [reviewer/crops/system_18_86_87.png](reviewer/crops/system_18_86_87.png)

### GRACE-P088-P092-S1-TIMING

**Address:** {"part": "Violino", "bars": [88, 89, 90, 91, 92], "staff": "1"}

How should the small unslashed notes in this continuation be realized?

**Retained:** Preserve F4,F5,Eb5/D5,C5/C5,Bb4 grace pitches as zero-duration32nds before the dotted eighths, no invented time allocation.

**Why open:** Printed small notes determine notation but not unique performance timing.

**Alternatives:** Short lead-in; Appoggiatura-style realization

**Evidence:** [reviewer/crops/system_19_88_89.png](reviewer/crops/system_19_88_89.png), [reviewer/crops/system_19_90_92.png](reviewer/crops/system_19_90_92.png)

### GRACE-P093-P096-S1-TIMING

**Address:** {"part": "Violino", "bars": [93, 94, 95, 96], "staff": "1"}

How should the small unslashed notes before dotted figures be timed?

**Retained:** Keep Bb3,F4,Eb4/D4,C4/C4 small notes as zero-duration32nds, without invented steal-time.

**Why open:** Notation does not uniquely determine performance timing.

**Alternatives:** Short lead-in; Appoggiatura-style realization

**Evidence:** [reviewer/crops/system_20_93_95.png](reviewer/crops/system_20_93_95.png), [reviewer/crops/system_20_96_98.png](reviewer/crops/system_20_96_98.png)

### SLUR-P098-S1-ENDPOINT

**Address:** {"part": "Violino", "bar": 98, "staff": "1", "note": "m098-s1-v1-e09"}

Does the final F#4 slur continue to the first B4 of Variation V?

**Retained:** Provisionally connect P098 final F#4 to P099 B4 below, keeping this interpretation unresolved.

**Why open:** Curve leaves final F#4 toward right system edge, but no clear continuation arch is visible at next violin entry. Piano has a visible corresponding continuation; that is supporting context only.

**Alternatives:** Connect to P099 B4; Retain only local curve as unpaired graphic pending source clarification

**Evidence:** [reviewer/crops/system_20_bar98_violin.png](reviewer/crops/system_20_bar98_violin.png), [reviewer/crops/system_21.png](reviewer/crops/system_21.png)

### GRACE-P100-S3-TIMING

**Address:** {"part": "Pianoforte", "bar": 100, "staff": "3", "note": "C#5 D5 E5 grace group"}

How should the unslashed three-note grace group be realized?

**Retained:** Retain three32nds at zero metrical duration, with no steal-time fraction.

**Why open:** Printed grace notation does not uniquely prescribe performance timing.

**Alternatives:** Quick lead-in; Longer appoggiatura-style realization

**Evidence:** [reviewer/crops/system_21_99_100.png](reviewer/crops/system_21_99_100.png)

### GRACE-P157-P163-PERFORMANCE

**Address:** Violin P157–P163 small notes before dotted eighths

How should the small unslashed thirty-seconds take time from the surrounding sustained/main notes?

**Retained:** Encode small notes as zero-metrical-duration unslashed grace32nds; retain main printed values; human listening to determine realization.

**Why open:** Print gives small-note values but no unique performance-time allocation.

**Alternatives:** Before-beat realization; On-beat time borrowed from following main note

**Evidence:** [reviewer/crops/system_35_violin_graces.png](reviewer/crops/system_35_violin_graces.png), [reviewer/crops/system_36_violin.png](reviewer/crops/system_36_violin.png)

### GRACE-P164-P170-PERFORMANCE

**Address:** {"parts": ["Violino", "Pianoforte"], "bars": [164, 165, 167, 169, 170]}

How should the closing unslashed grace32nds be timed?

**Retained:** Zero metrical duration, unslashed 32nd written types, no invented steal-time percentages. Preserve main printed durations.

**Why open:** Printed small notes specify notation but no unique performance allocation.

**Alternatives:** Before-beat realization; On-beat appoggiatura realization

**Evidence:** [reviewer/crops/system_37.png](reviewer/crops/system_37.png), [reviewer/crops/system_38_piano_run.png](reviewer/crops/system_38_piano_run.png)

### FINGERING-P033-S3

**Address:** {"part": "Pianoforte", "bar": 33, "staff": "3", "note": "lower D5 quarter near end of P033"}

Is the small stroke below the lower D5 a printed fingering 1 or a broken curve/print blemish?

**Retained:** Retain no fingering provisionally; do not treat the reader-reported 1 as confirmed print.

**Why open:** Small angled stroke lies beside the slur/tie geometry; source is too damaged to distinguish a numeral confidently.

**Alternatives:** Add fingering 1 below the lower D5; No fingering; preserve only musical curves

**Evidence:** [reviewer/crops/P033_possible_fingering.png](reviewer/crops/P033_possible_fingering.png), [reviewer/crops/system_07.png](reviewer/crops/system_07.png)

### DELIVERY-SEP-MARKS

**Address:** MARKS layer, including physical bars 35–36,49,155,170 and unsupported ornaments

Review MARKS normalization and unsupported ornament/text warnings before accepting a layer edit.

**Retained:** Keep released revision03 MusicXML authoritative. Diagnostic MARKS Apply normalizes slur numbering/order at 32 anchored notes; exact slur payload comparison fails. Ornaments, technical/fingering, arpeggiation and member ties are preserved exactly. Do not substitute the diagnostic XML.

**Why open:** MARKS Apply now completes and text is a fixed point, but exact slur payload comparison finds 32 note-level changes (number renaming and endpoint child ordering). Unsupported ornaments and voice-bound text still warn. Do not equate normalized codec output with a print certificate.

**Review scope:** These payloads remain in the immutable primary; CORE Apply was byte-exact. Direct primary playback is independently verified.

**Evidence:** [validation/layer_checks.json](validation/layer_checks.json), [delivery_final/MARKS.sep](delivery_final/MARKS.sep), [validation/revision01/layer_checks.json](validation/revision01/layer_checks.json), [validation/revision01/marks_payload_checks.json](validation/revision01/marks_payload_checks.json), [validation/revision03/layer_checks.json](validation/revision03/layer_checks.json), [validation/revision03/marks_payload_checks.json](validation/revision03/marks_payload_checks.json)

### METADATA-UNPRINTED-CREDITS

**Address:** Supplied PDF pages1–8, header/footer

If fuller catalog credits are desired, provide an authoritative title/composer/instrument-credit page; these movement pages print Allegretto. and W. A. M. 496. only.

**Retained:** Use Allegretto. as the printed movement title; leave composer, arranger, lyricist, rights and printed part-name strings empty. Preserve frame instrument roles separately.

**Why open:** Full composer and instrument names are not printed on the supplied movement pages; footer initials are not expanded into a credit.

**Alternatives:** Retain the source-limited namecard; Supply separate authoritative bibliographic evidence for later metadata review

**Evidence:** [reviewer/orientation.json](reviewer/orientation.json)

### VISUAL-P122-LABELS

**Address:** {"bar": 122, "parts": ["Violino", "Pianoforte"], "layouts": ["w1350-z1", "w1000-z1", "w1000-z0.9", "w900-z1"]}

Review placement of Tempo primo. beside VAR. VI. at the variation boundary.

**Retained:** Retain readable text and correct XML onset; viewer puts the violin tempo text partly over preceding fermata.

**Why open:** Horizontal placement does not align neatly with the intended variation entrance.

**Review scope:** Both strings remain fully readable; notes and fermata are unobscured, and the source plus XML anchor identify the intended entrance. Human can review the placement without altered timing.

**Evidence:** [validation/revision02/visual_checks.json](validation/revision02/visual_checks.json), [validation/revision02/production_render_revision02/w1350-z1-system-27.png](validation/revision02/production_render_revision02/w1350-z1-system-27.png), [validation/revision02/production_render_revision02/w1000-z1-system-40.png](validation/revision02/production_render_revision02/w1000-z1-system-40.png), [validation/revision02/production_render_revision02/w1000-z0.9-system-36.png](validation/revision02/production_render_revision02/w1000-z0.9-system-36.png), [validation/revision02/production_render_revision02/w900-z1-system-49.png](validation/revision02/production_render_revision02/w900-z1-system-49.png), [reviewer/crops/system_27.png](reviewer/crops/system_27.png), [validation/revision03/visual_inspections.json](validation/revision03/visual_inspections.json), [validation/revision03/production_render_revision03/w1350-z1-system-27.png](validation/revision03/production_render_revision03/w1350-z1-system-27.png), [validation/revision03/production_render_revision03/w1000-z1-system-40.png](validation/revision03/production_render_revision03/w1000-z1-system-40.png), [validation/revision03/production_render_revision03/w1000-z0.9-system-36.png](validation/revision03/production_render_revision03/w1000-z0.9-system-36.png), [validation/revision03/production_render_revision03/w900-z1-system-49.png](validation/revision03/production_render_revision03/w900-z1-system-49.png)

### SLUR-P151-P152-S4-START

**Address:** {"part": "Pianoforte", "staff": "4", "bars": [151, 152], "encoded_start": "m151-s4-v1-e01", "encoded_stop": "m152-s4-v1-e08"}

Should the lower-piano phrase begin at P152 rather than the currently encoded first note of P151?

**Retained:** Retain the released source-audit interpretation provisionally; do not present its earlier supported label as certainty. Compare original system34 before publication.

**Why open:** The earlier audit describes a continuous arch across the barline, but this focused source/render comparison sees the clearest arch beginning over P152. The current render includes an extra preceding bar under the phrase.

**Alternatives:** Keep current P151 start if the faint preceding arch can be established in original print.; Move start to first lower-piano note in P152, retaining stop m152-s4-v1-e08.

**Evidence:** [reviewer/crops/system_34.png](reviewer/crops/system_34.png), [reviewer/inspection_system_34.json](reviewer/inspection_system_34.json), [validation/revision03/visual_inspections.json](validation/revision03/visual_inspections.json), [validation/revision03/production_render_revision03/w1350-z1-system-34.png](validation/revision03/production_render_revision03/w1350-z1-system-34.png), [validation/revision03/production_render_revision03/w1350-z1-system-35.png](validation/revision03/production_render_revision03/w1350-z1-system-35.png)

### VISUAL-P037-LEGATO

**Address:** {"part": "Pianoforte", "staff": 3, "bar": 37, "layouts": ["1350/1", "1000/1", "1000/0.9", "900/1"]}

Review the legato label touching the repeat barline at the Variation II entrance.

**Retained:** Retain the full word on the correct piano staff and onset; defer its horizontal placement for human review.

**Why open:** The initial letters intersect the thick repeat barline.

**Review scope:** The word legato is recognizable; its piano ownership and variation entrance are clear. The repeat dots, pitches and durations remain distinct.

**Evidence:** [reviewer/crops/system_08.png](reviewer/crops/system_08.png), [validation/revision03/visual_inspections.json](validation/revision03/visual_inspections.json), [validation/revision03/production_render_revision03/w1000-z0.9-system-09.png](validation/revision03/production_render_revision03/w1000-z0.9-system-09.png), [validation/revision03/production_render_revision03/w900-z1-system-12.png](validation/revision03/production_render_revision03/w900-z1-system-12.png)

## Resolved findings retained in the register

- **DELIVERY-SLUR-M155** — Revision01 separates source-supported touching slur numbers without moving endpoints. Revision03 structural check has no broken findings; all four final layouts inspected.
- **DELIVERY-SLUR-M170** — Revision01 separates source-supported touching slur numbers without moving endpoints. Revision03 structural check has no broken findings; all four final layouts inspected.
- **DELIVERY-SLUR-M35** — Revision01 separates source-supported touching slur numbers without moving endpoints. Revision03 structural check has no broken findings; all four final layouts inspected.
- **DELIVERY-SLUR-M36** — Revision01 separates source-supported touching slur numbers without moving endpoints. Revision03 structural check has no broken findings; all four final layouts inspected.
- **DELIVERY-SLUR-M49** — Revision01 separates source-supported touching slur numbers without moving endpoints. Revision03 structural check has no broken findings; all four final layouts inspected.
- **DELIVERY-FINAL-BAR-REPEAT** — Released revision02 normalizes barline containers without changing musical children. Fresh revision03 renders in all four layouts show the printed final double bar without repeat dots.
- **DELIVERY-VEXFLOW-TUPLETS** — Released hidden endpoints preserve printed rhythm and omitted numerals. Zero missing/extra events and zero tick mismatches in all four layouts.
- **ERRATUM-P005-STEMS** — Revision01 applies the four source-supported downward stems; confirmed in all four revision03 layouts.
- **VISUAL-P105-FLAGS** — Host-released revision03 orders unchanged beam children on the two named violin notes. All four production layouts show three continuous beams and the required fourth backward hooks without the stray flag.

All 26 stable/register items, including resolved history, are retained in [human_attention.json](human_attention.json). Source-audit files and all accepted XML versions remain preserved. The new bar151–152 lower-piano slur-start question qualifies the earlier audit: its current start is provisional, not asserted as certain print.
