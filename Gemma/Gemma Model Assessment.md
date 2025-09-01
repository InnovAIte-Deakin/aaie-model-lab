{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh18000\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Gemma Model Assessment\
\
## Executive Summary\
\
After testing, the Gemma model demonstrates better results in generating structured, criteria-based feedback. However, the model fails in AI detection capabilities, displaying an extreme bias, and is unusable for classification tasks. While the feedback quality is a notable improvement over other models, the detection performance is a major limitation.\
\
## Key Findings\
\
### Structured but Repetitive Feedback Generation\
\
- The model generates detailed, rubric-style feedback, including specific criteria, ratings, evidence from the text, and actionable improvement tips. However, the overall summary has high content repetition across submissions, frequently starting with \'93The student demonstrates a solid understanding of the manufacturing process..."\
\
### Complete AI Detection Failure\
\
- The model is incapable of distinguishing between Human, AI, and Hybrid writing.\
- The model showed consistent bias, misclassifying every single submission as Hybrid, regardless of the ground truth label.\
\
### Prohibitively Slow Performance\
\
- The model took 1.5 hours to process 6 submissions, resulting in an average of 15 minutes per submission.\
-This response time is not viable for real-time or high-throughput educational assessment applications.\
\
### Technical Limitations\
\
- Gemma models are typically open-source, which may require significant technical expertise for setup, fine-tuning, and maintenance.\
\
### Performance Data\
\
| Metric                          | Gemma Result  |\
| 			      | 			 |\
| Feedback Quality        | 4/5                     |\
| AI Detection Accuracy | 33%                   |\
\
## Detailed Analysis\
\
### Feedback Generation Issues and Strengths\
\
While the high-level summary is generic, the model excels at breaking down its evaluation into a structured format.\
\
**Sample Output Analysis**\
\
- Criterion: c1  \
- Rating: good  \
- Evidence: "The engineer explicitly mentions 'mapping out the entire production workflow' and 'value stream maps,' demonstrating an understanding of process analysis."  \
- Improvement Tip: "Expand on the specific CAD software used and how it was utilized to optimize the layout..."  \
\
This structured output is a clear advantage, providing more actionable insights than a single block of text.\
\
### AI Detection Failures\
\
The model's performance on the 6 test examples per domain was exceptionally poor due to a complete bias towards one class. The ground truth data was equally divided into two examples for each of the three classes (Human, AI, Hybrid).\
\
### Why Gemma Fails and Succeeds\
\
- The model is likely biased by a detection prompt, causing it to default to Hybrid in all cases. It lacks the nuanced training to differentiate between writing styles effectively. Conversely, the model appears to have been trained effectively on educational evaluation patterns and rubric-based feedback structures. This allows it to generate detailed, criteria-driven assessments\'97a significant strength.\
\
### Hybrid Approaches\
\
- Train or fine-tune separate models for each academic field to improve subject-matter expertise.\
- Use AI to provide initial suggestions that are then reviewed and refined by a human educator.\
\
## Conclusion\
\
Gemma's ability to generate structured, rubric-based feedback is better for educational applications, whereas its failure in AI detection makes it an unreliable tool for classification. The model is biased towards a single class. The evaluation result shows a strength in structured feedback and a failure in detection. This provides a clear direction to use Gemma for feedback capabilities only under strict human supervision while exploring more reliable alternatives for any text classification or AI detection tasks.\
}