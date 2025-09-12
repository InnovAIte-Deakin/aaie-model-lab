# Evaluation of Gemini 1.5 Flash

**Author:** Qasim Nasir  
**Student ID:** 223282352  

---

## Model Description
Gemini 1.5 Flash is Google’s fast, lightweight multimodal model distilled from 1.5 Pro. It is designed for high-volume, low-latency workloads such as chat, summarization, captioning, and document/table extraction. It supports long context understanding across text, images, audio, video, and PDFs via the Gemini API and Vertex AI.  

The model emphasizes speed and cost efficiency with minimal quality trade-offs, making it suitable for production applications that do not require the highest reasoning capabilities of the Pro model but benefit from scalable multimodal I/O and extended context handling.

---

## Gemini API Key
- Obtain a Gemini API key via [Google AI Studio](https://ai.google/studio) and store it securely as an environment variable.  
- Use the key with the Gemini API/SDKs (`apiKey` or `x-goog-api-key`) to call Gemini 1.5 Flash; quickstart snippets are available in the documentation.  
- For enterprise-level deployment, use Vertex AI for managed access and billing controls.

---

## Use in AAIE
The model was tested using the same pipeline and dataset structure as other models:

- **Datasets:** `engineering.json`, `accounting.json`, `it.json`, `psychology.json`, `teaching.json`  
- **Prompting Technique:** Chain of Thoughts prompting (step-by-step reasoning)  
- **Output Captured:** `[DETECTION]` and `[FEEDBACK]` blocks in plain text  

This ensured a like-for-like comparison across models.

---

## AI Detection Task Evaluation

The AI detector achieved high accuracy, performing best in Psychology and Teaching, and weakest in Accounting and IT. Overall accuracy across the five domains was **86.7%**.

| Domain                     | Total Submissions | Correct Predictions | Wrong Predictions | Accuracy (%) |
|----------------------------|-----------------|-------------------|-----------------|--------------|
| Engineering  | 6               | 6                 | 0               | 100.0        |
| Accounting                 | 6               | 4                 | 2               | 66.7         |
| Information Technology     | 6               | 4                 | 2               | 66.7         |
| Psychology                 | 6               | 6                 | 0               | 100.0        |
| Teaching                   | 6               | 6                 | 0               | 100.0        |
| **Overall**                | 30              | 26                | 4               | 86.7         |

### Interpretation
- **Engineering:** Perfect accuracy; AI, Human, and Hybrid predictions matched true labels.  
- **Accounting:** Two errors where Hybrid submissions were predicted as AI.  
- **IT:** Errors occurred in Human/Hybrid cases.  
- **Psychology & Teaching:** Full accuracy, indicating strong domain performance.

---

## Feedback Generation Task – Human Evaluation

Human raters evaluated feedback on correctness, clarity, tone, and actionability. Overall, scores were **Good** across domains.

| Domain                  | Correctness | Clarity | Tone  | Actionability | Overall Avg |
|-------------------------|------------|--------|------|---------------|-------------|
| Engineering             | 4          | 4      | 5    | 3–4           | 4 (Good)    |
| Accounting              | 4          | 4      | 4    | 3             | 4 (Good)    |
| Information Technology  | 4          | 4      | 4–5  | 3             | 4 (Good)    |
| Psychology              | 4          | 4      | 4    | 3             | 4 (Good)    |
| Teaching                | 4          | 4      | 4    | 2–4           | 4 (Good)    |
| **Overall Average**     | 4          | 4      | 4–5  | 3–4           | 4 (Good)    |

### Interpretation
- **Strengths:** Accurate, clear, constructive feedback; strong tone and clarity.  
- **Weaknesses:** Accounting and IT feedback had limited depth; some guidance lacked specific examples or risk analyses.  
- **Consistency:** Feedback followed a standardized rubric with coherent flow and professional, encouraging tone.  

---

## Overall GenAI Rubric Rating
- **Correctness (Accuracy & Helpfulness):** Good to excellent, domain-appropriate terminology, minor depth limitations in Accounting/IT.  
- **Clarity (Understandability & Communication):** Good to excellent, occasional structural suggestions.  
- **Tone (Supportiveness & Constructiveness):** Excellent, consistently professional and encouraging.  
- **Actionability (Clear Next Steps):** Average to good, with repeated prompts for specificity.  
- **Coherence (Consistency & Flow):** Good, standardized rubric structure ensures consistent logic.  
- **Emotion (Sensitivity & Encouragement):** Good, affirming strengths while offering constructive guidance.  

---

## Recommendations
- Short answer: Yes, select GPT-4.1 as the leading candidate for AAIE’s Phase 1 detection & feedback.
---

## Advantages
- Fast and lightweight; suitable for high-volume workloads.  
- Multimodal capabilities (text, image, audio, video, PDFs) with extended context handling.  
- Cost-effective and scalable for production applications.  
- High accuracy in domains with strong training representation (Engineering, Psychology, Teaching).  
- Professional and supportive feedback tone across domains.  

---

## Limitations
- Slightly lower AI detection accuracy in Accounting and IT domains.  
- Actionability of feedback is moderate in some areas, requiring deeper examples or risk analyses.  
- Does not reach the reasoning depth of Gemini 1.5 Pro, so not ideal for highly complex tasks.  
- Requires careful prompt design (e.g., Chain of Thought) to achieve optimal results.  

