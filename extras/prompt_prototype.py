import os
import json
from google import genai
from google.genai import types

def generate_dispatch_recommendation(request_text: str) -> str:
    """
    Uses Gemini API to extract transshipment details and suggest a dispatch action.
    """
    client = genai.Client()

    system_instruction = (
        "You are an AI Dispatch Assistant for a transshipment fleet. "
        "Your job is to read natural language requests from operators, extract the key data, "
        "and output a structured JSON response containing: "
        "'pickup_location', 'dropoff_location', 'urgency' (Low, Medium, High), "
        "and a brief 'action_recommendation' for the human dispatcher."
    )

    prompt = f"Operator Request:\n\"\"\"{request_text}\"\"\""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.1, 
                response_mime_type="application/json",
            ),
        )
        return response.text
    except Exception as e:
        return json.dumps({"error": str(e), "fallback": "Route to manual dispatcher queue."})

if __name__ == "__main__":
    if not os.getenv("GEMINI_API_KEY"):
        print("[ERROR] GEMINI_API_KEY environment variable is not set!")
        exit(1)

    sample_request = "We have 4 passengers at Vincom Mega Mall Royal City needing an immediate transfer to Times City. They have heavy luggage, so prioritize an SUV. It's rush hour, so find the fastest route."
    
    print("--- ANALYZING TRANSSHIPMENT REQUEST ---")
    result = generate_dispatch_recommendation(sample_request)
    
    # Pretty print the JSON output
    try:
        parsed_json = json.loads(result)
        print(json.dumps(parsed_json, indent=2, ensure_ascii=False))
    except json.JSONDecodeError:
        print(result)