from agent.orchestrator import run_full_analysis
from agent.report_generator import generate_final_report
from agent.evaluation import evaluate_analysis


project_text = """
I want to build an AI-powered hiring assistant
for startups that can analyze resumes,
rank candidates, and generate interview summaries.
"""

print("Running Full Project Insight Analysis...\n")

analysis_result = run_full_analysis(project_text)

final_report = generate_final_report(analysis_result)

print("\n=== FINAL REPORT ===\n")

print(final_report)

evaluation_result = evaluate_analysis(analysis_result)

print("\n=== EVALUATION ===\n")

print(evaluation_result)