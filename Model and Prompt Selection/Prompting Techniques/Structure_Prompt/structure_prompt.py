# %%
import torch
import json
import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM


# %%
from typing import List, Dict, Any

def build_detection_prompt(submission: str, domain: str):
    """
    Build a structured prompt for classifying submissions as Human, AI, or Hybrid.
    """
    role = f'You are an impartial AI text detector evaluating in {domain} whether a given text is AI- or human-generated or Hybrid.'
    task = 'Classify the text and provide reasoning for your decision.”'   
    step =  """
    Step 1: Analyze the text’s linguistic patterns and style. 
    Step 2: Compare patterns to typical AI-generated and human-written texts. 
    Step 3: Determine the label (AI-generated or human-written). 
    Step 4: Provide reasoning"""

    with open(f"/kaggle/input/training-data-subject/Training Data/{domain}.json", "r") as file:
        data = json.load(file)
    # Few-shot examples block
    examples_block = []
    for s in data['submissions']:
        examples_block.append(f'Submission: {s.get("final_submission","")}label: {s.get("label_type")}\n' )

    system_prompt = f"""
    {role}
    Your task is to {task}
    Following the {step}
   
    Given the examples:
    {examples_block}

    Take the input:
        - 'Submission' which is submission.
    Then output these following:
        - label: AI, Human or Hybird
        - Reasoning:
            - First reason why it is the predicted label.
            - Second reason why it is the predicted label.
    """

    user_prompt = 'This the submission {submission}. Base on that provided me result'
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


# %%
def build_feedback_prompt(domain: str, submission: str) -> List[Dict[str, str]]:
    """
    Build a structured prompt for rubric-aligned feedback generation.
    """
    def format_rubric(rubric):
      formatted_rubric = f"""
      Rubric ID: {rubric['rubric_id']}
    
      Criteria:
      """
    
      for rubric_item in rubric['criteria']:
        formatted_rubric += f"""
        Criterion: {rubric_item['criterion_id']}
        Name: {rubric_item['name']}
        Description: {rubric_item['description']}
        Performance Descriptors:
        """
        for key, val in rubric_item['performance_descriptors'].items():
          formatted_rubric += f"""
          - {key}: {val}
          """
      return formatted_rubric
    with open(f"/kaggle/input/training-data-subject/Training Data/{domain}.json", "r") as file:
        data = json.load(file)
    rubric = format_rubric(data['rubric'])
    role = f"You are a helpful and respectful educational assessment assistant of {domain} that provides feedback on submitted work. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Provide assessment feedback and a rating for the assessment based on performce descriptors."
    task = "Analyze the student’s response and generate detailed, actionable feedback"
    step = """
    Summarize overall performance in 2-4 sentences.
    For each rubric criterion:
    •	Identify rating (excellent to poor)
    •	Provide evidence from the submission (1-3 points)
    •	Give one concrete improvement tip

    """
    system = f"""
    {role} and your task is to {task}.
    Given the rubric of task is:
    {rubric}
    Following the below step: {step}
    
    Take the input as a text submission of the task and provide the output as these following:
        1) Overall Summary: 2–4 sentences on strengths and priorities.
        2) Criteria Feedback: For each rubric criterion, include:
           - Criterion
           - Rating (excellent, good, average, needs_improvement, poor)
           - Evidence (1–3 bullet points citing excerpts or behaviors)
           - Improvement Tip (one concrete step)
"""
    user = f"This is the submission of the student {submission} and provide the output"
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]

# %%
from huggingface_hub import login

def generate_result(model, tokenizer, text, device = 'cuda'):
    model.to(device)
    inputs = tokenizer.apply_chat_template(
                    text,
                    add_generation_prompt=True,
                    tokenize=True,
                    return_dict=True,
                    return_tensors="pt",
                ).to(device)
    output_ids = model.generate(**inputs, max_new_tokens=800)
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    prompt_text = tokenizer.decode(inputs["input_ids"][0], skip_special_tokens=True)
    return generated_text[len(prompt_text):].strip()

# %%
model_id = "mistralai/Mistral-7B-Instruct-v0.2"
token = "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"
login(token=token)
    
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_id)


# Example submission and rubric
submission_human_it = """
In network security, firewalls act as a barrier between a trusted internal network and untrusted external networks. 
They filter incoming and outgoing traffic based on pre-defined rules. Additionally, intrusion detection systems (IDS) 
monitor network traffic for suspicious activity and alert administrators. Combining firewalls with IDS enhances 
overall network security by preventing unauthorized access and detecting potential threats.
"""
domain = 'it'

# Run Academic Integrity Detector
detector_prompt = build_detection_prompt(submission = submission_human_it, domain = 'it')
detector_result = generate_result(model = model, tokenizer = tokenizer,text = detector_prompt)
print("=== Academic Integrity Detection ===")
print(detector_result)

# Run Rubric-Aligned Feedback
feedback_prompt = build_feedback_prompt(submission = submission_human_it, domain = 'it')
feedback_result = generate_result(model = model, tokenizer = tokenizer,text = feedback_prompt)
print("\n=== Rubric-Aligned Feedback ===")
print(feedback_result)


# %%


# %%



