import os
import google.generativeai as genai
from dotenv import load_dotenv
import time

load_dotenv(override=True)
api_key = os.getenv("GEMINI_API_KEY")
print(f"Loaded Key Starts With: {api_key[:10]}...")

genai.configure(api_key=api_key)

models_to_test = ['gemini-2.5-flash']

for model_name in models_to_test:
    print(f"\n--- Testing {model_name} ---")
    try:
        model = genai.GenerativeModel(model_name)
        start_time = time.time()
        print("Sending prompt: 'Hello, are you alive? Reply with YES'")
        response = model.generate_content("Hello, are you alive? Reply with YES", request_options={"timeout": 10})
        end_time = time.time()
        print(f"SUCCESS ({end_time - start_time:.2f}s): {response.text.strip()}")
    except Exception as e:
        print(f"FAILED: {str(e)}")
