`                    `**Classification Metrics for AAIE Overview:** 

AAIE  (Artificial  Assessment  Intelligence  for  Educators)  will  employ  classification models in several scenarios. These include detecting AI-generated vs. human-written assignments,  classifying  student  responses  into  rubric  categories,  identifying inappropriate AI  use,  and  tagging  revision  behaviours.  Evaluating  these  models requires more than a single accuracy figure. This report summarises key classification metrics (accuracy, precision, recall, F-scores, ROC-AUC) and fairness measures, explains how they are computed, and discusses their strengths and limitations in the educational context. 

**Accuracy:** 

Accuracy is the ratio of all predictions that are correctly predicted by the model. 

Accuracy =      TP+TN/TP+TN+FP+FN ![](Aspose.Words.5469efaf-aea8-4a91-9b24-6c888e5f2dee.001.png)

TP = TRUE POSITIVES, TN = True Negatives, FN = False Negatives, FP = False Positives. 

**Use in AAIE:** Accuracy is useful for a quick assessment of rubric-classification or revision-behaviour  classifiers  when  each  class  is  roughly  equally  represented. However, many educational tasks involve class-imbalance (e.g., only a small fraction of submissions may be AI-generated), making accuracy misleading because a model can achieve high accuracy by always predicting the majority class. So, accuracy should be reported and not used for critical decisions. 

**Precision:** 

Precision tells us among the cases model labelled positive, how many were actually positive. 

Precision = TP/TP+FP ![](Aspose.Words.5469efaf-aea8-4a91-9b24-6c888e5f2dee.002.png)

**Use in AAIE:** High precision is essential when the cost of a false alarm is high. For instance, falsely accusing a student of AI misuse could erode trust. A classifier that labels submissions as AI-generated should aim for high precision so that flagged cases are truly suspicious. Precision can also be computed per rubric category to assess how often predicted grades match teacher’s expectations. 

**Recall:** 

Recall measures the proportion of actual positives that the model detects. 

Recall = TP/TP+FN ![](Aspose.Words.5469efaf-aea8-4a91-9b24-6c888e5f2dee.003.png)

**Use in AAIE:** In situations where missing a positive case has serious consequences— such as failing to detect AI misuse or incorrectly grading a student—high recall is desirable. For example, if AI-generated content must be flagged for manual review, the model should prioritise recall to avoid allowing unflagged cases to slip through. 

**F1 Score and F-Beta Scores:** 

**F1 Score:** It is a Harmonic mean of precision and recall. 

`     `F1 Score  = 2\*(Precision\*Recall/Precision+ Recall) ![](Aspose.Words.5469efaf-aea8-4a91-9b24-6c888e5f2dee.004.png)

It balances the importance of precision and recall and is recommended over accuracy when classes are imbalanced. 

**F-beta  Score:**  Scikit-learn  generalises  the  F1  score  by  introducing  a  parameter β\betaβ that weights recall more than precision. The F-beta score is interpreted as a weighted harmonic mean of precision and recall, with a score of 1 being best. When beta>1, recall is emphasises; when beta<1, precision is emphasised. 

**Use in AAIE:** For high-stakes tasks (e.g., detecting academic misconduct) where missing a positive case is costly, AAIE can use an F-beta score with beta > 1to penalise false negatives more than false positives. Conversely, for automated grading where over-penalisation could harm students, a lower beta may be appropriate.** 

**Final Notes:** 

- Start with accuracy to find whether the model is better than random guessing.** 
- Inspect precision and recall to understand the trade-offs between false alarms and missed positives. Choose F-beta based on the cost of missing AI misuse vs. the cost of false accusations.** 
