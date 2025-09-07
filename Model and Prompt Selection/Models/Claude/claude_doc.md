# Phase 1 Model Selection: Claude-3.5-haiku

This script evaluates multiple student submissions against two dimensions:
1. **Academic Integrity Detection** — classifies text as Human, AI, or Hybrid.
2. **Rubric-Aligned Feedback** — provides detailed criterion-based feedback.

It uses **Anthropic Claude models** via the **OpenRouter API** and outputs structured, plain-text results.

---

## Overview of Steps

1. **Setup**  
   - Install and import dependencies (`requests`, `json`, etc.).  
   - Securely load the `OPENROUTER_API_KEY`.  
   - Define model and endpoint (`anthropic/claude-3.5-haiku` by default).  

2. **Load Datasets**  
   - Input JSON files (`teaching.json`, `psychology.json`, `it.json`, etc.).  
   - Each JSON contains:
     - Domain (e.g., IT, Education)  
     - Assignment prompt  
     - Rubric (criteria + performance descriptors)  
     - Student submissions  

3. **Rubric Processing**  
   - `rubric_to_text()` flattens rubric JSON into readable text.  
   - Includes `rubric_id`, criterion names, descriptions, and performance descriptors.  

4. **Prompt Construction**  
   - **Detection Prompt** (`build_detection_prompt`)  
     - Uses 1–2 example submissions as few-shots.  
     - Asks the model to output:  
       ```
       Label: Human | AI | Hybrid
       Rationale:
       - bullet point
       - bullet point
       Flags: style_inconsistency / high_verbatim / generic_phrasing / none
       ```
   - **Feedback Prompt** (`build_feedback_prompt`)  
     - Provides domain, assignment prompt, rubric text, and submission.  
     - Expected output includes:  
       1. Overall Summary  
       2. Criteria Feedback (criterion, rating, evidence, improvement tip)  
       3. Overall Rating  

5. **Model Call**  
   - `call_claude_openrouter()` sends prompts to OpenRouter’s `/chat/completions` endpoint.  
   - Returns plain-text outputs (no JSON).  
   - Handles errors and joins segmented responses if needed.  

6. **Runner** (`run_all()`)  
   - Loops through each dataset.  
   - For every submission:
     - Calls detection + feedback prompts.  
     - Stores outputs with submission index.  
   - Returns structured results.  



