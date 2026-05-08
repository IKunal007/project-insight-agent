import json
import re


def parse_json_response(response_text: str):
    try:
        # Extract JSON block
        json_match = re.search(r"\{.*\}", response_text, re.DOTALL)

        if not json_match:
            return {
                "error": "No JSON found",
                "raw_response": response_text
            }

        json_text = json_match.group(0)

        return json.loads(json_text)

    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON response",
            "raw_response": response_text
        }