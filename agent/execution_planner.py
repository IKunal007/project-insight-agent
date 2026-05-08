from agent.llm_client import generate_response
from agent.prompt_loader import load_prompt
from agent.json_parser import parse_json_response


def generate_execution_plan(project_overview: str):
    system_prompt = load_prompt("system_prompt.md")
    execution_prompt = load_prompt("execution_prompt.md")

    full_prompt = f"""
{execution_prompt}

PROJECT OVERVIEW:
{project_overview}
"""

    response = generate_response(
        system_prompt=system_prompt,
        user_prompt=full_prompt
    )

    parsed_response = parse_json_response(response)

    return parsed_response