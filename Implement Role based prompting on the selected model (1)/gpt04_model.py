import os
import json
from openai import AzureOpenAI

# ------------------------
# 1. Azure OpenAI Client Setup
# ------------------------
endpoint = "https://prompttechnique.openai.azure.com/"
subscription_key = "2uolqoqrTeC6eU1exxJDIjbZPw56w3gOsEkj6woGg7tEXjHG83a4JQQJ99BIACL93NaXJ3w3AAABACOGPSjG"  
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version=api_version
)

# Fine-tuned deployment
deployment = "gpt-4-1-nano-2025-04-14-ft-63a7cd1dcd5441759d25c5fd42246603"

# ------------------------
# 2. Function to run a prompt
# ------------------------
def run_finetuned_prompt(prompt: str, system_message: str) -> str:
    """
    Sends a prompt to the fine-tuned deployment and returns the output text.
    For feedback generation tasks, it can provide rubric-style detailed feedback.
    """
    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1200,   # increased for detailed rubric outputs
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()

# ------------------------
# 3. Read JSONL dataset
# ------------------------

dataset = []

with open("training_prompts.jsonl", "r") as f:
    for line in f:
        if line.strip():
            dataset.append(json.loads(line))

# ------------------------
# 4. Run each prompt through fine-tuned model
# ------------------------
for i, item in enumerate(dataset):
    # Extract messages
    messages = item.get("messages", [])
    system_msg = next((m["content"] for m in messages if m["role"] == "system"), "")
    user_msg = next((m["content"] for m in messages if m["role"] == "user"), "")

    print(f"\n=== Task {i+1} ===")
    print("Prompt:", user_msg)

    try:
        result = run_finetuned_prompt(user_msg, system_msg)
        print("Model Output:\n", result)
    except Exception as e:
        print("⚠️ Error running prompt:", e)

# ------------------------
# 5. Close client
# ------------------------
client.close()
