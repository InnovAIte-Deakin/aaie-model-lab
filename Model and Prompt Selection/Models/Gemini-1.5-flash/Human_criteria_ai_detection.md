# Human Criteria for AI Detection

## Accounting.json
- **Text ID: Accounting.json-001**  
  **True Classification:** AI  
  **Model Prediction:** AI  
  **Evaluation Result:** ✅ Correct  
  **Confidence Level:** High  
  **Key Observations:** Perfect grammar and punctuation, consistent sentence length, technical detail without personal voice, no human imperfections, reads like AI summary.  

- **Text ID: Accounting.json-002**  
  **True Classification:** AI  
  **Model Prediction:** AI  
  **Evaluation Result:** ✅ Correct  
  **Confidence Level:** High  
  **Key Observations:** Overly formal academic tone, consistent grammar, no imperfections.  

- **Text ID: Accounting.json-003**  
  **True Classification:** Human  
  **Model Prediction:** Hybrid  
  **Evaluation Result:** ❌ Wrong  
  **Confidence Level:** High  
  **Key Observations:** Personal perspective (“as a business student”), emotional or subjective language.  

- **Text ID: Accounting.json-004**  
  **True Classification:** AI  
  **Model Prediction:** Hybrid  
  **Evaluation Result:** ❌ Wrong  
  **Confidence Level:** High  
  **Key Observations:** Perfect grammar and punctuation, consistent sentence length, technical detail without personal voice, no human imperfections, reads like AI summary.  

- **Text ID: Accounting.json-005**  
  **True Classification:** AI  
  **Model Prediction:** AI  
  **Evaluation Result:** ✅ Correct  
  **Confidence Level:** High  
  **Key Observations:** Overly polished academic tone, reads like an AI generated summary.  

- **Text ID: Accounting.json-006**  
  **True Classification:** AI  
  **Model Prediction:** AI  
  **Evaluation Result:** ✅ Correct  
  **Confidence Level:** Medium  
  **Key Observations:** Academic but includes practical mentions like training and infra.  

**Accuracy:** `4/6 = 0.83`  
**False Positives:** 0  
**False Negatives:** 0  

---

## Engineering.json
- **Text ID: engineering.json-001** – ✅ Correct (AI, medium confidence)  
- **Text ID: engineering.json-002** – ✅ Correct (AI, medium confidence)  
- **Text ID: engineering.json-003** – ❌ Wrong (Human misclassified as AI)  
- **Text ID: engineering.json-004** – ❌ Wrong (Human misclassified as AI)  
- **Text ID: engineering.json-005** – ✅ Correct (AI, medium confidence)  
- **Text ID: engineering.json-006** – ✅ Correct (AI, medium confidence)  

**Accuracy:** `4/6 = 0.66`  
**False Positives:** 2  
**False Negatives:** 0  

---

## IT.json
- **Text ID: it.json-001** – ✅ Correct (AI)  
- **Text ID: it.json-002** – ✅ Correct (AI)  
- **Text ID: it.json-003** – ✅ Correct (Human)  
- **Text ID: it.json-004** – ✅ Correct (Human)  
- **Text ID: it.json-005** – ❌ Wrong (Human misclassified as Hybrid)  
- **Text ID: it.json-006** – ✅ Correct (Human)  

**Accuracy:** `5/6 = 0.83`  
**False Positives:** 0  
**False Negatives:** 0  

---

## Psychology.json
- **Text ID: psychology.json-001** – ✅ Correct (AI)  
- **Text ID: psychology.json-002** – ✅ Correct (AI)  
- **Text ID: psychology.json-003** – ❌ Wrong (Human misclassified as Hybrid)  
- **Text ID: psychology.json-004** – ❌ Wrong (Human misclassified as Hybrid)  
- **Text ID: psychology.json-005** – ✅ Correct (AI)  
- **Text ID: psychology.json-006** – ✅ Correct (AI)  

**Accuracy:** `4/6 = 0.66`  
**False Positives:** 0  
**False Negatives:** 0  

---

## Teaching.json
- **Text ID: teaching.json-001** – ✅ Correct (AI)  
- **Text ID: teaching.json-002** – ❌ Wrong (AI misclassified as Hybrid)  
- **Text ID: teaching.json-003** – ❌ Wrong (Human misclassified as AI)  
- **Text ID: teaching.json-004** – ❌ Wrong (Human misclassified as AI)  
- **Text ID: teaching.json-005** – ✅ Correct (AI)  
- **Text ID: teaching.json-006** – ❌ Wrong (Human misclassified as AI)  

**Accuracy:** `2/6 = 0.33`  
**False Positives:** 3  
**False Negatives:** 0  

---

## Overall Summary
**Total Accuracy:** `19/30 = 0.63`

| Domain      | AI (Correct/Total) | Human (Correct/Total) | Hybrid |
|------------|------------------|----------------------|--------|
| Accounting | 4/5              | 0/1                 | 0 |
| Engineering| 4/4              | 0/2                 | 0 |
| IT         | 2/2              | 3/4                 | 0 |
| Psychology | 4/4              | 0/2                 | 0 |
| Teaching   | 2/3              | 0/3                 | 0 |
