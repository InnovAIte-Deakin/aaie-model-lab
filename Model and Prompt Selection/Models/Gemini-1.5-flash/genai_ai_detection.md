# Evaluation with GenAI for AI Detection

## Accounting.json
- **Submission_text_id: 1**  
  **Label:** AI  
  **Prediction:** AI  
  **Result:** ✅ Correct  
  **Confidence Level:** 90% (High confidence text is AI-generated)

- **Submission_text_id: 2**  
  **Label:** AI  
  **Prediction:** AI  
  **Result:** ✅ Correct  
  **Confidence Level:** 95% (Very high confidence text is AI-generated)

- **Submission_text_id: 3**  
  **Label:** Human  
  **Prediction:** Hybrid  
  **Result:** ❌ Wrong  
  **Confidence Level:** 93% (Strong confidence the text is Human-written)

- **Submission_text_id: 4**  
  **Label:** Human  
  **Prediction:** Hybrid  
  **Result:** ❌ Wrong  
  **Confidence Level:** 94% (High confidence text is Human-written)

- **Submission_text_id: 5**  
  **Label:** Hybrid  
  **Prediction:** AI  
  **Result:** ❌ Wrong  
  **Confidence Level:** 88% (High confidence text is Hybrid — AI-like fluency with domain-aware specificity)

- **Submission_text_id: 6**  
  **Label:** Hybrid  
  **Prediction:** AI  
  **Result:** ❌ Wrong  
  **Confidence Level:** 87% (Confident it is Hybrid — AI fluency with structured specificity)

**Correct Detections:**  
- AI: 2/2  
- Hybrid: 0/2  
- Human: 0/2  

**Accuracy:** `2/6 = 0.33`

---

## Engineering.json
- **Submission_text_id: 1** – ✅ Correct (AI, 91%)  
- **Submission_text_id: 2** – ✅ Correct (AI, 92%)  
- **Submission_text_id: 3** – ❌ Wrong (Human misclassified as AI, 93%)  
- **Submission_text_id: 4** – ❌ Wrong (Human misclassified as AI, 94%)  
- **Submission_text_id: 5** – ❌ Wrong (Hybrid misclassified as AI, 89%)  
- **Submission_text_id: 6** – ❌ Wrong (Hybrid misclassified as AI, 86%)  

**Correct Detections:**  
- AI: 2/2  
- Hybrid: 0/2  
- Human: 0/2  

**Accuracy:** `2/6 = 0.33`

---

## IT.json
- **Submission_text_id: 1** – ❌ Wrong (AI misclassified, 95%)  
- **Submission_text_id: 2** – ✅ Correct (AI, 94%)  
- **Submission_text_id: 3** – ✅ Correct (Human, 96%)  
- **Submission_text_id: 4** – ✅ Correct (Human, 97%)  
- **Submission_text_id: 5** – ✅ Correct (Hybrid, 90%)  
- **Submission_text_id: 6** – ❌ Wrong (Hybrid misclassified as Human, 91%)  

**Correct Detections:**  
- AI: 2/2  
- Hybrid: 1/2  
- Human: 2/2  

**Accuracy:** `5/6 = 0.83`

---

## Psychology.json
- **Submission_text_id: 1** – ✅ Correct (AI, 96%)  
- **Submission_text_id: 2** – ✅ Correct (AI, 97%)  
- **Submission_text_id: 3** – ❌ Wrong (Human misclassified as Hybrid, 94%)  
- **Submission_text_id: 4** – ❌ Wrong (Human misclassified as Hybrid, 95%)  
- **Submission_text_id: 5** – ❌ Wrong (Hybrid misclassified as AI, 88%)  
- **Submission_text_id: 6** – ❌ Wrong (Hybrid misclassified as AI, 87%)  

**Correct Detections:**  
- AI: 2/2  
- Hybrid: 0/2  
- Human: 0/2  

**Accuracy:** `2/6 = 0.33`

---

## Teaching.json
- **Submission_text_id: 1** – ✅ Correct (AI, 96%)  
- **Submission_text_id: 2** – ❌ Wrong (AI misclassified as Hybrid, 95%)  
- **Submission_text_id: 3** – ❌ Wrong (Human misclassified as AI, 94%)  
- **Submission_text_id: 4** – ❌ Wrong (Human misclassified as AI, 95%)  
- **Submission_text_id: 5** – ❌ Wrong (Hybrid misclassified as AI, 89%)  
- **Submission_text_id: 6** – ❌ Wrong (Hybrid misclassified as AI, 90%)  

**Correct Detections:**  
- AI: 1/2  
- Hybrid: 0/2  
- Human: 0/2  

**Accuracy:** `1/6 = 0.16`

---

## Overall Summary
**Total Accuracy:** `12/30 = 0.4`

| Domain      | AI (Correct) | Human (Correct) | Hybrid (Correct) |
|------------|-------------|----------------|-----------------|
| Accounting | 2           | 0              | 0 |
| Engineering| 2           | 0              | 0 |
| IT         | 2           | 2              | 1 |
| Psychology | 2           | 0              | 0 |
| Teaching   | 1           | 0              | 0 |
