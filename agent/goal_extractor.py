from agent.llm_client import generate_response
from agent.prompt_loader import load_prompt


def extract_goals(project_overview: str) -> str:
    system_prompt = load_prompt("system_prompt.md")
    goal_prompt = load_prompt("goal_prompt.md")

    full_prompt = f"""
{goal_prompt}

PROJECT OVERVIEW:
{project_overview}
"""

    response = generate_response(
        system_prompt=system_prompt,
        user_prompt=full_prompt
    )

    return response