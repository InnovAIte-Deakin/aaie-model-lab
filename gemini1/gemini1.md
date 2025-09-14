SIT378 – Project B

Project name: AAIE – LLM Prototyping and Training

-----

**Report: Implementing Role-Based Prompting with selected model (Gemini 1.5 flash model) for AI Detection & Feedback Generation**

-----

1. **Overview**

   The aim of this work was to evaluate the ability of Gemini 1.5 Flash, accessed via Google AI Studio, to perform two tasks:

1) AI Detection Task: Classify student submissions as Human, AI, or Hybrid and justify based on linguistic criteria.
1) Feedback Generation Task: Generate structured academic feedback scored across six evaluation dimensions.

The experiment was conducted with a set of test prompts and student-like submissions, focusing on academic integrity evaluation and supportive academic assessment.

1. **Methodology:**

- Model Used: Gemini 1.5 Flash (via Google AI Studio).
- Domain Focus: Academic Integrity, Education, and Environmental Science.
- Evaluation Strategy: Each prompt was submitted to the model. The generated outputs were analyzed along two dimensions:
1) AI Detection Quality: clarity of evaluation, reasoning, and recommendations for further investigation.
1) Feedback Quality: clarity, rubric alignment, and actionability of suggestions.

   1. AI Detection Criteria

- The model's classifications (Human / AI / Hybrid) were checked against markers such as:
- Repetition
- Lexical Diversity
- Sentence Structure Diversity
- Grammar
- Content Specificity
- Emotional Expressiveness
- Coherence & Natural Transitions
- Pronouns & Contextual Appropriateness
- Output Assessment: Each prediction was marked Correct or Incorrect and given a short explanation with confidence score in percentage.

  1. Feedback Evaluation Criteria:

- Feedback quality was scored on a 1–5 scale using six dimensions:
- Correctness – accurate, helpful
- Clarity – easy to understand
- Tone – supportive, constructive
- Actionability – clear next steps
- Coherence – logical flow
- Emotion – empathetic, sensitive
- Output Assessment: Each feedback was scored across criteria, averaged, and explained briefly.

1. **Implementation**

1. *Environment Set-up:*

- Selected Model: Gemini 1.5 flash
- Install SDK: pip install google-genai
- Required Jsonl dataset format: 

  {"contents":[{"parts":[{"text":"You are an academic integrity evaluator. Provide clear structured answers.\n\nSubmission: \"I studied hard and wrote this essay myself.\". Task: AI Detection."}]}]}

  {"contents":[{"parts":[{"text":"You are an academic integrity evaluator. Provide clear structured answers.\n\nSubmission: \"Artificial intelligence models revolutionize education by providing adaptive learning.\". Task: AI Detection."}]}]}

  {"contents":[{"parts":[{"text":"You are an academic integrity evaluator. Provide clear structured answers.\n\nSubmission: \"I asked ChatGPT for help with the outline, then expanded it with my own analysis.\". Task: AI Detection."}]}]}

  {"contents":[{"parts":[{"text":"You are a supportive academic assessor. Provide rubric-aligned feedback.\n\nDomain: Environmental Science. Assignment prompt: 'Discuss the causes and impacts of climate change.' Student submission: 'This essay provides a good overview of climate change but lacks specific examples and references.' Rubric: Clarity of argument; Use of evidence; Critical thinking; Writing quality."}]}]}

  {"contents":[{"parts":[{"text":"You are a careful academic assistant. Provide clear structured answers.\n\nGive feedback: 'This essay provides a good overview of climate change but lacks examples.'"}]}]}

  1. Gemini 1.5 flash model Set-up:

genai.configure(api\_key="AIzaSyBwVZ9ABILNzNixnXFb0TgbrI90r7BEH1g")  

MODEL = "gemini-1.5-flash"

1. *Role-Based Prompting:*

1) **Role 1: Academic Integrity Evaluator (AI Detection):**
- Classify label the submission whether it is Human, AI, or Hybrid
- Rational: provide evidences, the reason such as grammar, cites, or lack of research.
- Explanation: provide full detail such as what student have and what they need to improve
- Flags: summary the key points (main keys)

1) **Role 2: Supportive Academic Assessor (Feedback Generation):**
- Score submission against 6 criteria (Correctness, Clarity, Tone, Actionability, Coherence, Emotion).
- Compute Overall Rating (average): show the rating from 1 to 5, such as excellent, good, average, need improvement, and poor
- Provide feedback text and reasoning for each score.

1. *Input Submission*
- Create Jsonl file for fine tuning with selected model (Gemini 1.5 flash model)

1. **The Result**

   1. *AI Detection Output:*

      **AI Detection Output 1:**  
      <img src="https://github.com/InnovAIte-Deakin/aaie-model-lab/blob/e7ec3f79c77dacf3a13675ee355d0f66d9f290d1/gemini1/AI_detect1.png" alt="AI Detection Output 1 image" width="300"><br>

      **AI Detection Output 2:**  
      <img src="https://github.com/InnovAIte-Deakin/aaie-model-lab/blob/e7ec3f79c77dacf3a13675ee355d0f66d9f290d1/gemini1/AI_detect2.png" alt="AI Detection Output 2 image" width="300"><br>

      **AI Detection Output 3:**  
      <img src="https://github.com/InnovAIte-Deakin/aaie-model-lab/blob/e7ec3f79c77dacf3a13675ee355d0f66d9f290d1/gemini1/AI_detect3.png" alt="AI Detection Output 3 image" width="300"><br>

   1. *Feedback AI Generation Output:* 

      **Feedback Generation Output 1:**
      <img src="https://github.com/InnovAIte-Deakin/aaie-model-lab/blob/e7ec3f79c77dacf3a13675ee355d0f66d9f290d1/gemini1/Feedback1.png" alt="Feedback Generation Output 1 image" width="300"><br>

      **Feedback Generation Output 2:**
      <img src="https://github.com/InnovAIte-Deakin/aaie-model-lab/blob/ad399cbe698170006e72195ec645a1de05c40e6f/gemini1/Feedback2.png" alt="Feedback Generation Output 2 image" width="300"><br>

1. **Observation**

- **Structured Output:** Each response contained clear sections (Detection Result, Confidence Level, Justification, Recommendations). The model reliably followed the role-based prompting.
- **AI Detection:**
- Output Structure (AI Detection):
- Result: Correct / Incorrect (based on comparison of label vs. prediction).
- Criteria-based Analysis: Detailed reasoning using the markers above.
- Confidence Level: Probability estimate (%) of correct classification.
- Correctly flagged AI-like phrasing and admissions of hybrid use.
- Provided probabilistic confidence levels.
- Recommended verification methods (plagiarism checks, stylistic analysis).
- **Feedback Generation:**
- Output Structure (Feedback Evaluation):
- Criterion Scores: Each scored 1–5.
- Overall Rating: Average of scores (or adjusted in edge cases).
- Reasoning: Written justification for each score with references to text.
- Rubric-aligned, constructive, supportive.
- Direct mapping to clarity, evidence, critical thinking, and writing quality.
- **Language and Style:**
- Professional, coherent, and grammatically sound.
- Tone supportive, avoiding harsh or accusatory framing.


