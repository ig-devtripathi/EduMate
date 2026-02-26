import os
import requests
import json
import base64
from dotenv import load_dotenv

load_dotenv(override=True)
API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

API_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def _call_groq_rest(
    prompt,
    model="llama-3.3-70b-versatile",
    max_tokens=4096,
    temperature=0.4,
    image_parts=None
):
    if not GROQ_API_KEY:
        return "System Error: Gemini rate limit exceeded, and Groq fallback key not found."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    # Note: Groq's main models are text-based. We gracefully ignore images in fallback
    # to prevent JSON validation crashes against models like Llama-3.

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    try:
        response = requests.post(
            GROQ_API_URL,
            json=payload,
            headers=headers,
            timeout=30
        )

        print("GROQ STATUS:", response.status_code)

        if response.status_code != 200:
             return f"System Error: Both AI engines (Gemini & Groq) exceeded rate limits or failed."

        data = response.json()
        
        if "choices" not in data or not data["choices"]:
            return "System Error: Groq fallback returned an unexpected structure."

        return data["choices"][0]["message"]["content"]
        
    except requests.exceptions.Timeout:
        return "System Error: Both AI engines timed out."
    except Exception as e:
        return f"System Error: Network failure on Groq fallback ({str(e)})."



def _call_gemini_rest(
    prompt,
    model="gemini-2.5-flash",  # Free-tier friendly
    max_tokens=4096,
    temperature=0.4,
    image_parts=None
):
    if not API_KEY:
        return "Error: GEMINI_API_KEY not found."

    url = API_URL.format(model=model, key=API_KEY)

    parts = []

    # Handle image input (for document analyzer)
    if image_parts:
        b64_img = base64.b64encode(image_parts["data"]).decode("utf-8")
        parts.append({
            "inline_data": {
                "mime_type": image_parts["mime_type"],
                "data": b64_img
            }
        })

    parts.append({"text": prompt})

    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens
        }
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=30
        )

        print("STATUS:", response.status_code)

        if response.status_code != 200:
            error_msg = response.text.lower()
            if response.status_code == 429 or "quota" in error_msg:
                print("Gemini limit exceeded. Seamlessly falling back to Groq (Llama 3).")
                return _call_groq_rest(prompt, max_tokens=max_tokens, temperature=temperature, image_parts=image_parts)
            return f"API Error: Unable to complete request at this time."

        data = response.json()

        # Handle empty or blocked responses
        if "candidates" not in data or not data["candidates"]:
            if "promptFeedback" in data:
                return "System Error: Model blocked request due to safety filters."
            return "System Error: Unexpected response structure from API."

        parts = data["candidates"][0].get("content", {}).get("parts", [])

        if not parts or "text" not in parts[0]:
            return "System Error: Model returned no text content."

        return parts[0]["text"]

    except requests.exceptions.Timeout:
        return "System Error: Request timed out. Please try again."
    except Exception as e:
        return f"System Error: An unexpected error occurred while calling the API."


# ---------------------------
# FEATURE FUNCTIONS
# ---------------------------

def explain_concept(topic, difficulty):
    prompt = f"""
Explain the concept of "{topic}" at "{difficulty}" level.
Keep it educational and under 4 paragraphs.
"""
    return _call_gemini_rest(prompt)


def summarize_notes(notes_text):
    prompt = f"""
Summarize the following notes into concise bullet points:

{notes_text}
"""
    return _call_gemini_rest(prompt)


def generate_quiz(topic, difficulty="Medium", num_questions=5):
    prompt = f"""
Generate exactly {num_questions} multiple-choice questions about "{topic}" at a "{difficulty}" difficulty level.

Return ONLY valid JSON in this exact structure:

{{
  "questions": [
    {{
      "id": 1,
      "question": "Question text",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "answer": "Correct option text",
      "explanation": "Short explanation"
    }}
  ]
}}

IMPORTANT:
- Do not include markdown.
- Do not include backticks.
- Do not include explanations outside JSON.
- Return raw JSON only.
"""

    response_text = _call_gemini_rest(
        prompt,
        model="gemini-2.5-flash",
        temperature=0.4,
        max_tokens=4096
    )

    if not response_text:
        return "Error: Empty response from model."

    cleaned = response_text.strip()
    
    # Check for quota warnings or exact system errors
    if cleaned.startswith("⚠️") or cleaned.startswith("⏱️") or cleaned.startswith("System Error") or cleaned.startswith("API Error") or cleaned.startswith("Error:"):
        return cleaned

    # Aggressive stripping of backticks if Gemini ignored instructions
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:-3].strip()
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:-3].strip()

    # Locate the first '{' and last '}' to extract raw JSON
    start_idx = cleaned.find("{")
    end_idx = cleaned.rfind("}")
    
    if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
        cleaned = cleaned[start_idx:end_idx+1]
        
    return cleaned


def analyze_document_or_image(prompt, text_content=None, image_parts=None):
    if text_content:
        text_content = text_content[:12000]
        prompt = f"{prompt}\n\nDocument Content:\n{text_content}"

    return _call_gemini_rest(prompt, image_parts=image_parts)