from agent.llm_client import generate_response
from agent.prompt_loader import load_prompt
from agent.json_parser import parse_json_response


def recommend_architecture(project_overview: str):
    system_prompt = load_prompt("system_prompt.md")
    architecture_prompt = load_prompt("architecture_prompt.md")

    full_prompt = f"""
{architecture_prompt}

PROJECT OVERVIEW:
{project_overview}
"""

    response = generate_response(
        system_prompt=system_prompt,
        user_prompt=full_prompt
    )

    parsed_response = parse_json_response(response)

    return parsed_response