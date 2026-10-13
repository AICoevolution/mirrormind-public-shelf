# Phase 3 frozen
All 30 physical regions, 60 staff regions, 325 candidate note elements, all marks and all route elements have been checked against actual printed pixels on all five systems. Repeated passages were individually inspected. The independent print_event_spec.json accounts for 318 pitched elements (including two grace notes) and five printed rests: 323 final elements. The two extra candidate rests in P27 are not printed. No sounding onset or duration is padded or trimmed.

The exact changes are in planned_operations.json (30 measure replacements), with 257 addressed records in phase3_review.json. complete_event_audit.json covers every candidate element, not just disagreements. All 325 candidate ledger entries match XML after normalizing rest spelling; every event has provenance. All 102 disagreement entries and all112 uncertainties were rechecked; their original alternatives remain in evidence. Provenance does not cover absent marks; coverage incorrectly omits partial_regions, and structural pairing diagnoses the wrong musical pairs. Selected P29 G4+Bb4 is wrong: E4+G4 is printed. Three sharp symbols are attached to A4 instead of C#4 in P24/P27/P28, despite pitch/alter saying A natural; consumers can change the sounding result. Restore only the printed accidental symbols, including B natural P9 and courtesy Bb P13.

No phrases/hairpins/tuplets/other ornaments exist. Restore ties in P3/P7/P12/P16, both grace slurs P20/P22, all Phase1 articulation and dynamic positions, tempo Vivace dotted-quarter100 (quarter150), and two Ped/asterisk spans. Restore exact printed beams and stem directions as planned. ROUTE already matches 1–9 twice and10–30 twice. Preserve6/8 and lower clef changes8:1.5,12:2.5,30:end2.5; designate1/9/10/30 as implicit partials without changing meter.

## Minimal topology frozen before application
V1 upper staff continuous principal line, V3 lower staff continuous line. P27 V2 is a real independent inner line: F4 eighth at0, G4 quarter at0.5 while upper F5 quarter/C5 eighth sounds. The lines join the printed F4+F5 quarter chord at1.5. Move that chord into V1; remove two unprinted filler rests. V2 ends at1.5 and has no artificial rest afterwards. Context-scoped relabeling is mandatory: old v6 changes role midbar; an indiscriminate global Map would erase genuine simultaneous independence. Old upperv5 becomesv1, lowerv15 becomesv3. No empty lane retained. P27 lower two stems point down; main F5/C5 up, joined chord down, last chord up.

No source-frame or hash blocker remains. No damaged-print ambiguity is forced into a fact. Human attention should focus on restored marks throughout, the grace slurs P20/P22, genuine inner voice P27, accidental attachments P24/P27/P28, corrected P29 chord, and both repeated partial pairs. Human outcome null; status UNVERIFIED.

Frozen SHA-256 references:
{
  "print_event_spec.json": "19ac92be6c5348fa8055e051da2e90d047f0be463f27c8400bcc4f6cd0798f2d",
  "planned_operations.json": "153f8186a9e636f87e280e03dd18c1a5f931b390bd475caeae9bde6e253753a5",
  "phase3_review.json": "f88c0c8536466b3c19c889319cfd34cad46b46b4f0e1a41666e2a0fc36429a1b",
  "complete_event_audit.json": "e002401ec44cb6055866be583456a98925dce1cf6f7a45ff8cd7cb6107ed1d2e",
  "ensemble_disagreement_recheck.json": "b524ea7f3b8bc35ad6aae1760e85cae65aeac023646a003a1bf683567a5817a0",
  "uncertainty_recheck.json": "dbd6535d3c3818a69a995102ebf740cf5aee0ed95caa67409a27e2260232ac5c",
  "phase3_hashes.json": "a7f600a66294c08e35cb65190c37b3364dfa4425539133bcef38479eb29603c2"
}
