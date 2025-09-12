import json
import requests
import os
import random  

# ------------------------
# Gemini API Setup
# ------------------------
API_KEY = "AIzaSyBwVZ9ABILNzNixnXFb0TgbrI90r7BEH1g"
MODEL = "gemini-1.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

HEADERS = {
    "Content-Type": "application/json",
    "X-goog-api-key": API_KEY
}

# ------------------------
# Run AI Detection Prompt
# ------------------------
def run_ai_detection(prompt_text: str) -> dict:
    """Call Gemini API and return text output as string."""
    payload = {
        "contents": [
            {"parts": [{"text": prompt_text}]}
        ]
    }

    try:
        response = requests.post(URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()

        candidates = data.get("candidates", [])
        if candidates:
            parts = candidates[0].get("content", {}).get("parts", [])
            if parts:
                return {
                    "text": "\n".join(part.get("text", "").strip() for part in parts if part.get("text"))
                }

        return {"text": "⚠️ No text found in model response."}

    except requests.exceptions.HTTPError as e:
        return {"text": f"⚠️ HTTP Error: {e}"}
    except Exception as e:
        return {"text": f"⚠️ Unexpected Error: {e}"}

# ------------------------
# Generate Criteria-based Analysis
# ------------------------
def generate_analysis(text: str) -> dict:
    """
    Assign a mock Confidence_Level (0-100%) and generate example criteria-based analysis.
    In a real setup, you would use NLP metrics or the model output to calculate these.
    """
    # Mock confidence based on heuristics or random (replace with real AI detection logic)
    confidence = random.randint(60, 95)  # Example: 75% confidence the text is AI-generated

    # criteria-based breakdown
    analysis = {
        "Confidence_Level": f"{confidence}%",
        "Criteria": {
            "Repetition": "Low" if "repeated phrases" not in text else "High",
            "Lexical Diversity": "Moderate",
            "Sentence Structure Diversity": "High",
            "Grammar": "Correct",
            "Content Specificity": "Low" if "generic" in text else "Moderate",
            "Emotional Expressiveness": "Neutral",
            "Coherence & Natural Transitions": "Moderate",
            "Pronouns & Contextual Appropriateness": "Appropriate"
        }
    }
    return analysis

# ------------------------
# Main Routine
# ------------------------
if __name__ == "__main__":
    dataset_file = "training_prompts_test.jsonl"
    if not os.path.exists(dataset_file):
        print(f"❌ File '{dataset_file}' not found.")
        exit(1)

    dataset = []
    with open(dataset_file, "r") as f:
        for line in f:
            if line.strip():
                dataset.append(json.loads(line))

    # Evaluate each prompt
    for i, item in enumerate(dataset):
        try:
            prompt_text = item.get("contents", [])[0].get("parts", [])[0].get("text", "").strip()
        except (KeyError, IndexError, TypeError):
            print(f"⚠️ Skipping task {i+1}, invalid JSON structure.")
            continue

        submission_text = item.get("submission", "N/A")

        print(f"\n=== Task {i+1} ===")
        print("Prompt:", prompt_text if prompt_text else "(Empty)")
        print("Submission:", submission_text)
        print("-" * 50)

        if not prompt_text:
            print("⚠️ No prompt text found, skipping task.")
            continue

        # Combine prompt + submission
        full_prompt = prompt_text
        if submission_text != "N/A":
            full_prompt += f"\n\nSubmission: {submission_text}"

        # Run Gemini
        result = run_ai_detection(full_prompt)
        model_text = result.get("text", "")

        # Generate criteria-based analysis
        analysis = generate_analysis(model_text)

        # Print results clearly
        print("Model Output:\n")
        print(model_text)
        print("\n--- AI Detection Analysis ---")
        print(f"Confidence_Level: {analysis['Confidence_Level']}")
        for criterion, value in analysis["Criteria"].items():
            print(f"{criterion}: {value}")
        print("=" * 80)
