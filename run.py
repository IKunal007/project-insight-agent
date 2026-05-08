from pprint import pprint

from agent.execution_planner import generate_execution_plan


project_text = """
I want to build an AI-powered hiring assistant
for startups that can analyze resumes,
rank candidates, and generate interview summaries.
"""

print("Running Execution Planner...\n")

result = generate_execution_plan(project_text)

print("\n=== EXECUTION PLAN ===\n")

pprint(result)