# Erratum 002 — printed engraving attachment and explicit rest positions

Frozen before application; confidence high; human_outcome null. Focused rendered review found the generic stem-side slur placement rule did not preserve the printed side at the following spans. Set both slur endpoints explicitly above: RH P10@0->11@0, P12@2.5->13@0, P17@0->17@1, P27@0->27@1.5; LH P9@0->9@1.5, P17@0->17@1, P27@0->27@1.5, P38/P39/P40@1->same@1.5, P49@1.5->51@0, P51@1.5->53@0. Other frozen endpoints remain unchanged. Evidence is the corresponding original print-system PNGs and first rendered system PNGs.

Explicitly position all printed rests on the central staff line using display-step/display-octave: B4 under treble, D3 under bass, as governed by the frozen effective clef timeline. This prevents the installed viewer from displacing the principal-line rests below the independent sustained bass. No extra rest or duration is introduced.

Restate the already-active RH F4 clef at P2 onset0 and LH F4 at P19 onset0 with print-object=no. These are hidden state restatements, not new printed clef changes. They mitigate observed viewer state leakage from the two simultaneous opening clefs and the P18 end cautionary. Preserve the original printed initial G2->F4 and end-P18 LH F4 declarations. Verify render and exact sounding schedule again.

Give Allegro vivace text and metronome separate default-x positions and a common above-staff height; place below-staff text explicitly below the RH staff. These are layout attributes only. No tempo, dynamic or textual content changes. Set ties below except the upper F#4/A4 sustained ties P55-P57 above, matching the print's separation of upper and inner spans.

This erratum does not authorize changing production viewer code. Any remaining wrong stem direction, shared-beam rendering, or cautionary-clef placement must remain a reported renderer limitation. The delivery MusicXML must retain the printed stem directions and musical line identities.
