# Stage 5 consumer recheck

Technical recheck PASS. Primary XML and completed Phase 1–3 evidence remain byte-exact from astra_review_20261012_6f8cf1fd. Original musical review attribution and frozen corrections are retained. This job owns the consumer recheck only.

The cross_staff_chord.v1 production profile passed at widths 1400, 1350, 1000 (zoom 0.9), and 900. Each layout retains 604 note/rest members, 60 ordinary beams, matching staff/voice/onset/duration/pitch, and passing cursor mapping. All four screenshots were visually inspected; A3 is now on staff 2 at P008/P012/P024/P044/P056. See validation/consumer_recheck/.

PROPER, independent playback (540 attacks), CORE/MARKS/ROUTE roundtrips and other completed gates are retained under the consumer-only recheck contract; their frozen evidence is unchanged. Current rendering, staff geometry and cursor regressions were independently rerun. No musical or primary XML changes were made. Historical blocked reports are preserved as history and superseded by the new gate evidence in FINAL_FREEZE.json.

The delivery remains UNVERIFIED pending human musical verification. Unresolved questions in [human_attention.json](human_attention.json):

- G3-STEM-P007: Does the extra downward stem on G3 prescribe a separately sustained inner voice, and if so its exact endpoint?
- G3-STEM-P023: Does the extra downward stem on G3 prescribe a separately sustained inner voice, and if so its exact endpoint?
- G3-STEM-P055: Does the extra downward stem on G3 prescribe a separately sustained inner voice, and if so its exact endpoint?
- OVERLAPPING-ARCS: Confirm the lower same-pitch curved span belongs to the moving voice while the upper curve ties into the sustained voice.
