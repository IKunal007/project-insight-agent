import ollama


MODEL_NAME = "llama3.1:8b"


def generate_response(system_prompt: str, user_prompt: str) -> str:
    try:
        print("Sending request to Ollama...")

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            options={
                "temperature": 0.3
            }
        )

        print("Response received.")

        return response["message"]["content"]

    except Exception as e:
        print("ERROR:", e)
        return "LLM request failed."