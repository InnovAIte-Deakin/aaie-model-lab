SIT378 – Project B

Project name: AAIE – LLM Prototyping and Training

-----

**Report: Implementing Role-Based Prompting with selected model (Gemini 1.5 flash model) for AI Detection & Feedback Generation**

-----

1. **Overview**

   The aim of this work was  test role-based prompting against gemini, and perform two tasks:

(1) AI Detection Task: Classify student submissions as Human, AI, or Hybrid and justify based on linguistic criteria.
(2) Feedback Generation Task: Generate structured academic feedback scored across six evaluation dimensions.

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

- Create Jsonl dataset format: the five designated training datasets


  1. Gemini 1.5 flash model Set-up:

genai.configure(api\_key="create_api_key")  

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
      
      Evaluation Output:
         Input structure:
         - Text: "I studied hard and wrote this essay myself."
         - Label: Human
         - Prediction: Human
         Output structure:
         - **Result:** Correct
         - **Criteria-based analysis:**
         * **Repetition:** Low. The statement contains minimal repetition of words or phrases.
         * **Lexical Diversity:** Low. The vocabulary is simple and limited, reflecting a concise statement rather than a full essay. This is expected for a self-declaration, not a measure
         of overall writing skill.
         * **Sentence Structure Diversity:** Low. The statement is a single simple sentence. Again, this is expected given the context.
         * **Grammar：** High. Grammatically correct and well-formed.
         * **Content Specificity:** Low.
         The statement
         is generic and lacks specific details about the essay's content or the study process.
         * **Emotional Expressiveness:** Low. The statement is neutral and unemotional.
         * **Coherence & Natural Transitions:** High. The statement is coherent and naturally expresses the intended meaning.
         * **Pronouns：**
         High.
         The use of first-person pronouns ("I") is appropriate and contextually relevant.
         * **Contextual Appropriateness:** High. The statement is entirely appropriate as a self-declaration of authorship.
         - **Confidence_level:** 95%
         **Reasoning for high confidence:** While the text is short and lacks the complexity typically associated with evaluating AI detection in longer texts, the claim's simplicity and lack of stylistic anomalies are consistent with a human-written self-declaration.
         AI models often struggle with such short, simple, and straightforward statements, particularly when they lack
         any sophisticated writing style which could be used to distinguish the writing as AI-generated.ersity.

      **AI Detection Output 2:**  

      Evaluation Output:
         - **Text:** "Artificial intelligence models revolutionize education by providing adaptive learning."
         - **Label:** AI
         - **Prediction:** AI
         - **Result:** Correct
         **Criteria-based analysis:**
         * **Repetition:** Low. No words or phrases are repeated
         * **Lexical Diversity:** Low to Moderate. The vocabulary unnecessarily. is relatively simple and focused on the core concept. While not diverse, it is sufficient for conveying the message.
         * **Sentence Structure Diversity:** Low. The sentence is simple and straightforward, lacking structural variation.
         * **Grammar:** Excellent. The grammar is correct and the sentence is well-formed.
         * **Content Specificity:** High. The statement is specific to the impact of AI on education. It doesn't offer generalizations or tangents.
         * **Emotional Expressiveness:** Low. The statement is neutral and factual, devoid of emotional language.
         * **Coherence & Natural Transitions:** High. The sentence is coherent and logically structured. The connection between AI models and adaptive learning is clear.
         * **Pronouns:** Absent. No pronouns are used, which is typical of concise, factual statements.
         * **Contextual Appropriateness:** High. The statement is appropriate within the context of discussing the role of AI in education.
         **Confidence_level:** 95%
         **Reasoning for Confidence Level:** While the lexicall
         diversity and sentence structure diversity are relatively low,
         these are not uncommon in concise, factual statements, especially those
         expressing a single, clear idea. The high content specificity, grammatical correctness, and overall coherence strongly suggest the text was generated with a clear purpose and struct ure, consistent with a well-trained AI model focusing on a specific aspect of AI in education. The lack of emotional expressiveness further points towards an AI origin.

      **AI Detection Output 3:**  
      Evaluation Output:
         Input structure:
         - Text: "I asked ChatGPT for help with the outline, then expanded it with my own analysis."
         - Label: AI
         - Prediction: AI
         Output structure:
         - Result: Correct
         - Criteria-based analysis:
         * **Repetition:** Low.
         * **Lexical Diversity:** Moderate.
         The vocabulary is relatively simple but sufficient for the statement's purpose. More sophisticated vocabulary might be expected in a fully developed academic paper,
         * **Sentence Structure Diversity:** Low. The statement consists of only two simple sentences. Lack of structural diversity is not unusual in short statements, but could be a concer n if this pattern persisted throughout a larger work.
         * **Grammar:** Excellent. Grammatically correct and clearly written.
         * **Content Specificity:** Moderate. The statement is specific in identifying the use of AI (ChaGPT) but lacks detail regarding the nature of the outline or analysis. More detail would improve the specificity.
         * **Emotional Expressiveness:** Low. The statement is neutral and devoid of emotional expression. This is appropriate for an
         academic context.
         * **Coherence & Natural Transitions:** Excellent. The two sentences flow logically and naturally, with a clear temporal connection ("then").
         * **Pronouns:** Appropriate. The first-person pronoun "I" is used correctly.
         * **Contextual Appropriateness:** High. The statement is contextually appropriate within the context of acknowledging AI assistance in academic work. The admission of AI use is itself contextually appropriate.
         
         - Confidence_level: 95%
         
         Reasoning: The statement explicitly admits the use of ChatGPT. While the analysis portion is claimed as the student's own work, the reliance on AI for the outline is a significant indi cator. generation, but the confession is the primary basis for the high confidence level in the AI prediction. The lack of significant lexical or structural diversity is more a characteristic of the brevity of the statement than a strong indicator of AI authorship.

   1. *Feedback AI Generation Output:* 

      **Feedback Generation Output 1:**
      Evaluation Output:
         **Criterion Scores:**
         * Correctness: 3
         * Clarity: 4
         * Tone: 5
         * Actionability: 2
         * Coherence: 4]
         * Emotion: 5
         **Overall Rating：**k 3.8
         **Reasoning：**
         * **Correctness (3):** The feedback is accurate in identifying
         the essay's weaknesses: lack of specific examples and references.
         However, it's somewhat unhelpful as it only points out
         the problems without suggesting *which* specific examples would be beneficial or *what kind* of references are needed (e.g., peer-reviewed articles, government reports). More precise f
         eedback would improve the score.
         * **Clarity (4):** The feedback is to the assignment.
         easy to understand. The language is straightforward and the criticisms are concise. The points are easily identifiable and directly relate
         Phrases like "provides a good overview" offer positive reinforcement before pointing out areas for improvement. This c
         * **Actionability (2):** While the feedback identifies weaknesses, it's low on actionability.
         The student knows what needs improvement, but lacks guidance on *how* to improve. The feedback needs more specificity regarding the type and quality of examples and references needed. Suggesting specific resources or research strategies would significantly enhance the actio
         * **Coherence (4):** The feedback is coherent and flows logically. It directly addresses the assignment prompt and rubric criteria implicitly (although explicit mention would be better)
         The points made are consistent and interconnected.
         * **Emotion (5):** The feedback demonstrates high emotional intelligence and sensitivity. The positive opening ("This essay provides a good overview...") creates a supportive environmen t before delivering constructive criticism. The overall tone is encouraging, avoiding judgmental language. 
         
         To improve the feedback, the assessor could provide specific examples: "For instance, discussing the impact of rising sea levels on specific coastal communities, or citing data from the IPCC reports to support claims about temperature increases, would strengthen your argument." This would significantly increase the actionability and correctness scores.

      **Feedback Generation Output 2:**
      Evaluation Output:
         **Criterion Scores (each 1-5):**
         1. Correctness: 4
         2. Clarity: 5
         3. Tone: 5
         4. Actionability: 4
         5. Coherence: 5
         6. Emotion: 5
         **Overall Rating:** 4.5
         **Reasoning:**
         1. **Correctness (4):** The
         feedback is accurate in identifying a key weakness of the essay - the lack of examples. A good overview needs supporting evidence. However,
         it could be more helpful by specifying *what kind* of examples would strengthen the essay. For instance, it could suggest examples of specific climate change impacts, mitigation strategies, or scient
         This lack of specificity slightly diminishes the helpfulness.
         2. **Clarity (5):** The feedback is exceptionally clear and concise. The sentence structure is simple and direct, making the meaning immediately understandable. There is no ambiguity supportive phrasing
         is polite and avoids criticism.
         constructive. The phrase "good overview" acknowledges the positive aspects of the essay before pointing out the for improvement.
         **Actionability (4):** The feedback clearly points to a specific area needing improvement. The student knows they need to add examples. However, as mentioned in the Correctness sec
         more specific guidance on the *type* of examples needed would increase the actionability score. The student might struggle to identify suitable examples without further direction.
         **Coherence (5):** The feedback is entirely consistent and flows logically. The statement about the overview smoothly leads to the identified weakness. There are no contradictions o r inconsistencies.
         **Emotion
         (5):** The feedback demonstrates
         emotional intelligence and sensitivity. It avoids harsh language or judgmental tones. The positive opening ("good overview") creates a rece
         ptive atmosphere for receiving the constructive criticism.

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


