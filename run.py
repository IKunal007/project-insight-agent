from agent.goal_extractor import extract_goals


project_text = """
I want to build an AI-powered hiring assistant
for startups that can analyze resumes,
rank candidates, and generate interview summaries.
"""

result = extract_goals(project_text)

print(result)