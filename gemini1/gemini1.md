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
- Additionally, each output was extended with a criteria-based analysis, including:
- Confidence Level (%)
- Repetition
- Lexical Diversity
- Sentence Structure Diversity
- Grammar
- Content Specificity
- Emotional Expressiveness
- Coherence & Natural Transitions
- Pronouns & Contextual Appropriateness

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

API\_KEY = "AIzaSyBwVZ9ABILNzNixnXFb0TgbrI90r7BEH1g"

MODEL = "gemini-1.5-flash"

URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"



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

   ![](Aspose.Words.dacac0b8-64ef-4e69-aa17-91bc1227534f.001.png)

   ![](Aspose.Words.dacac0b8-64ef-4e69-aa17-91bc1227534f.002.png)

   ![](Aspose.Words.dacac0b8-64ef-4e69-aa17-91bc1227534f.003.png)

   ![](Aspose.Words.dacac0b8-64ef-4e69-aa17-91bc1227534f.004.png)

   ![](Aspose.Words.dacac0b8-64ef-4e69-aa17-91bc1227534f.005.png)


1. **Observation**

- **Structured Output:** Each response contained clear sections such as Detection Result / Confidence Level, Justification, Recommendations, and Conclusion. This consistency demonstrates that Gemini 1.5 Flash is reliable in following role-based prompts (such as academic integrity evaluator, supportive assessor).
- **Handling of Academic Integrity Detection:**
- The model effectively identified red flags such as overly generic phrasing, lack of specificity, or direct admissions of AI usage.
- It consistently recommended multi-step verification: plagiarism checks, stylistic analysis, and student interviews.
- Confidence levels were provided, which gave a probabilistic feel to the evaluation.
- **Feedback on Academic Writing:**
- The model provided rubric-aligned feedback directly mapped to Clarity, Evidence, Critical Thinking, Writing Quality.
- The feedback tone was supportive and constructive, making it appropriate for real educational settings.
- **Language and Style:**
- The generated text was grammatically correct, coherent, and professional.
- Tone remained neutral to supportive, avoiding harsh or accusatory language.


