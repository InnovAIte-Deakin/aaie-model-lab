Tokenization Methods Analysis for AAIE Project: WordPiece vs Unigram
________________________________________
1. Overview of Tokenization Methods
WordPiece:
•	Core Logic: Greedy, frequency-based subword tokenization algorithm.
o	Starts with a base vocabulary of characters.
o	Iteratively merges the most frequent pairs of tokens to form new tokens.
o	Produces a fixed-size vocabulary optimized for the corpus.
o	Encodes unknown or rare words as subword sequences.
•	Example: unhappiness → ["un", "##happi", "##ness"]
Unigram Language Model Tokenizer:
•	Core Logic: Likelihood-based probabilistic model.
o	Starts with a large vocabulary of all possible substrings.
o	Uses EM (Expectation-Maximization) to prune vocabulary.
o	Picks tokenizations that maximize the likelihood of the training data.
•	Example: unhappiness → ["un", "happiness"] OR ["un", "happi", "ness"] depending on learned probabilities.
________________________________________
2. Strengths and Weaknesses
WordPiece
•	Strengths:
o	Robust handling of OOV (out-of-vocabulary) words.
o	Efficient and deterministic tokenization.
o	Widely used in BERT and related models.
•	Weaknesses:
o	Can over-segment rare or domain-specific words.
o	Less flexible than probabilistic approaches.
o	Assumes greedy best merge path, potentially suboptimal.
Unigram
•	Strengths:
o	More flexible in selecting tokenization paths.
o	Supports dropout regularization for improved generalization.
o	Better handling of multilingual and rare patterns.
•	Weaknesses:
o	Computationally heavier to train.
o	Prone to under-segmentation if not tuned properly.
o	Requires robust likelihood estimation for effectiveness.
________________________________________
3. Educational Text Suitability
•	Academic Language:
o	Unigram may preserve complex educational terms better (e.g., photosynthesis, metacognition).
o	WordPiece is more stable with known academic roots but may fragment novel jargon.
•	Feedback Structure:
o	Both support rubric-style and structured comments.
o	Unigram allows smoother handling of sentence boundaries and expressions.
•	Special Patterns:
o	WordPiece often fails to preserve token boundaries for special cases ([1], (see above)).
o	Unigram more capable of learning special token patterns given sufficient training data.
•	Mathematical Content:
o	Tokenizers must be able to handle LaTeX-style equations, variables, operators, and math symbols (e.g., E = mc^2, \frac{x}{y}).
o	WordPiece may fragment equations unpredictably.
o	Unigram, when trained with such patterns included in the corpus, better preserves math expressions as logical subunits.
________________________________________
4. Implementation Complexity
Factor	WordPiece	Unigram
Preprocessing	Minimal	Moderate (normalization)
Training Time	Faster	Slower (EM iterations)
Tuning Requirements	Low	High (dropout, likelihood)
HuggingFace Support	Yes (via tokenizers)	Yes (via SentencePiece)
TensorFlow Support	Yes	Yes
________________________________________
5. Educational Corpus Characteristics
•	Input Structure: Paragraphs, rubric sections, feedback fragments, and math assignments.
•	Vocabulary: Dense with academic terms, rubric-specific keywords, symbols, and math notation.
•	Special Tokens: [1], (see above), numbered bullets, LaTeX math symbols, equations.
•	Multilingual Needs: Non-English essays and bilingual phrases.
Tokenizer Fit:
•	WordPiece: Better if alignment with BERT is needed; struggles with new formats.
•	Unigram: Better adaptability; captures rare, mathematical, and non-standard phrasing more flexibly.
________________________________________
6. Tokenizer Training Pipeline Design
•	Corpus Preprocessing:
o	Lowercasing, Unicode normalization, removal of HTML artifacts.
o	Custom filters to preserve rubric syntax and LaTeX/math notation.
•	Training Methodology:
o	WordPiece: Greedy frequency merge + fixed vocab size.
o	Unigram: Large initial vocab + EM pruning + optional dropout.
•	Vocab Size Tuning:
o	Start with 8k, 16k, 32k for benchmarking.
o	Balance between over-fragmentation (small vocab) and memory overhead (large vocab).
•	Validation Metrics:
o	Subword length per sentence.
o	Unknown token rate.
o	Token distribution entropy.
o	Equation/token preservation accuracy.
•	Integration Plan:
o	Train on AAIE corpus (including academic and math-rich text).
o	Plug into NanoGPT and TinyLLaMA pipelines.
o	Evaluate on downstream tasks: feedback generation, AI-text detection.
________________________________________
7. Tokenization Strategy Recommendation
Recommended: Unigram Tokenizer
•	Why:
o	Superior handling of multilingual, structured, mathematical, and domain-specific text.
o	Flexibility in token segmentation helps generate higher-quality feedback.
o	Better preserves academic phrasing essential for detection tasks.
•	Integration Plan:
o	Train SentencePiece-based Unigram tokenizer.
o	Validate against reference corpus with special formatting and equations.
o	Deploy in Sprint 2 along with model finetuning.
________________________________________
Final Notes
•	BERT compatibility favors WordPiece, but for AAIE-specific goals, Unigram provides better fidelity and adaptability.
•	Recommend keeping a parallel WordPiece tokenizer for comparison and fallback.
________________________________________



