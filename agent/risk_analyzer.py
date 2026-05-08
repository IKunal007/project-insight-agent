from agent.llm_client import generate_response
from agent.prompt_loader import load_prompt
from agent.json_parser import parse_json_response


def analyze_risks(project_overview: str):
    system_prompt = load_prompt("system_prompt.md")
    risk_prompt = load_prompt("risk_prompt.md")

    full_prompt = f"""
{risk_prompt}

PROJECT OVERVIEW:
{project_overview}
"""

    response = generate_response(
        system_prompt=system_prompt,
        user_prompt=full_prompt
    )

    parsed_response = parse_json_response(response)

    return parsed_response