# Human Evaluation Analysis – AI Detection Task

## Overall Accuracy
Correct Predictions: 16 / 30
Wrong Predictions: 14 / 30
This is barely above random chance, highlighting significant weaknesses in the model’s ability to align with human judgments.

## Domain-Level Accuracy
| Domain | Submissions | Correct | Wrong | Notes |
| --- | --- | --- | --- | --- |
| Psychology | 6 | 3 | 3 | Mixed results, struggles with Hybrid vs Human distinction. |
| IT | 6 | 4 | 2 | Best-performing domain. Clear Human essays recognized well. AI misclassified as Human persists. |
| Engineering | 6 | 3 | 3 | Similar to Psychology — balance of correct/wrong, mostly errors on Hybrid. |
| Teaching | 6 | 2 | 4 | One of the weakest; frequent over-attribution to Human. |
| Accounting | 6 | 2 | 4 | Same as Teaching — major misclassification of AI as Human. |

IT is the only domain where the detector showed reasonable reliability.
Teaching & Accounting domains are clear weaknesses, dragging down the overall performance.

## Error Pattern Analysis
### False Negatives (AI → Human/Hybrid)
- Most frequent error type, especially in Accounting & Teaching.
- Detector tends to trust AI-like polished academic writing as Human.
- Example: Accounting Submissions 1 & 2 were AI but classified as Human.
Impact: This undermines the tool’s primary purpose — to flag AI writing.

### Human Misclassified (Human → Hybrid/AI)
- Less frequent but occurs in Teaching & Accounting.
- Detector sometimes overcompensates, labelling nuanced human writing as Hybrid.
- Example: Accounting Submission 4 was Human but labelled Hybrid.

### Hybrid Misclassifications
- Hybrid texts are inconsistently detected.
- Correct in IT Submission 6 and Accounting Submission 5.
- Missed in several cases across Engineering, Teaching, and Accounting.
- Detector struggles to distinguish AI-polished from Human-authored with support.

## Confidence Analysis
- High confidence on wrong predictions is concerning and indicates a systematic blind spot.
- Many AI texts misclassified as Human were given High Confidence.
- Medium confidence appears more often on Hybrid misclassifications.

## Key Insights
- Bias toward Human labels leads to false negatives, especially in Accounting and Teaching.
- Hybrid detection is weak and often confused with Human, needing clearer criteria.
- Systematic overconfidence reveals calibration issues in prediction outputs.

## Recommendations
- Recalibrate detection thresholds to reduce bias toward Human in polished, rubric-aligned texts.
- Improve Hybrid recognition with nuanced AI + Human collaboration samples.
- Apply domain-specific fine-tuning for Accounting and Teaching.

## Final Summary
- False Negatives (AI → Human) are the largest issue.
- Hybrid misclassification underscores the need for nuanced detection.
- Overconfidence on wrong predictions suggests deeper calibration problems.
