from pprint import pprint

from agent.risk_analyzer import analyze_risks


project_text = """
I want to build an AI-powered hiring assistant
for startups that can analyze resumes,
rank candidates, and generate interview summaries.
"""

print("Running Risk Analysis...\n")

result = analyze_risks(project_text)

print("\n=== RISK ANALYSIS RESULT ===\n")

pprint(result)