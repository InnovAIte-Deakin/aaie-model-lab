{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # NanoGPT Model Assessment\
## Executive Summary\
After testing across multiple academic domains, NanoGPT demonstrates some limitations in AI detection and feedback generation, but overall, in contrast with the other models, this performed well.\
\
## Key Findings\
\
### Generic Feedback Generation\
\
- High content repetition across all submissions, for example, "The submission demonstrates a solid understanding of...\'94.\
- No personalization - identical suggestions regardless of submission quality or ground truth label.\
\
### Poor AI Detection Performance\
\
- Cannot distinguish between Human, AI, and Hybrid writing, and frequently misclassifies submissions as Hybrid with around 10% accuracy for classifying humans.\
- Inconsistent classification.\
\
### Technical Limitations\
\
- The model is a paid service.\
\
### Performance Data\
\
| Metric                              | NANGOGPT Result    |\
| \'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97| \'97\'97\'97\'97\'97\'97\'97\'97\'97\'97|\
| Feedback Quality            | 4/5 			    |\
| Content Uniqueness       | <10% 			    |\
| AI Detection Accuracy     | 39% 			    |\
| Response Time               | Fast 			    |\
\
## Detailed Analysis\
\
### Feedback Generation Issues\
\
Sample Output Analysis:\
\
- **Domain:** Accounting (Blockchain Technology)  \
  **Generated:** "The submission demonstrates a solid understanding of blockchain technology and its implications for accounting..."\
\
- **Domain:** Teaching (Early Literacy)  \
  **Generated:** "The submission demonstrates a solid understanding of key early literacy concepts, developmental milestones..."\
\
- **Domain:** Psychology (Cognitive Biases)  \
  **Generated:** "The submission demonstrates a solid understanding of cognitive biases and their relevance in practical contexts..."\
\
No specialized terminology is used across different domains, and the model fails to provide unique, actionable insights based on the submission's content.\
\
### AI Detection Failures\
The total number of training examples in each domain is 6, equally divided into three classes. The model failed to achieve better results for the human class with an accuracy of 10%, and was biased toward the AI and hybrid classes, with around 70% accuracy in detecting AI class.\
\
### Why NANGOGPT Fails\
\
- Insufficient specialized academic content in its training.\
- Limited exposure to educational evaluation patterns and rubric-based feedback.\
- Missing examples of high-quality, specific, and actionable educational feedback.\
- Bias toward the hybrid class because of the detection prompt.\
\
### Alternative Solutions\
\
- GPT-4 Turbo better capabilities in educational assessment and reasoning.  \
- Claude 3 strong performance in reasoning, analysis, and adapting to specific domains.  \
- Gemini Pro potential for education-focused optimizations and integrations.\
\
### Hybrid Approaches\
\
- Train or fine-tune separate models for each academic field to improve expertise.  \
- Combine multiple models to improve AI detection accuracy.  \
- Use AI to provide initial suggestions that are then reviewed and refined by a human educator.\
\
## Conclusion\
\
While NANGOGPT is fast, it lacks the accuracy, consistency, and domain knowledge required for educational assessment applications. It cannot be directly labeled as a failure; its performance depends on the data, prompts, and context. However, based on the current evaluation framework, critical limitations were identified, preventing deployment of a flawed tool and providing clear direction for exploring more capable and reliable alternatives.\
}