import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def score_claim(claim_data):
    prompt = f"Analyze this healthcare finance claim: {claim_data}. Determine risk and anomalies."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
