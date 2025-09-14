import json
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="AIzaSyBwVZ9ABILNzNixnXFb0TgbrI90r7BEH1g")  

MODEL = "gemini-1.5-flash"

# ---------------------------
# Rubrics for evaluation
# ---------------------------

FEEDBACK_CRITERIA = """
You are an evaluator. Evaluate the given feedback against these criteria:

1. Correctness (Accuracy & Helpfulness) -- 1 to 5
2. Clarity (Understandability & Communication) -- 1 to 5
3. Tone (Supportiveness & Constructiveness) -- 1 to 5
4. Actionability (Clear Next Steps & Implementation) -- 1 to 5
5. Coherence (Consistency & Flow) -- 1 to 5
6. Emotion (Emotional Intelligence & Sensitivity) -- 1 to 5

Output structure:
- Criterion Scores (each 1–5)
- Overall Rating (average or adjusted in exceptional cases)
- Reasoning (justification for each score with references to text)
"""

AI_DETECTION_CRITERIA = """
You are an evaluator. Compare model prediction with actual label using these criteria:

Repetition, Lexical Diversity, Sentence Structure Diversity, Grammar, Content Specificity,
Emotional Expressiveness, Coherence & Natural Transitions, Pronouns, Contextual Appropriateness.

Input structure:
- Text: input text
- Label: actual label (AI/Human)
- Prediction: model prediction (AI/Human)

Output structure:
- Result: Correct / Incorrect
- Criteria-based analysis (reasoning under the criteria)
- Confidence_level: percentage estimate
"""

# ---------------------------
# Utility functions
# ---------------------------

def load_jsonl(filename):
    """Load JSONL file into list of dicts"""
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"⚠️ Skipping invalid line: {e}")
    return data

def extract_text(item):
    """Extract text from contents->parts->text"""
    try:
        return item["contents"][0]["parts"][0]["text"].strip()
    except (KeyError, IndexError, TypeError):
        return ""

def run_gemini(task_text, rubric):
    """Send task + rubric to Gemini"""
    model = genai.GenerativeModel(MODEL)
    full_prompt = f"{task_text}\n\nEvaluation Criteria:\n{rubric}"
    response = model.generate_content(full_prompt)
    return response.text if response else "⚠️ No response from Gemini."

# ---------------------------
# Main
# ---------------------------

def main():
    input_file = "training_prompts_test.jsonl"
    tasks = load_jsonl(input_file)

    for i, item in enumerate(tasks, start=1):
        print(f"\n=== Task {i} ===")
        task_text = extract_text(item)

        if not task_text:
            print("No text found, skipping task.")
            print("-" * 50)
            continue

        print(f"Prompt:\n{task_text}\n")
        print("-" * 50)

        try:
            # Decide rubric based on the type of task
            if "feedback" in task_text.lower():
                rubric = FEEDBACK_CRITERIA
            elif "ai detection" in task_text.lower():
                rubric = AI_DETECTION_CRITERIA
            else:
                rubric = FEEDBACK_CRITERIA  # default

            output = run_gemini(task_text, rubric)
            print("Evaluation Output:\n", output)
        except Exception as e:
            print(f"Error during generation: {e}")
        print("-" * 50)

if __name__ == "__main__":
    main()

