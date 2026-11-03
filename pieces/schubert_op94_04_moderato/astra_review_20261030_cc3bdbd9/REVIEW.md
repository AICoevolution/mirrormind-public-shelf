# UNVERIFIED delivery for human review

Primary: `delivery_final/UNVERIFIED_schubert_op94_04_moderato.musicxml`
SHA-256: `78a08ae48b6747a116a55a104e92872db3887f1ff25d5f7372c6ed61c681d5c8`

The original Astra Phase 1–3 musical audit and correction decisions are preserved unchanged. This continuation independently reran the current handoff, primary structural, CORE/MARKS/ROUTE, playback, production viewer and encoding checks. Handoff replay now passes; CORE rebuild preserves the musical projection and Apply is byte-identical. All 2325 members, 2671 playback attacks, both layouts and 14 cross-staff beam groups pass their technical comparisons.

All 79 rendered systems were visually rechecked. The six recorded presentation issues remain visible and are retained for human review. The pedal structure observation and MARKS representation limits also remain unresolved. Stage 5 completion means ready for human review, not publication approval or a human stamp. Current evidence is under `continuation_validation/`; old `validation/` reports are historical and retain their original results. No edition catalog was supplied.

Human review questions (not the reason for the technical stop):

## BASS-031-146: P031/P146, lower staff, q=1/4–3/2
Confirm the onset and duration of the accented G#3 against the dotted F#3 and sixteenth rest.
Retained treatment: G#3 quarter at q=1/2, F#3 dotted eighth at q=1/4, E3/D#3 eighths at q=1 and 3/2.
Dense/damaged print leaves the independent inner onset ambiguous; interval validity is not a musical decision.

## CRESC-095-096: P095–096, between staves
Does the printed cresc. begin late in P095 or at P096?
Retained treatment: Attach cresc. below upper staff at P096 q=0.
Text is close to the bar boundary in the print.

## PEDAL-RELEASE: P023/P138 lower staff q=1; following passage
How should the two printed Ped. starts be released or repedaled?
Retained treatment: Retain two sign-only pedal starts; add no unprinted release or sustained playback inference.
The print has no explicit release. Encoding checker reports repeated/unclosed endpoints; engraving checker flags the final open pedal.

## MARKS-REPRESENTATION: P023/P138 Ped.; P178 ppp
Retain the primary XML as the authority for marks omitted by MARKS v0.
Retained treatment: Use the corrected primary. MARKS export is limited; no claim of lossless standalone representation.
MARKS v0 reports unsupported ppp and unclosed pedal signs, while actual Apply preserves the primary events and exact slur endpoints.

## DISPLAY-CODA: P178 upper staff, sectional text Coda.
Confirm the sectional Coda. text and reject any unintended navigation instruction in the view.
Retained treatment: Primary retains words Coda.; playback has no Coda jump.
Production rendering substitutes a To-coda-looking label/sign for the plain printed sectional text.

## DISPLAY-RITARD: P181 above lower staff, q=0; both layouts
Confirm the lower-staff ritard. position and scope.
Retained treatment: Retain the exact staff-2 direction in XML.
Viewer places ritard. above the whole system, at the system beginning (P179 in the narrow layout), away from its encoded P181 lower-staff address.

## DISPLAY-KEY180: P180 q=1, both staves
Confirm the mid-bar change from five flats to four sharps.
Retained treatment: Keep the key change at q=1 in XML. First chord remains F4/Ab4 over Db3/Ab3/Db4.
Viewer draws the new signature at the bar beginning. Explicit accidentals and all displayed note identities remain correct, but the signature timing is visually ambiguous.

## DISPLAY-WEDGE181: P181 lower staff, crescendo q0–1 and diminuendo q1–2
Confirm both hairpins where the upper bass-figuration notes obscure their lines.
Retained treatment: Retain both printed wedges and exact endpoints in XML.
The rendered hairpins crowd/overlap the lower-staff figuration; source and ledger show their intended spans.

## DISPLAY-UNISONS: P018/P048/P133/P163 upper staff, q=0
Confirm independent voices sharing the opening pitch and their different written values.
Retained treatment: Retain the printed independent durations and both voice stems.
The production view uses adjacent/shared heads at the same pitch; dense stems and dots merit visual confirmation.

## DISPLAY-NATURALSHARP: P052/P167 lower-staff F#3 at q=1/4
Confirm the explicit natural-then-sharp cancellation printed after the preceding double sharp.
Retained treatment: XML contains accidental natural-sharp; sounding pitch is F#3.
Viewer displays a sharp without the natural cancellation portion. The pitch is unambiguous under the new bar key but the full printed glyph sequence is not shown.

