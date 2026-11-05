# Local GIF walkthrough

Captured November 5, 2026 from the actual standalone DraftLoop application on
localhost. The recording shows entering the [original synthetic essay](../data/synthetic-walkthrough.json),
receiving rubric feedback, and selecting **Next AP Point** to request revision advice.
No student writing or released AP essay text is shown.

- Provider/model: installed local Ollama `llama3.2:3b`, `CLASS_25` mode.
- The native app code and scoring rules were not changed for the recording.
- A temporary local SQLite database was used; no cloud database or hosted model was used.
- Displayed rubric: A 1/1, B 3/4, C 1/1; total 5/6. No human reference score exists.
- The displayed 3–6 range is a heuristic, not a calibrated confidence interval.
- Frames were captured at 1280×720 and encoded as a looping 960×540 GIF using FFmpeg.
- The clip is edited from five real interface states. Reading pauses are inserted and
  model wait time is compressed; this is not an inference-speed measurement.
- This capture is separate from the November 4 screenshot and the November 3
  three-essay experiment. No evaluation result or historical fixture was changed.

The same synthetic input can produce different feedback on another run. The model's
suggestions require writer/teacher judgment; showing a complete response does not
validate the score or advice.

[Watch the GIF](assets/local-coach-demo.gif) · [Static November 4 capture](assets/local-coach.jpg) · [Project overview](../README.md)
