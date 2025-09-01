# Tokenization Methods Analysis for AAIE Project: WordPiece vs Unigram

> **Executive Summary**  
> For AAIE’s educational + math-rich corpus, adopt **Unigram (SentencePiece)** as the **primary** tokenizer. Keep **WordPiece** for compatibility baselines and ablations (e.g., BERT-aligned comparisons).

---

## Table of Contents
- [1. Overview of Tokenization Methods](#1-overview-of-tokenization-methods)
  - [1.1 WordPiece (greedy, frequency-based)](#11-wordpiece-greedy-frequency-based)
  - [1.2 Unigram Language Model (probabilistic)](#12-unigram-language-model-probabilistic)
- [2. Strengths and Weaknesses](#2-strengths-and-weaknesses)
  - [2.1 WordPiece](#21-wordpiece)
  - [2.2 Unigram](#22-unigram)
- [3. Suitability for Educational Text](#3-suitability-for-educational-text)
  - [3.1 Clarification: “special tokens”](#31-clarification-special-tokens)
- [4. Implementation Complexity (Comparison Table)](#4-implementation-complexity-comparison-table)
- [5. AAIE Corpus Characteristics & Fit](#5-aaie-corpus-characteristics--fit)
- [6. Tokenizer Training Pipeline Design](#6-tokenizer-training-pipeline-design)
- [7. BERT Context (What & Why it Matters)](#7-bert-context-what--why-it-matters)
- [8. Recommendation ](#8-recommendation--next-steps)


---

## 1. Overview of Tokenization Methods

### 1.1 WordPiece (greedy, frequency-based)
- Starts with a base vocabulary of characters.  
- Iteratively merges the most frequent adjacent token pairs to form new tokens.  
- Produces a **fixed-size** vocabulary optimized for the corpus.  
- Encodes unknown/rare words as sequences of subwords.  
- **Example**  
unhappiness → ["un", "##happi", "##ness"]
### 1.2 Unigram Language Model (probabilistic)
- Starts with a **large** vocabulary of candidate substrings.  
- Uses **EM (Expectation–Maximization)** to prune and optimize the vocabulary.  
- Chooses tokenizations that **maximize the likelihood** of the training data.  
- **Example**  
unhappiness → ["un", "happiness"] OR ["un", "happi", "ness"]

---

## 2. Strengths and Weaknesses

### 2.1 WordPiece
**Strengths**
- Robust handling of OOV (out-of-vocabulary) words.  
- Efficient, deterministic tokenization and faster training.  
- Widely used in **BERT** and related models.

**Weaknesses**
- Can over-segment rare or domain-specific words.  
- Greedy merges can be sub-optimal for some domains.  
- Often fragments mathematical and structured patterns.

### 2.2 Unigram
**Strengths**
- More flexible segmentation; fits multilingual/rare patterns well.  
- Supports **tokenizer dropout** for improved generalization.  
- Tends to preserve meaningful subunits better in mixed-format text.

**Weaknesses**
- Heavier training (EM iterations); more tuning required.  
- Can under-segment if poorly tuned.  
- Requires robust normalization and likelihood estimation.

---

## 3. Suitability for Educational Text
- **Academic language.** Unigram often preserves complex terms (e.g., `photosynthesis`, `metacognition`) with fewer fragments; WordPiece may split rarer morphemes.  
- **Feedback/rubrics.** Both work; Unigram’s stochasticity (with dropout) can help robustness to phrasing variation.  
- **Mathematical content.** Tokenizer must handle LaTeX-style expressions, variables, operators (e.g., `E = mc^2`, `\frac{x}{y}`); WordPiece tends to fragment these; Unigram preserves more logical chunks when trained on math-rich text.

### 3.1 Clarification: “special tokens”
By “special tokens” we mean **citation markers** and **bracketed references** commonly found in academic writing—e.g., ``[1]``, ``(see above)``, ``(Eq. 3)``—plus rubric markers and numbered bullets.  
- **Why it matters:** Treating these as single units (or few subunits) helps downstream scoring, detection, and alignment.  
- **Observed behavior:**  
- **WordPiece** often splits them into many pieces like `"["`, `"1"`, `"]"` or `"("`, `"see"`, `"above"`, `")"`.  
- **Unigram**, when trained on data containing such patterns and with proper normalization, more often keeps compact subunits like `"[1]"` or `"(see above)"`.

---

## 4. Implementation Complexity (Comparison Table)

| Factor               | WordPiece                                | Unigram (SentencePiece)                   |
|---------------------|-------------------------------------------|-------------------------------------------|
| Preprocessing       | Minimal                                   | Moderate (Unicode normalization, rules)   |
| Training Time       | Faster (greedy merges)                    | Slower (EM iterations)                    |
| Tuning Requirements | Low                                       | Higher (dropout, likelihood thresholds)   |
| Hugging Face        | Yes (`tokenizers`, `transformers`)        | Yes (SentencePiece + HF integration)      |
| TensorFlow/PyTorch  | Yes                                       | Yes                                       |

---

## 5. AAIE Corpus Characteristics & Fit
**Input structure:** paragraphs, rubric sections, short feedback fragments, math assignments.  
**Vocabulary:** dense academic terms, rubric keywords, symbols, and math notation.  
**Special tokens:** citation markers (``[1]``), bracketed phrases (``(see above)``), numbered bullets, LaTeX math symbols, and equations.  
**Multilingual needs:** non-English essays and bilingual phrases.

**Tokenizer fit**
- **WordPiece:** Good if tight alignment with BERT is required; can struggle with newer/atypical formats.  
- **Unigram:** More adaptable; better at capturing rare, mathematical, and non-standard phrasing with fewer fragments.

---

## 6. Tokenizer Training Pipeline Design
**Corpus preprocessing**
- Lowercasing (if training lowercased models), Unicode normalization.  
- Preserve LaTeX/rubric syntax—do **not** strip characters like ``[](){}\/^_#%``.  
- Remove HTML artifacts without damaging math or rubric markers.

**Training methodology**
- **WordPiece:** greedy frequency merges + fixed vocab size.  
- **Unigram:** large initial vocab + EM pruning + optional tokenizer dropout.

**Vocab size tuning**
- Benchmark **8k**, **16k**, **32k**; balance over-fragmentation (small vocab) vs memory/latency (large vocab).

**Validation metrics**
- Average **subword length per sentence**.  
- **Unknown token rate** (should be very low).  
- **Token distribution entropy**.  
- **Equation/citation preservation rate** (percent of math/citation tokens kept as compact units).

**Integration plan**
- Train on the AAIE corpus (academic + math-rich).  
- Plug into **NanoGPT** and **TinyLLaMA** pipelines.  
- Evaluate on downstream tasks: **feedback generation** and **AI-text detection**.


---

## 7. BERT Context (What & Why it Matters)
**What is BERT?**  
BERT (Bidirectional Encoder Representations from Transformers) is a widely used transformer **encoder** that learns contextual word/subword representations. **BERT uses WordPiece** tokenization.

**Why it matters for AAIE**  
- If we want to reuse BERT-family checkpoints or align strictly with BERT’s preprocessing, **WordPiece** is the most compatible.  
- If our priority is **fidelity on math-rich, structured educational text** and we control training end-to-end, **Unigram** typically preserves structure better and reduces fragmentation—leading to cleaner inputs for generation and detection tasks.

---

## 8. Recommendation & Next Steps
**Recommendation**  
- **Primary:** **Unigram (SentencePiece)**  
- **Also keep:** **WordPiece** for BERT compatibility and controlled baselines.

---