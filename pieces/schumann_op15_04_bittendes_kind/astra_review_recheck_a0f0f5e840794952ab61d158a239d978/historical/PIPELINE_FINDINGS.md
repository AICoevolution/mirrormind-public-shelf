# Pipeline findings

Source duration success concealed substantial musical error. Missing expressive marks and missing accompaniment require direct print review even with source agreement. Seven source voice labels reduce to three musical lines via context-specific assignment; five SEP staff/voice lanes do not imply five independent voices.

ScoreAnalyzer `_merge_tied` explicitly requires temporal adjacency. P016 E4/C#4 have printed arpeggiated ties whose notated endpoints leave a gap; the primary playback re-attacks them. A consumer fix needs a narrowly justified sustain interpretation without altering displayed note values. CORE separately cannot represent the final incoming/cross-voice member ties and safely refuses Apply.

Production adapters restore all 31 cross-staff beam groups and five final tie paths. Cross-staff slur placement remains wrong relative to the source: notehead-based curves traverse the musical material. The generic essential probe reported success for the earlier XML because it checks a different fixture and does not certify these phrase arcs. Only the exact final production probe and focused visual report govern readiness here.

MusicXML mixed-staff chord serialization initially moved the upper final chord to the bass staff in OSMD. Numbered E002 uses same-voice simultaneous staff groups separated by an exact backup and restores positions without changing pitches or timing. No production code modified.
