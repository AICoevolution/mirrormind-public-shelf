# PHASE 2 FREEZE

Frozen before candidate access. Phase 1 frame accepted and its inventory retained with PRINT_ERRATUM_001.md. All 21 Phase 2 allowlisted input hashes match. All five system packets inspected: every physical-region reader array is empty. Raw reader_claims.json supplies the actual evidence; its record ordinals, parts, pitches, rhythm, and repeat markers permit independent recovery of correspondence.

## Correspondence, all physical regions
SmartScore uses two parts P1=upper and P2=lower, each ordinal n/raw n corresponds to printed Pn for n=1..28. PlayScore P1 ordinal n/raw n likewise maps Pn for all 28. This was checked through actual note/rhythm sequences, not just equal counts. Audiveris P1 ordinals1..7/raw0..6 correspond P1..7; printed P8 is omitted; ordinals8..27/raw7..26 map P9..28. Its raw8 is second-strain pickup, raw7 backward-repeat cadence, raw26 final repeat. Thus baseline raw-number comparisons misalign much of the score. Do not interpret zero claims in packets as unanimous rests.

| System | Physical regions | SmartScore/PlayScore ordinals | Audiveris ordinals | Direct printed anchors and differences |
|---|---|---|---|---|
| 1 | 1–5 | 1–5 | 1–5 | E4 pickup; A4 C#5 E5 rise; paired chords; ornamented descent; dotted-chord cadence and pickup. SmartScore adds initial quarter rest and G#6 phantom, misconstrues grace rhythm/tuplets. Audiveris replaces ornament with spurious long E5. |
| 2 | 6–9 | 6–9 | 6,7,missing,8 | Low C#4/E4/A4 chord then arpeggio; chordal response; ornament bar P8 distinct from final partial P9. Audiveris drops P7 RH second chord and entire P8. SmartScore splits chord tones into wrong-duration voices; PlayScore E#3 at P6 last chord is false (printed E3). |
| 3 | 10–15 | 10–15 | 9–14 | C#5 pickup; two grace D5 figures; rising subdivided D5 figure; six chordal eighths with hairpins; E5 held over independent RH line; tied upper E5 over staccato lower eighths. SmartScore overfills P14; Audiveris drops grace notes and manufactures tie in P11. PlayScore calls the true P14–15 E5 tie a slur. |
| 4 | 16–21 | 16–21 | 15–20 | D5/F#5 opening voices and subdivision; chordal six-eighth response; B4 then sharped chord; E5 upper over moving lower voice; tied E3 bass and D4/C#4 upper bass line; arpeggio return. PlayScore extra shifted E5 voice in P19 and false E5 tie in P20; SmartScore timing/voice errors; actual independent lines must be preserved. |
| 5 | 22–28 | 22–28 | 21–27 | Chordal rise; ornament over high LH line; dotted chord and pickup; low arpeggio; fermata bar; ornament bar; final repeat cadence. Audiveris loses grace groups, misallocates melody to staff-changing bass lane, invents dynamics. SmartScore creates non-grace notes, tuplets, false ties; PlayScore preserves more but still misses important marks. |

Every reader event set was inspected, including both SmartScore parts. Reader evidence does not certify the candidate. Octaves/accidentals stated here follow staff-line reading. Physical scope includes 28 regions on five systems.

## All 12 priority questions answered
- a6f2c3d91b77: printed P27 and P28 exist, page2/S5, ornament bar and final partial. Audiveris raw25/raw26 correspond. The missing reader region is P8, not the last two bars. Raw labels are not physical IDs.
- 87ce7f367610: opening upper clef is G2, page1/S1/P1. Audiveris raw0 and the other readers raw1 identify the same opening.
- d7430dd72920: opening lower clef is F4 at the same opening.
- 54131eae5749: opening has three sharps on both staves.
- 85b009e82ee5: opening has printed 6/8 on both staves.
- 2b6b9956f206: opening pickup exists; SmartScore raw1 contains it plus an erroneous leading quarter rest. Absence of raw label0 is not a missing printed bar.
- 1fc30edab264: opening pickup exists; PlayScore raw1 contains it accurately.
- 5b4d4e2aa6d2: lower F4 clef printed at P1. SmartScore lower part's unnumbered clef and Audiveris raw0 refer to this same location; claim of their absence is an addressing/extraction artifact.
- f328fb22721d: three sharps at P1; Audiveris raw1 is P2, so no new key required there.
- 7ef234ac1169: 6/8 printed at P1; Audiveris raw1=P2 inherits it.
- e02b4716449f: Audiveris raw8=P10 at page2/S3 repeats three sharps in the system signature. No key change. It is not printed P8.
- 8a68b726a604: P10 inherits 6/8; no printed meter redeclaration at that system start. PlayScore's extra declaration is not a change of meter.

## Independent controls
No deterministic three-reader controls supplied: controls.json=[]; the empty intersection is evidence loss, not a pass. All three parent print controls fail as stated:
1. P1 s1 q0 is **E4** eighth, not E5. Other rhythmic/frame details agree.
2. P14 s1 q0 is **B4 quarter**, not G#5 dotted-quarter. The upper dotted-quarter **E5** enters q1.5. Lower staff E4+G#4 quarter at q0. Enlarged detail-s3.png.
3. P28 s1 q0 is **G#4+B4 dotted-quarter**, not A4+C5 and not A4. Next A4 eighth and eighth rest give 5/2q. detail-s5.png.
Failed controls retained, not discarded. Their confidence values do not override the print.

## MARKS / ROUTE comparison
PlayScore captures most phrase endpoints but misses printed tempo/metronome, piu lento/a tempo, numerous accents and LH fermata; falsely emits octave-shift stops P13/P17 and strong-accent P7; drops RH P7→8 slur and last staccato at P8; P16 slur begins too early; P26–27 endpoint needs repair. Its wedges have offset artifacts outside bars. SmartScore corrupts tempo text, injects title/page/fingerings as words, loses many slurs, invents tenuto P6 and tied connections P11, P20→21, P23→24; grace rhythms become normal durations. Audiveris misses grace groups, carries dangling slurs from omitted P8, invents p at P7/P20/P25 and ppp/pp near P26/P27, misses lower fermata, misreads several small arcs. Both inspected route barlines in all readers identify backward repeat P9, forward P10, backward P28 after mapping; no volta/navigation claim justified. Source family agreement about a mark or pitch remains merely evidence.

Shared blind spots: tempo words/metronome, ornament rendering, independent/unison voices around P14–20, grace/main arc boundaries, two fermatas P26, dynamic/text confusion, comparison using raw labels. Baseline 'proper' for PlayScore only describes arithmetic, not print accuracy; 215 agreed keys are not a certificate. The baseline durations correctly flag many SmartScore/Audiveris overflow artifacts but pickup pairing prose incorrectly links first pickup to final close across strains. Correct route pairs are P1+P9 and P10+P28.

All priority questions answered. Baseline content questions are raw-label-derived; their claims remain available in the digest and are not accepted by majority. The full candidate event audit must independently review every printed event, including purported agreements. No candidate, ensemble manifest, provenance, disagreement, or model content has been opened. Phase 2 is frozen and permits Phase 3.
