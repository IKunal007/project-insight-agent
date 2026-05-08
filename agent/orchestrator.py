from agent.goal_extractor import extract_goals
from agent.risk_analyzer import analyze_risks
from agent.priority_engine import prioritize_project
from agent.architecture_advisor import recommend_architecture
from agent.execution_planner import generate_execution_plan


def run_full_analysis(project_overview: str):
    print("Running Goal Extraction...")
    goals = extract_goals(project_overview)

    print("Running Risk Analysis...")
    risks = analyze_risks(project_overview)

    print("Running Priority Reasoning...")
    priorities = prioritize_project(project_overview)

    print("Running Architecture Advisor...")
    architecture = recommend_architecture(project_overview)

    print("Running Execution Planner...")
    execution_plan = generate_execution_plan(project_overview)

    return {
        "goals": goals,
        "risks": risks,
        "priorities": priorities,
        "architecture": architecture,
        "execution_plan": execution_plan
    }