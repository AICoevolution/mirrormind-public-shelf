# Erratum 001 — continuous tie identity and slur numbering

Frozen before application. The first real CORE Apply and independent playback comparison exposed retriggers at the proposed cross-voice tie joins. The print explicitly sustains lower A4/A3 in P17, and lower D2 into P43/P47. Preserve those independent musical lines through their tied destinations instead of rejoining the machine voice at the tie endpoint. This changes the context-scoped topology interpretation, not pitch, onset, duration, staff, meter or sounding chord membership.

P17 RH: remove A4 members from principal events e04/e06/e08 and retain the original lower events m017-s1-v2-e05/e07/e09, voice2, at 1.5/2/2.5 with eighth duration; all stem down, beam begin/continue/end. P17 LH: remove A3 members from principal e04/e06/e07 and place them in voice4, eighths at 1.5/2/2.5, IDs m017-s2-v2-e05/e08/e09; all stem up, beam begin/continue/end. Both initial lower dotted quarters remain lower voices, tie into their same-voice onset1.5 note. Printed common-beam grouping is retained; duplicate coincident beam geometry must be inspected in the render.

P43/P47 LH D2@0 dottedquarter: voice3->voice4, preserving the continuing sustained bass identity from P42/P46. The later octave at1.5 remains the principal chordal line. No artificial visible rest is added to either strand.

All RH slurs use number1; all LH slurs use number2 so simultaneous spans in one MusicXML part cannot overwrite each other's identities. Numbers are implementation identities; printed endpoints remain frozen. This specifically repairs the initial MARKS export's orphaned/never-closed spans.

Evidence: print_system_04.png, print_system_10.png and the initial gate_values.json. Confidence high. Human outcome null. Final voice count remains four. This representation must pass the actual playback comparison; no failure is waived.
