# AAIE — Final Report on Evaluation Metrics 

# **Why we wrote this**

For AAIE, we’re fine-tuning language models to  detect AI-generated writing and produce teacher-style feedback for student work. This report explains, in everyday terms, the measures (“metrics”) we’ll use to judge whether our models are doing a good job—what each metric tells us, what it doesn’t, and when to use which.

# **The two things we’re evaluating**

1\) AI-detection (Is this text likely written by AI?): We compare the model’s decisions against known examples (human, AI, or hybrid) and see how often it gets it right.

2\) Feedback quality (Is the model’s feedback similar in content and meaning to a teacher’s feedback?): We compare the model’s feedback with real teacher feedback for the same essay.

# **The metrics, in simple terms — Perplexity**

Perplexity is a number that reflects how predictable a piece of text is to the model (lower \= less surprise). We use it during training to monitor learning and pick the best checkpoint, and as a supporting signal for AI-detection. Limits: low surprise doesn’t guarantee quality or correctness, so we don’t use it alone to judge feedback.

# **The metrics, in simple terms — BLEU**

BLEU is a phrase-matching score. If the model’s feedback reuses many of the same short phrases that a teacher used, BLEU tends to go up. Good for style/wording similarity. Limits: can miss good paraphrases.

# **The metrics, in simple terms — ROUGE**

ROUGE checks coverage: did the model mention the key ideas the teacher mentioned? Good for ensuring feedback covers rubric points. Limits: still overlap-based; doesn’t fully understand meaning.

# **The metrics, in simple terms — BERTScore**

BERTScore compares meaning, not just words. It uses language representations to see if two pieces of feedback line up semantically, even with different wording. Good for capturing paraphrases; usually aligns better with human judgment than pure overlap.

# **Classification metrics (for AI‑detection or rubric labels)**

Accuracy \= overall right-or-wrong. Precision \= when the model says “AI”, how often it’s correct. Recall \= of all actual AI cases, how many we catch. F1 \= balance of precision and recall. Averaging: Macro treats each class equally (good with imbalance); Weighted reflects real-world proportions; Micro aggregates globally (often equals accuracy in multiclass).

# **Fairness and care**

We’ll review errors across meaningful groups (e.g., ESL status, essay length, topic) and adjust thresholds or rules if we see uneven patterns. Teachers remain the final decision-makers. Model output is a draft or a signal—not a verdict.

# **When we use which metric (quick guide)**

• While training: track Perplexity for learning progress and checkpoint choice.

• Feedback quality: use BERTScore (meaning), plus ROUGE (coverage) and BLEU (overlap), with a small teacher review.

• AI-detection/rubric labels: report Precision, Recall, F1, Accuracy and state whether results are macro or weighted.

# **How we set up trustworthy testing**

We’ll build a stratified gold set (a carefully curated, human-checked mini‑dataset covering different essay types). We’ll keep training/validation/test splits fixed so scores are comparable over time. Where possible, we’ll include real teacher feedback so BLEU/ROUGE/BERTScore are meaningful.

# **What this means for AAIE — AI‑detection**

We will calibrate the detector to balance precision (avoid false flags) and recall (catch real cases). Results will include a confidence signal and short explanation. Teachers are encouraged to review flagged cases rather than treat them as final.

# **What this means for AAIE — Feedback generation**

We will fine‑tune models on teacher‑style data and judge results by meaning (BERTScore), coverage (ROUGE), and overlap (BLEU), with teacher review as the final word. Draft feedback will be clearly labelled and editable.

# **What we will publish (simple, repeatable outputs)**

• Training charts: Perplexity over time and the chosen checkpoint.

• Feedback quality: BERTScore, ROUGE, BLEU, plus a few anonymised examples next to teacher comments.

• AI‑detection quality: Precision, Recall, F1, Accuracy, and a short note on fairness checks.

# **Key takeaways**

No single number tells the whole story. We use a bundle of metrics to reflect wording, meaning, coverage, and decision quality. Perplexity is for training progress and early checks, not for judging feedback usefulness. BERTScore \+ ROUGE (+ BLEU) give a rounded picture of feedback quality; Precision/Recall/F1 summarise detector behaviour. Fairness and teacher oversight are built in: models assist; teachers decide.