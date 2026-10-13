# ERRATUM 002 — frozen before application

Upper phrase slurs on a chord attach to its highest printed pitch, rather than the first serialized chord member. This clarifies exact attachment without changing any note, timing or phrase span. Exact changes follow.

Slur numbers must also be unique while open in MusicXML document order: allocation only by musical time can reuse a number in an earlier serialized voice before a later voice has closed it in the same measure. Allocate against document-order intervals. This is a serialization correction only.

```json
[
  {
    "slur_id": "SL002",
    "endpoint": "start",
    "bar": 3,
    "before": "A-P003-r1-q3_2-n1",
    "after": "A-P003-r1-q3_2-n2",
    "printed_pitch": "E5",
    "evidence": "print_system_1.png",
    "confidence": "high"
  },
  {
    "slur_id": "SL006",
    "endpoint": "start",
    "bar": 11,
    "before": "A-P011-r1-q3_2-n1",
    "after": "A-P011-r1-q3_2-n2",
    "printed_pitch": "E5",
    "evidence": "print_system_2.png",
    "confidence": "high"
  },
  {
    "slur_id": "SL019",
    "endpoint": "start",
    "bar": 32,
    "before": "A-P032-r1-q3_2-n1",
    "after": "A-P032-r1-q3_2-n2",
    "printed_pitch": "E5",
    "evidence": "print_system_4.png",
    "confidence": "high"
  },
  {
    "slur_id": "SL023",
    "endpoint": "end",
    "bar": 45,
    "before": "A-P045-r1-q0-n1",
    "after": "A-P045-r1-q0-n2",
    "printed_pitch": "C5",
    "evidence": "print_system_5.png",
    "confidence": "high"
  },
  {
    "slur_id": "SL024",
    "endpoint": "end",
    "bar": 46,
    "before": "A-P046-r1-q0-n1",
    "after": "A-P046-r1-q0-n2",
    "printed_pitch": "A4",
    "evidence": "print_system_5.png",
    "confidence": "high"
  }
]
```

Human outcome: null.
