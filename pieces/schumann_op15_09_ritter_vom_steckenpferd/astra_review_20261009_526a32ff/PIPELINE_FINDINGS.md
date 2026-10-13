# Stage 5 findings

CONSUMER-CLEF-P001 resolves with the current openingClefRendering adapter. The historical reproduction harness lacked this new adapter, so the new workspace scripts were updated to follow the current ScoreViewer adapter sequence before testing. Production code was not edited. Current consumer files are SHA-256 bound.

Primary structural, playback, mapping, VexFlow timing, essential notation and focused visual gates pass. CORE and MARKS application pass. ROUTE Apply still makes the implicit opening explicit; exact printed roundtrip is blocked separately and the applied output must not replace the primary. Unison ambiguity at P007/P019 remains for final human verification. The fixed-width screenshot clips the overlong duplicate diagnostic title; musical notation remains visible.
