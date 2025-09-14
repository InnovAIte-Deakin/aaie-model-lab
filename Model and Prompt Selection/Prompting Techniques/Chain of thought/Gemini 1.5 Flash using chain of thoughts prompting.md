# Evaluation of Gemini 1.5 Flash  
**Author:** QASIM NASIR  
**Student ID:** 223282352  

---

## Model Description  
Gemini 1.5 Flash is Google’s fast, lightweight multimodal model distilled from 1.5 Pro, designed for high volume, low latency workloads like chat, summarization, captioning, and document/table extraction, while supporting long context understanding across text, images, audio, video, and PDFs via the Gemini API and Vertex AI; it emphasizes speed and cost efficiency with minimal quality trade offs, making it a strong default for production apps that don’t require the highest end reasoning of Pro but benefit from scalable multimodal IO and extended context handling  

---

## Gemini API key  
- Get a Gemini API key at Google AI Studio, then copy and store it securely (env var).  
- Use the key with the Gemini API/SDKs (set apiKey or x-goog-api-key) to call Gemini 1.5 Flash; quickstart snippets are in the docs.  
- On Google Cloud, use Vertex AI for managed access and enterprise controls after enabling the API and billing.  

---

## Use in AAIE  
We used the same pipeline and same dataset structure as with all the other models we tested:  
- Datasets: engineering.json, accounting.json, it.json, psychology.json, teaching.json.  
- Prompting: CHAIN OF THOUGHTS prompting (step-by-step reasoning)  
- Output captured: per submission [DETECTION] and [FEEDBACK] blocks in plain text.  

This ensured a like-for-like comparison with other models.  

---

## AI Detection Task Evaluation  
The AI detector made the most correct calls in Psychology, Engineering and Teaching, and it was weakest in Accounting and IT; overall accuracy across the five domains is 86.% based on majority labels versus true labels in the provided outputs.  

| Domain                   | Total Submissions | Correct Predictions | Wrong Predictions | Accuracy (%) |
|---------------------------|-------------------|---------------------|-------------------|--------------|
| Engineering | 6                 | 6                   | 0                 | 100.0        |
| Accounting                | 6                 | 4                   | 2                 | 66.7         |
| Information Technology    | 6                 | 4                   | 2                 | 66.7         |
| Psychology                | 6                 | 6                   | 0                 | 100.0        |
| Teaching                  | 6                 | 6                   | 0                 | 100.0        |
| **Overall**               | 30                | 26                  | 4                 | 86.7         |

**Results table**  

### Interpretation  
- **Engineering:** All six predictions matched the true labels, yielding perfect accuracy on this set (AI for submissions 1–2, Human for 3–4, Hybrid for 5–6).  
- **Accounting:** Two errors occurred where Hybrid-labeled submissions (5–6) were predicted as AI; the other four were correct, resulting in lower accuracy for this domain.  
- **Information Technology:** Two mistakes happened among Human/Hybrid cases (notably submission 4 predicted Hybrid while true label Human); the remainder were correct, giving mid-level performance.  
- **Psychology:** All six were correctly classified across AI, Human, and Hybrid cases, indicating strong domain performance on this sample.  
- **Teaching:** All six were correctly classified, including a Hybrid majority on submission 2 and Human majority on submissions 3–4 and 6, yielding perfect accuracy here as well.  

---

## Feedback Generation Task – Human Evaluation  
The human rater scores indicate consistently strong correctness, clarity, tone, and actionability across domains, with weaker depth in a few Accounting and IT items; the overall average across criteria is good to excellent, with the clearest strengths in Psychology, Teaching, and Manufacturing Engineering based on the rubric-aligned feedback provided.  

**Results table**  

| Domain                   | Correctness | Clarity | Tone | Actionability | Overall Avg |
|---------------------------|-------------|---------|------|---------------|-------------|
| Engineering               | 4           | 4       | 5    | 3–4           | 4 (Good)    |
| Accounting                | 4           | 4       | 4    | 3             | 4 (Good)    |
| Information Technology    | 4           | 4       | 4–5  | 3             | 4 (Good)    |
| Psychology                | 4           | 4       | 4    | 3             | 4 (Good)    |
| Teaching                  | 4           | 4       | 4    | 2–4           | 4 (Good)    |
| **Overall Average**       | 4           | 4       | 4–5  | 3–4           | 4 (Good)    |

### Interpretation  
- **Engineering:** Feedback is accurate, well-structured, and professional in tone, though several entries note limited depth of analysis and call for more specific examples or calculations, which slightly tempers actionability despite an overall strong showing.  
- **Accounting:** Explanations are correct and clear with relevant examples, but multiple items request deeper challenges/risks discussion and broader stakeholder analysis, lowering actionability versus other domains.  
- **Information Technology:** Narrative clarity and tone are strong, using relatable anecdotes; however, guidance often asks for specific real-world tools or exploration of risks, keeping actionability moderate.  
- **Psychology:** Definitions and links to theory are correct and clear, but mitigation strategies and real-world exemplars are frequently flagged as brief, which limits actionable next steps.  
- **Teaching:** Correct and inclusive advice with solid clarity; several entries ask to evaluate evidence-based approaches more critically and address diversity in practice with specifics, creating a mixed actionability profile.  

---

## Feedback Generation Task – Human Evaluation  
Overall, the GenAI feedback is consistently accurate, clear, constructive, and moderately actionable, with the strongest signals in Engineering, Psychology, and Teaching, and recurring suggestions to deepen examples and mitigation details in Accounting and IT; the overall GenAI rubric rating is good across criteria with supportive tone and coherent flow throughout.  

### Correctness  
- Most feedback accurately identifies strengths and gaps, using correct terminology across domains (anchoring bias, dialogic reading), with only depth-related limitations noted in Accounting and IT where more analysis is requested.  
- Human/Hybrid cases are also judged on-point conceptually, citing valid needs like case studies, stakeholder analysis, and evidence-based evaluation of approaches in Teaching and Psychology.  

### Clarity  
- Widespread mentions of “clear,” “concise,” and “logical sequence” indicate consistently high understandability and organization across submissions.  
- Occasional recommendations to add transitions, headings, or subheadings suggest small structural refinements rather than systemic clarity issues.  

### Tone  
- The tone is uniformly professional, supportive, and academic, with frequent praise for “clear, concise, and professional” language and an inclusive orientation, especially in Teaching and Engineering.  
- Guidance avoids harshness, framing gaps as growth areas with constructive “Improvement Tip” prompts.  

### Actionability  
- Each item includes concrete “Improvement Tip” directives, though many call for more specific examples, calculations, case studies, or deeper analysis, indicating moderate actionability overall and strongest where precise metrics or techniques are suggested.  
- Actionability is comparatively weaker in some Accounting and IT entries due to generic calls for more examples/risks, but still provides clear next-step themes to address.  

### Coherence  
- Feedback within each submission follows a consistent rubric structure (criterion, rating, evidence, tip), producing coherent flow and consistent evaluation logic across domains.  
- Minor flow gaps are self-identified via suggestions to add transitions between steps or sections, reinforcing internal coherence awareness.  

### Emotion  
- The feedback is respectful and encouraging, acknowledging strengths before highlighting improvements, and emphasizing inclusive practices and professional tone, especially in Teaching and Psychology.  
- Calls for deeper analysis are framed as constructive enhancements, maintaining a supportive stance throughout.  

---

## Overall GenAI Rubric Rating  
- **Correctness (Accuracy & Helpfulness):** good-to-excellent, with domain-appropriate terminology and valid diagnostics of gaps.  
- **Clarity (Understandability & Communication):** good-to-excellent, with occasional suggestions for transitions/headings.  
- **Tone (Supportiveness & Constructiveness):** excellent, consistently professional and encouraging.  
- **Actionability (Clear Next Steps):** average-to-good, with repeated but useful prompts for specificity, data, and exemplars.  
- **Coherence (Consistency & Flow):** good, standardized rubric structure ensures consistent flow.  
- **Emotion (Sensitivity & Encouragement):** good, affirming strengths and providing constructive guidance.  
- **Overall GenAI Rubric Rating:** good across domains, with standout strength in tone and clarity, and main growth area being deeper, more specific next-step guidance in Accounting and IT items.  
 

---

## Recommendations
- Gemini 1.5 Flash should be adopted for AAIR due to its speed, cost-efficiency, and strong results in most domains. However, a dual-layer strategy (Flash + Pro or Flash + reviewer for Accounting/IT) will ensure balanced accuracy and actionable feedback quality across all domains.
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

