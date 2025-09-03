# My Observation

The detector performs barely above chance with given data and base prompts 16/30 correctness, 53.3%. Feedback generation is fundamentally unreliable, with format violations, truncation, rubric regurgitation, and a 1/5 rating, which disqualifies it for formative or summative feedback use.
## Detection quality
- 16/30 correct and 14/30 wrong, revealing systematic weaknesses rather than random noise.
- Hybrid recognition is inconsistent, with frequent collapses into Human or AI, indicating the model fails to capture nuanced AI-assisted writing patterns.
## Domain behavior
- Teaching and Accounting consistently drag down accuracy, with frequent AI→Human mislabels and confused Hybrid handling that skew results.
- This variability signals domain sensitivity and weak transfer, which is risky for broad deployment in education.
## Confidence and risk
- Wrong answers often come with “High confidence,” showing miscalibration between certainty and correctness that can mislead instructors and systems.
- Overconfidence is most damaging on AI→Human errors, masking the detector’s blind spots and inflating trust in incorrect outcomes.
•	Such calibration issues require either model retraining or explicit post-hoc calibration before any production use.
## Feedback generation
- The model fails to produce structured, rubric-aligned feedback, instead echoing rubric text, breaking format, and truncating outputs mid-stream.
- Ratings of 1/5 for feedback and 2/5 for detection reflect systemic capability gaps, not just prompt hygiene problems.
- This behavior makes it unsuitable for learner-facing feedback or grading support without heavy human editing.

