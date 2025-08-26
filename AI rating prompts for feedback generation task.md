Project: AAIE – Artificial Assessment Intelligence for Education

Week 6: Generative AI Rating Criteria Task

Activity: Model Development. [Planner - Generative AI Rating Criteria](https://teams.microsoft.com/l/entity/com.microsoft.teamspace.tab.planner/mytasks?tenantId=d02378ec-1688-46d5-8540-1c28b5f470f6&webUrl=https%3A%2F%2Ftasks.teams.microsoft.com%2Fteamsui%2FpersonalApp%2Falltasklists&context=%7B%22subEntityId%22%3A%22%2Fv1%2Fassignedtome%2Fview%2Fboard%2Ftask%2FGm-KKFL6cECuk7MdRUObD8gAL6Ck%22%7D)

**Objective: AI rating prompts for feedback generation task**

Prompt evaluation should include explanation: using LLM-based judge that not only rates outputs (pass/fail or scalar rating) but also provides reasoning based on evaluation criteria which gives insight into why a response passes or fails.

*Part 1: Evaluation Rubric*

- **Rating:** score from 1 to 5 (from poor/not relevant to excellent/very relevant)
- **Reasoning:**
1. Correctness: Does the feedback accurately identify errors and provide valid advice?
- Score 1 (Completely incorrect): Misidentifies, misleading or wrong advice.
- Score 2 (Mostly incorrect with minor truth): Suggests something irrelevant or wrong, but may contain a small partially correct hint.
- Score 3 (Partially correct): Identifies some correct issues, but misses key points or mixes correct and incorrect statements.
- Score 4 (Mostly correct but not fully precise): Gets the core issue right but overlooks minor details or nuances.
- Score 5 (Fully correct): Accurately diagnoses the issue with no factual errors, precise advice.
1. Clarity: Is the explanation easy to understand?
- Score 1(Completely unclear): Very confusing, vague, or ambiguous.
- Score 2 (Low clarity): understood with effort, but contains vague wording or awkward phrasing.
- Score 3 (Moderately clear): Generally understandable, but not well structured, slightly wordy or imprecise.
- Score 4 (Clear but not optimal): Clear and readable but could be more concise, polished, or better structured.
- Score 5(Perfectly clear): Concise, unambiguous, easy for the student to understand.
1. Tone: Is the feedback supportive and professional?
- Score 1(Inappropriate): Negative, discouraging, or disrespectful.
- Score 2(Weakly supportive): Neutral but cold, lacks encouragement.
- Score 3(Acceptable or Neutral): Professional but not warm, neither encouraging nor discouraging.
- Score 4(Supportive but not strong): Friendly and helpful, but could be more encouraging.
- Score 5(Excellent tone): Fully constructive, encouraging, motivating, respectful.
1. Actionability: Does the feedback provide concrete next steps?
- Score 1(Inappropriate): Negative, discouraging, or disrespectful.
- Score 2(Weakly supportive): lacks encouragement, 
- Score 3 (Acceptable or Neutral): neither encouraging nor discouraging.
- Score 4 (Supportive but not strong): Friendly and helpful
- Score 5 (Excellent tone): Fully constructive, encouraging, motivating, respectful.

*Part 3: Few-shot prompting:*

**Goal:** the model rate student feedback from 1–5 across four criteria (Correctness, Clarity, Tone, Actionability), provide reasoning, and give an overall rating.

**Format:**

{  "Label": "AI" | "Human",  

`   `"Confidence": "<0-100>",  

`   `"Reasoning": {    

"Stylistic fluency": "...",    

"Repetition patterns": "...",    

"Specificity": "...",    

"Complexity balance": "...",    

"Topical coherence": "..."  

}

}

- Bad feedback: Rating = 1
- Good feedback: Rating = 4.
- Excellent feedback: Rating = 5.
- A feedback rated 2 must include reasoning like "Identifies a problem but is vague (improve referencing) and does not explain how."

**Example:**

{  "Overall\_Rating": "4",  

`    `"Criterion\_Ratings": {    

"Correctness": "4",    

"Clarity": "4",    

“Tone": "4",    

"Actionability": "4"},  

`      `"Reasoning": {    

"Correctness": "Correctly identifies issue with paragraph structure.",    

"Clarity": "Clear feedback, easy to understand.",    

"Tone": "Supportive but not overly detailed.",    

"Actionability": "Provides direction (improve organization) but lacks specific examples."}

}

- Correctness (4): Yes, organization is a valid critique, but not pinpointed in detail.
- Clarity (4): Clear and understandable, but not deeply elaborated.
- Tone (4): Constructive and professional.
- Actionability (4): Actionable (reorganize paragraphs), but not specific about how.

*Part 2: Use Cases:*

- Case 1 (Strong Feedback): 

  **Prompted Feedback:** “Explained idea clearly, but missing cites and key sources. To solve, adding some references resources in this essay to support your research”

  **Expected JSON output:**

  {  "Overall\_Rating": "5",  

  `    `"Criterion\_Ratings": {    

  "Correctness": "5",    

  "Clarity": "5",    

  "Tone": "5",    

  "Actionability": "5"  

  },  

  `     `"Reasoning": {    

  "Correctness": "Feedback accurately identified the missing reference.",    

  “Clarity": "The explanation was concise and clear.",    

  "Tone": "Tone was supportive and professional.",    

  "Actionability": "Suggested a specific fix with source reference."}

  }

- Case 2 (Neutral Feedback):

**Prompted Feedback:** "You should work on your essay. It's not very strong in referencing."

**Expected JSON output:**

{  "Overall\_Rating": "3",  

`    `"Criterion\_Ratings": {    

"Correctness": "3",    

"Clarity": "3",    

"Tone": "3",    

"Actionability": "2"  

},  

`    `"Reasoning": {    

"Correctness": "Feedback identified a referencing issue but was vague.",    

"Clarity": "Message was understandable but not precise.",    

"Tone": "Neutral tone, not very supportive.",    

"Actionability": "Did not provide a specific way to fix the issue.”}

}

- Case 3 (Weak Feedback): 

  **Prompted Feedback:** "Your essay doesn’t match with main topic. Please fix it as soon as possible."

  **Expected JSON Output:**

  {  "Overall\_Rating": "1",  

  `    `"Criterion\_Ratings": {    

  "Correctness": "1",    

"Clarity": "1",    

"Tone": "1",    

"Actionability": "1"  

},  

`     `"Reasoning": {    

"Correctness": "Feedback gave no accurate or useful information.",    

"Clarity": "Message was vague and unhelpful.",    

"Tone": "Harsh and discouraging tone.",    

"Actionability": "No concrete steps were suggested."}

}




