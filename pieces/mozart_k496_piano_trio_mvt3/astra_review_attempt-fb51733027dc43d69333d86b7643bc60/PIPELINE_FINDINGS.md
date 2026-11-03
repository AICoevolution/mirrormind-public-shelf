# Pipeline findings — revision03

The primary passes PROPER; no broken engraving publication_findings remain. The odd voice-phantom finding at piano bar61 reflects a continuous line crossing staves between complete beam groups. Its note membership and all four visual layouts were checked.

Barline container ordering caused the production viewer to carry repeat state to the final bar. Host-released revision02 used the authorized normalize_measure implementation on 24 part/measure targets. It retained every barline child and all non-target measures. Print endings, independent route, playback, and all four final layouts agree; no final repeat dots remain.

Out-of-order beam children (4,1,2,3) on two bar105 violin notes created a stray flag. Host-released revision03 sorts unchanged children (1,2,3,4). All four final renders match the source beam grouping and hooks.

CORE Apply is byte-exact. Standalone CORE rebuild has narrower fidelity than full XML: only sounding-event equivalence after tie ordering normalization is asserted. MARKS Apply normalizes slur numbers/order at32 notes, despite preserving protected ornaments, technical/fingering, arpeggiation and ties. DELIVERY-SEP-MARKS remains LIMITED; never replace the primary with diagnostics.

The viewer places legato at bar37 into the repeat line and crowds Tempo primo./VAR. VI at bar122. Both remain readable; explicit delivery issues VISUAL-P037-LEGATO and VISUAL-P122-LABELS retain REVIEW_REQUIRED. These are not publication approval.

The final visual comparison also identifies ordinary source uncertainty about the lower-piano slur start at151/152. Keep SLUR-P151-P152-S4-START open; the encoded earlier start is provisional. Existing grace-realization, fingering33, slur98/99 and metadata questions remain visible. No audit evidence was rewritten to hide this qualification.
