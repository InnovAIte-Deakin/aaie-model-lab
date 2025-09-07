# Phase 1 Model Selection: Gemini 1.5 Pro

This script uses **Google Gemini (via `google-generativeai`)** to evaluate multiple student submissions.  
It provides two types of analysis for each submission:

1. **Academic Integrity Detection** — classifies the text as Human, AI, or Hybrid.  
2. **Rubric-Aligned Feedback** — generates structured feedback aligned to a provided rubric.  

The script ensures **plain-text outputs only** (no JSON), making results easy to review and include in academic reports.

---

## Workflow Overview

1. **Setup Environment**  
   - Installs `google-generativeai >= 0.7.2`.  
   - Imports dependencies (`os`, `json`, `textwrap`, etc.).  
   - Loads `GEMINI_API_KEY` securely from environment or user input.  
   - Configures Gemini API access.  

2. **Load Datasets**  
   - Loads JSON files such as `teaching.json`, `psychology.json`, `it.json`, etc.  
   - Each dataset must contain:
     - `domain`: subject area (e.g., IT, Education).  
     - `prompt`: assignment question given to students.  
     - `rubric`: structured grading rubric with criteria + performance descriptors.  
     - `submissions`: list of student answers.  

3. **Rubric Conversion**  
   - `rubric_to_text()` flattens rubric JSON into readable text.  
   - Includes:
     - `rubric_id`  
     - Each `criterion_id`, `name`, and `description`  
     - Any `performance_descriptors` (e.g., Excellent, Good, Poor).  

4. **Prompt Builders**  
   Two helper functions build structured prompts for Gemini:  

   - **Detection Prompt** (`build_detection_prompt`)  
     - Uses few-shot examples (1–2 previous submissions) when available.  
     - Guides Gemini to classify as:
       ```
       Label: Human | AI | Hybrid
       Rationale:
       - point 1
       - point 2
       Flags: style_inconsistency / high_verbatim / generic_phrasing / none
       ```

   - **Feedback Prompt** (`build_feedback_prompt`)  
     - Supplies the rubric, domain, assignment prompt, and submission.  
     - Expected output format:
       ```
       Overall Summary: 2–4 sentences

       Criteria Feedback:
       Criterion: <criterion_id>
       Rating: Excellent | Good | Average | Needs Improvement | Poor
       Evidence:
       - bullet point(s)
       Improvement Tip: one concrete suggestion

       Overall Rating: Excellent | Good | Average | Needs Improvement | Poor
       ```

5. **Gemini API Call**  
   - `call_gemini()` handles communication with Gemini.  
   - Merges `system` role instructions into the first `user` message (Gemini doesn’t support system role).  
   - Converts messages into Gemini’s `parts` format.  
   - Calls the model with `model.generate_content()`.  
   - Returns plain text outputs.  

6. **Runner (`run_all()`)**  
   - Iterates through each dataset file.  
   - For every submission:
     - Builds a **detection prompt** → calls Gemini → saves detection result.  
     - Builds a **feedback prompt** → calls Gemini → saves feedback result.  
   - Collects all results into a structured list.  


