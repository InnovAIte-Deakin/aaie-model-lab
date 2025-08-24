The Data Flow Diagram (DFD) of the AAIE system shows how data flows from
input to output through various processing stages. The system starts
with three inputs: student essays, rubrics, and teacher feedback. AI
detection and feedback generation models are trained on these inputs. In
the AI detection flow, the student's essay is tokenized and passed
through an AI model to check for AI-generated content. In the feedback
generation flow, rubrics and teacher feedback are tokenized and
processed using a feedback model and text generator to create
suggestions. After passing the inputs from the model, again,
preprocessing is applied to refine and clean the output. The final
outputs of both models are stored in a central database. Teachers and
students can access the data through a dedicated interface. This DFD
clearly shows how data flows in the system.
