# Phase 1 blocked checkpoint — Schumann Op. 68 No. 29

Status: BLOCKED_SOURCE_FRAME. This freezes the observed blocker, not a completed print inventory or an accuracy certificate. Phase 2 and Phase 3 have not been accessed. No corrections or delivery exports have been attempted.

## Launch and evidence boundary

Authorization schema astra_human_authorization.v1, decision AUTHORIZE, matched reviewer_handoff.json SHA-256 df96034b8939d29d81245fa658b73776cee3d603a3944e50b94d34f07f9cedb5. Authorization SHA-256 efd3f6ba7bd9e27d18813288bbcb67d2155c47bd9426cc6750d668c74c7f9a06. Both Phase 1 allowlist representations agreed. All nine allowlisted file hashes matched. Only the launch-gate documents and Phase 1 files were read from the prepared run. The PDF was hashed, not parsed. All three full-page PNGs were visually inspected; page metadata and frame/configuration JSON were read. Large combined JSON output was truncated; the disputed clef entries were then retrieved explicitly. No pre-existing system crops were opened: the focused evidence was generated directly from the allowlisted page-2.png.

## FRAME-1: treble-clef change one physical region too early

Address: page 2 (printed page 46), system 6 (first system on that page), lower staff, P038/P039 boundary.

The supplied x boundaries for system 6 are 265, 375, 472, 687, 960, 1054, 1161, 1371, 1633. Thus P038 is x=687..960; P039 is x=960..1054. The physical and reviewer frame locks assert G2 at P038 onset 0, REGION_START, effective_region P038, under the second mf. The visual verification repeats this claim.

Direct pixels show four beamed sixteenths, an eighth note, and an eighth rest in P038, all before the G-clef glyph. Their total is 2 quarter units. The glyph is near the right edge of P038, after the rest, before x=960. The half-note chord with mf is in P039. Applying the locked clef at onset 0 would interpret every preceding P038 lower-staff note in the wrong clef. This is a musical framing blocker, not a permissible duration adjustment.

Evidence: FRAME-1.png is an unscaled crop of page-2.png with rectangle [650,150,1100,530] (left, top, right, bottom). It contains the entire disputed lower-staff sequence, the G clef, the boundary, and the following half-note chord. The erroneous lock box [660,280,760,400] is near the opening of P038 and does not locate this G clef. Suggested replacement box [900,280,970,430] uses page coordinates; system 6 starts at page y=0.

Required repair: retain all bar boundaries and capacities; move effective G clef to P039 onset 0, with its printed glyph represented at P038 end (onset 2). Update the three framing documents consistently, rebuild affected dependent evidence and hashes, and obtain new authorization for the revised handoff. The prepared run is unchanged by this review.

## Print observations retained before the mandatory stop

Three printed pages (45–47), five piano systems per page. Opening is 2/4 with one flat and G2/F4 clefs; printed tempo is Vigoroso con forza, quarter=126. Two-flat signature begins at system 6; one flat returns at system 9. No printed meter change was observed in the page overview. The locked system counts are 6,7,7,7,7 / 8,8,9,6,6 / 6,6,7,9,8 = 107, but this checkpoint does not certify every region or capacity.

Visible route features include first/second endings on systems 2 and 5, forward repeats at systems 3 and 6, a backward repeat at system 6 end, an internal forward repeat after the first region of system 7, first ending at the end of system 8 and second ending at system 9 start, the word Coda at system 14, and the final barline at system 15. In particular, the system-5 first-ending bracket visually starts over P032 and spans P033; the system-8 bracket starts over P058 and spans P059. Full route audit is not complete.

The pages contain dynamics, accents/marcato, slurs, ties, hairpins, pedal depress/release marks, Coda text, and crescendo text; their complete addressed inventory is NOT frozen as complete. Fingerings were excluded. The mandatory clef/frame stop takes precedence over continuing the full inventory. No conclusions from reader agreement, candidate structure, provenance, model confidence, or validation were used.

## Resume condition

A repaired and rehashed prepared frame with a fresh matching authorization is required. Resume with a new independent Phase 1 checkpoint; do not advance to Phase 2 from this blocked checkpoint. human_outcome remains null. No final delivery exists.
