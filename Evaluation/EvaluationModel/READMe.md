# How to Use the Model Evaluation Framework

This guide shows you exactly how to use the model evaluation framework step by step.

## Step 1: Prepare Your Data

### For AI Detection (Classification Tasks)

Create a pandas DataFrame with these exact column names:

```python
import pandas as pd

# Your data must have these columns
df = pd.DataFrame({
    'text': [
        "This essay explores the complex relationship between technology and society.",
        "AI systems are becoming increasingly sophisticated in their capabilities.",
        "The quick brown fox jumps over the lazy dog repeatedly."
    ],
    'labels': ['human', 'ai', 'human'],        # True labels
    'predictions': ['human', 'ai', 'ai']       # Your model's predictions
})
```

### For Feedback Generation Tasks

```python
df = pd.DataFrame({
    'text': [
        "My essay about climate change discusses various environmental issues.",
        "This story begins with a mysterious character entering the room."
    ],
    'generated_texts': [
        "Your essay provides good coverage of climate issues. Consider adding more specific examples.",
        "The opening creates intrigue. Try developing the character's background more."
    ],
    'domain': ['academic', 'creative'],      # Optional
    'criteria': ['clarity', 'engagement']    # Optional
})
```

## Step 2: Create the Required Prompt Template

Create a file named `genai_prompt.json` in your project folder:

```json
{
  "ai_detection": {
    "system": "you are an AI detection expert",
    "criteria": {
      "accuracy": "Detect AI vs human text accurately"
    },
    "output_structure": {
      "prediction": "human or ai"
    },
    "example1": {
      "input": {
        "text": "Sample text here",
        "label": "human",
        "prediction": "ai"
      },
      "output": {
        "prediction": "human"
      }
    }
  },
  "feedback_generation": {
    "system": "you are a writing feedback expert",
    "criteria": {
      "helpfulness": "Provide constructive feedback"
    },
    "output_structure": {
      "feedback": "detailed feedback text"
    },
    "example1": {
      "input": {
        "text": "Sample essay",
        "domain": "academic"
      },
      "output": {
        "feedback": "Your essay shows promise..."
      }
    }
  }
}
```

## Step 3: Use the Framework

### Basic Classification Evaluation

```python
from evaluatemodel import EvaluateModel

# Initialize the evaluator
evaluator = EvaluateModel(
    dataset=df,                    # Your prepared DataFrame
    model_type="ai_detection"      # or "feedback_generation"
)

# Run evaluation and see results
evaluator.evaluate_classification_model()

# This will show:
# - Confusion matrix visualization
# - Classification report with precision, recall, F1
# - Accuracy score
```

### Basic Generative Model Evaluation

```python
evaluator = EvaluateModel(
    dataset=df,
    model_type="feedback_generation"
)

# Evaluate with multiple metrics
evaluator.evaluate_generative_model(
    metrics=['bleu', 'rouge', 'bertscore']
)

# This will print scores like:
# bleu                : 0.2451
# rouge1              : 0.3672
# rouge2              : 0.1834
# rougeL              : 0.3128
# bertscore_f1        : 0.8234
```

### Get Results Programmatically

```python
# Run evaluation without printing
evaluator.evaluate_classification_model(print_result=False)

# Access results dictionary
results = evaluator.results
print(f"Accuracy: {results['accuracy']:.3f}")
print(f"F1 Score: {results['f1_score']:.3f}")
print(f"Precision: {results['precision']:.3f}")
print(f"Recall: {results['recall']:.3f}")
```

## Step 4: Advanced Usage with Your Own Model

### Setting Up Model for Attention Visualization

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load your transformer model (must support attention output)
tokenizer = AutoTokenizer.from_pretrained("gpt2")  # or your model
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Initialize evaluator with your model
evaluator = EvaluateModel(
    dataset=df,
    model_type="ai_detection",
    model=model,
    tokenizer=tokenizer,
    device="cuda"  # Use "cpu" if no GPU available
)
```

### Attention Rollout Visualization

**What it shows**: Cumulative attention flow across all layers - how information flows from each token to the final prediction.

```python
# Example: Analyzing which words the model focuses on for AI detection
text_segment = "This essay was written using advanced AI language models."
full_prompt = "Determine if this text is AI-generated: " + text_segment

# Visualize attention rollout
evaluator.visualize_rollout(
    text=text_segment,           # The specific text you want to analyze
    prompt=full_prompt,          # Complete prompt including context
    title="AI Detection - Attention Flow"
)
```

**Output**: 
- Heatmap showing attention scores for each token
- Higher values (brighter colors) = more attention
- Shows which words contribute most to the model's decision

### Attention Weights Visualization

**What it shows**: Raw attention patterns from specific layers and heads - how each token attends to every other token.

```python
# Visualize specific layer and head
evaluator.visualize_attention_weights(
    text=text_segment,
    prompt=full_prompt,
    title="Layer 2, Head 0 - Token-to-Token Attention"
)
```

**Output**:
- Matrix heatmap where rows = "from tokens", columns = "to tokens"
- Shows which tokens pay attention to which other tokens
- Reveals patterns like attending to punctuation, subjects, etc.

### Advanced Attention Analysis

#### 1. Compare Different Layers
```python
# Analyze different layers to see how attention changes
text = "The AI model generated this creative story about dragons."
prompt = "Is this AI-generated text? " + text

for layer in [0, 6, 11]:  # First, middle, last layers
    evaluator.visualize_attention_weights(
        text, prompt, 
        title=f"Layer {layer} Attention Pattern"
    )
    # You'll see how attention patterns evolve through the model
```

#### 2. Analyze Multiple Heads
```python
# The attention weight class can analyze multiple heads
from ultis.attetion_explain import AttentionWeight

attention_analyzer = AttentionWeight(tokenizer, model, device="cuda")

# Get attention from multiple heads at once
attn_matrix, tokens = attention_analyzer.get_attention_weights(
    text=text_segment,
    prompt=full_prompt,
    layer=2,              # Which layer
    head=[0, 1, 2]       # Average across heads 0, 1, 2
)

# Visualize the averaged attention
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 8))
sns.heatmap(attn_matrix.detach().cpu(), 
           annot=True, cmap='viridis',
           xticklabels=tokens, yticklabels=tokens)
plt.title("Multi-Head Attention (Heads 0,1,2 Average)")
plt.show()
```

#### 3. Token-Specific Analysis
```python
# Focus on how a specific token (like the last token) attends to others
from ultis.attetion_explain import AttentionRollout

rollout_analyzer = AttentionRollout(tokenizer, model, device="cuda")

# Analyze attention for the last token (often the prediction token)
attention_vector, token_list = rollout_analyzer.forward(
    text=text_segment,
    prompt=full_prompt,
    token_index=-1  # Last token
)

# Show which tokens the final token pays most attention to
for token, score in zip(token_list, attention_vector):
    print(f"{token:15} | {score:.4f}")
```

### Practical Use Cases for Attention Visualization

#### 1. Debug Model Decisions
```python
# When your model makes wrong predictions, see what it's focusing on
wrong_predictions = df[df['labels'] != df['predictions']].head(3)

for idx, row in wrong_predictions.iterrows():
    text = row['text']
    true_label = row['labels']
    pred_label = row['predictions']
    
    prompt = f"Classify this text as human or AI: {text}"
    
    print(f"\nText: {text[:50]}...")
    print(f"True: {true_label}, Predicted: {pred_label}")
    
    evaluator.visualize_rollout(text, prompt, 
                               title=f"Wrong Prediction Analysis - Row {idx}")
```

#### 2. Compare Human vs AI Text Attention Patterns
```python
# See if model attends differently to human vs AI text
human_text = df[df['labels'] == 'human']['text'].iloc[0]
ai_text = df[df['labels'] == 'ai']['text'].iloc[0]

for label, text in [('Human', human_text), ('AI', ai_text)]:
    prompt = f"Determine if this is human or AI text: {text}"
    evaluator.visualize_rollout(text, prompt, title=f"{label} Text Analysis")
```

#### 3. Find Important Features
```python
# Identify which types of words/phrases get high attention
text = "This sophisticated narrative demonstrates complex reasoning patterns."
prompt = "Is this AI-generated? " + text

attention_vector, tokens = rollout_analyzer.forward(text, prompt)

# Sort tokens by attention score
token_attention_pairs = list(zip(tokens, attention_vector.cpu().numpy()))
sorted_pairs = sorted(token_attention_pairs, key=lambda x: x[1], reverse=True)

print("Most attended tokens:")
for token, score in sorted_pairs[:5]:
    print(f"'{token}': {score:.4f}")
```

### Understanding the Visualizations

**Attention Rollout Heatmap**:
- Single row showing cumulative attention
- Bright spots = tokens crucial for final decision
- Use to understand "what does the model care about most?"

**Attention Weights Matrix**:
- Square matrix showing token-to-token relationships  
- Diagonal patterns = self-attention
- Off-diagonal patterns = cross-token dependencies
- Use to understand "how do tokens interact with each other?"

### Tips for Effective Attention Analysis

1. **Start with rollout** for quick insights into important tokens
2. **Use weights matrix** for detailed token interaction patterns
3. **Compare multiple layers** to see how attention evolves
4. **Analyze failed predictions** to debug model behavior
5. **Keep text segments short** (< 50 tokens) for clear visualizations

## Step 5: Generate Prompts for Your Dataset

```python
# Build prompts for all rows in your dataset
evaluator.construct_data_messages()

# See what prompts were created
for i in range(min(3, len(evaluator.dataset_prompt))):  # Show first 3
    prompt = evaluator.dataset_prompt[i]
    print(f"=== Row {i} ===")
    print("SYSTEM PROMPT:")
    print(prompt["system"])
    print("\nUSER PROMPT:")
    print(prompt["user"])
    print("\n" + "="*50 + "\n")
```

## Common Usage Patterns

### 1. Quick Classification Check
```python
# Just want accuracy and F1? 
evaluator = EvaluateModel(df, "ai_detection")
evaluator.evaluate_classification_model(average='weighted')
print(f"Accuracy: {evaluator.results['accuracy']:.2%}")
```

### 2. Compare Different Averaging Methods
```python
for avg_method in ['macro', 'micro', 'weighted']:
    evaluator = EvaluateModel(df, "ai_detection")
    evaluator.evaluate_classification_model(average=avg_method, print_result=False)
    print(f"{avg_method.capitalize()} F1: {evaluator.results['f1_score']:.3f}")
```

### 3. Focus on Specific Metrics
```python
# Only BLEU and ROUGE for text generation
evaluator = EvaluateModel(df, "feedback_generation")
evaluator.evaluate_generative_model(
    metrics=['bleu', rouge'],  # Skip bertscore if it's slow
    print_result=True
)
```

### 4. Batch Process Multiple Datasets
```python
datasets = [df1, df2, df3]  # Your multiple datasets
results_list = []

for i, dataset in enumerate(datasets):
    evaluator = EvaluateModel(dataset, "ai_detection")
    evaluator.evaluate_classification_model(print_result=False)
    
    results_list.append({
        'dataset': f'Dataset_{i}',
        'accuracy': evaluator.results['accuracy'],
        'f1': evaluator.results['f1_score']
    })

# Compare results
for result in results_list:
    print(f"{result['dataset']}: Acc={result['accuracy']:.3f}, F1={result['f1']:.3f}")
```

## What You Get

### Classification Evaluation Output:
- **Confusion Matrix**: Visual heatmap showing true vs predicted labels
- **Classification Report**: Detailed precision, recall, F1 for each class
- **Overall Metrics**: Accuracy, macro/micro/weighted averages
- **Results Dictionary**: Programmatic access to all scores

### Generative Evaluation Output:
- **BLEU Score**: Measures n-gram overlap with reference text
- **ROUGE Scores**: ROUGE-1, ROUGE-2, ROUGE-L for different granularities
- **BERTScore**: Semantic similarity using BERT embeddings
- **Results Dictionary**: All metric scores for further analysis

### Attention Visualization Output:
- **Rollout Heatmap**: Shows cumulative attention across all layers
- **Weight Matrix**: Raw attention weights from specific layer/head
- **Token Analysis**: See exactly which tokens get attention

## Troubleshooting

**"Dataset missing required fields"**
→ Check your DataFrame has the exact column names shown above

**"Could not find text tokens in prompt"**
→ Make sure the text you want to visualize appears exactly in the full prompt

**"No module named 'ultis'"**
→ Make sure all the Python files are in the correct folder structure

**Slow BERTScore computation**
→ Remove 'bertscore' from metrics list or use smaller BERT model

Ready to evaluate your models? Start with Step 1!