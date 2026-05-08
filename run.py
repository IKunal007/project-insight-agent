from pprint import pprint

from agent.priority_engine import prioritize_project


project_text = """
I want to build an AI-powered hiring assistant
for startups that can analyze resumes,
rank candidates, and generate interview summaries.
"""

print("Running Priority Reasoning...\n")

result = prioritize_project(project_text)

print("\n=== PRIORITY ANALYSIS RESULT ===\n")

pprint(result)