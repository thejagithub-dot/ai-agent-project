import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv(dotenv_path="../.env")

print("HF KEY:", os.getenv("HUGGINGFACE_API_KEY"))  # debug


# Initialize Hugging Face client

client = InferenceClient(token="HUGGINGFACE_API_KEY")

def generate_answer(query, sources):
    # Convert sources list into readable text
    if sources:
        context = "\n\n".join(sources)
    else:
        context = "No search results available."

    # Improved prompt
    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using the search results below.

Question:
{query}

Search Results:
{context}

Instructions:
- Provide a clear and helpful answer
- Use the search results when relevant
- If no useful results, answer from your own knowledge
- Keep the answer simple and structured
"""

    try:
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating answer: {str(e)}"