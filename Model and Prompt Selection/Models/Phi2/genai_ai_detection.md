# Evaluation with GenAI for AI Detection

## Accounting

### Submission_text_id: 1
- Label: AI
- Prediction: Hybrid
- Result: Wrong Prediction
- Confidence Level: 90% (high confidence text is AI-generated)

### Submission_text_id: 2
- Label: AI
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 95% (Very high confidence that text is AI-generated)

### Submission_text_id: 3
- Label: Human
- Prediction: Hybrid
- Result: Wrong Prediction
- Confidence Level: 93% (strong confidence the text is Human-written)

### Submission_text_id: 4
- Label: Human
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 94% (high confidence text is human written)

### Submission_text_id: 5
- Label: Hybrid
- Prediction: Hybrid
- Result: Correct Prediction
- Confidence Level: 88% (high confidence the text is best described as Hybrid — AI-like fluency with domain-aware specificity.)

### Submission_text_id: 6
- Label: Hybrid
- Prediction: Hybrid
- Result: Correct Prediction
- Confidence Level: 87% (confident it is best described as Hybrid — AI fluency with structured specificity).

**Accuracy_accounting = 2/6 = 0.3**

---

## Engineering

### Submission_text_id: 1
- Label: AI
- Prediction: Hybrid
- Result: Wrong Prediction
- Confidence Level: 91% (high confidence this is AI-generated, not Hybrid).

### Submission_text_id: 2
- Label: AI
- Prediction: null
- Result: Wrong Prediction
- Confidence Level: 92% (high confidence text is AI-generated).

### Submission_text_id: 3
- Label: Human
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 93% (high confidence text is Human-written).

### Submission_text_id: 4
- Label: Human
- Prediction: Hybrid
- Result: Wrong Prediction
- Confidence Level: 94% (high confidence text is Human-written).

### Submission_text_id: 5
- Label: Hybrid
- Prediction: Hybrid
- Result: Correct Prediction
- Confidence Level: 89% (high confidence the text is Hybrid — polished, structured like AI, but with Human-like touches such as phrasing and tone)

### Submission_text_id: 6
- Label: Hybrid
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 86% (moderately high confidence text is Hybrid — AI polish with Human-like considerations).

**Accuracy_engineering = 1/6 = 0.16**

---

## IT

### Submission_text_id: 1
- Label: AI
- Prediction: AI
- Result: Correct Prediction
- Confidence Level: 95% (very high confidence text is AI-generated).

### Submission_text_id: 2
- Label: AI
- Prediction: AI
- Result: Correct Prediction
- Confidence Level: 94% (high confidence text is AI-generated).

### Submission_text_id: 3
- Label: Human
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 96% (very high confidence text is Human-written).

### Submission_text_id: 4
- Label: Human
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 97% (very high confidence text is Human-written).

### Submission_text_id: 5
- Label: Hybrid
- Prediction: Hybrid
- Result: Correct Prediction
- Confidence Level: 90% (high confidence text is Hybrid — AI structure + Human experience).

### Submission_text_id: 6
- Label: Hybrid
- Prediction: Hybrid
- Result: Correct Prediction
- Confidence Level: 91% (strong confidence this is Hybrid — AI structure + Human perspective).

**Accuracy_IT = 4/6 = 0.66**

---

## Psychology

### Submission_text_id: 1
- Label: AI
- Prediction: AI
- Result: Correct Prediction
- Confidence Level: 96% (very high confidence text is AI-generated).

### Submission_text_id: 2
- Label: AI
- Prediction: AI
- Result: Correct Prediction
- Confidence Level: 97% (very high confidence text is Human-written).

### Submission_text_id: 3
- Label: Human
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 94% (high confidence this text is Human-written).

### Submission_text_id: 4
- Label: Human
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 95% (high confidence this text is Human-written).

### Submission_text_id: 5
- Label: Hybrid
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 88% (high confidence this text is Hybrid).

### Submission_text_id: 6
- Label: Hybrid
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 87% (good confidence this is Hybrid, not pure AI).

**Accuracy_psychology = 2/6 = 0.33**

---

## Teaching

### Submission_text_id: 1
- Label: AI
- Prediction: AI
- Result: Correct Prediction
- Confidence Level: 96% (very high confidence the text is AI-generated).

### Submission_text_id: 2
- Label: AI
- Prediction: AI
- Result: Correct Prediction
- Confidence Level: 95% (very high confidence the text is AI-generated).

### Submission_text_id: 3
- Label: Human
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 94% (strong confidence text is Human-written).

### Submission_text_id: 4
- Label: Human
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 95% (very high confidence this is Human-written).

### Submission_text_id: 5
- Label: Hybrid
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 89% (good confidence text is Hybrid, not pure AI).

### Submission_text_id: 6
- Label: Hybrid
- Prediction: AI
- Result: Wrong Prediction
- Confidence Level: 90% (high confidence text is Hybrid).

**Accuracy_teaching = 2/6 = 0.33**
