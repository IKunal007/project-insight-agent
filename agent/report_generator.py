def generate_final_report(analysis_results: dict) -> str:
    report = []

    # Goals Section
    goals = analysis_results.get("goals", {})

    report.append("# Project Summary\n")
    report.append(f"Summary: {goals.get('summary', 'N/A')}\n")
    report.append(f"Core Objective: {goals.get('core_objective', 'N/A')}\n")

    report.append("\n## Target Users")
    for user in goals.get("target_users", []):
        report.append(f"- {user}")

    report.append("\n## Constraints")
    for constraint in goals.get("constraints", []):
        report.append(f"- {constraint}")

    report.append("\n## Success Criteria")
    for criteria in goals.get("success_criteria", []):
        report.append(f"- {criteria}")

    # Risks Section
    risks = analysis_results.get("risks", {})

    report.append("\n# Risk Analysis")

    report.append("\n## Ambiguities")
    for item in risks.get("ambiguities", []):
        report.append(f"- {item}")

    report.append("\n## Technical Risks")
    for item in risks.get("technical_risks", []):
        report.append(f"- {item}")

    report.append("\n## Scope Risks")
    for item in risks.get("scope_risks", []):
        report.append(f"- {item}")

    report.append("\n## Missing Information")
    for item in risks.get("missing_information", []):
        report.append(f"- {item}")

    # Priorities Section
    priorities = analysis_results.get("priorities", {})

    report.append("\n# Priority Breakdown")

    report.append("\n## High Priority")
    for item in priorities.get("high_priority", []):
        if isinstance(item, dict):
            report.append(f"- {item.get('feature')}: {item.get('description')}")
        else:
            report.append(f"- {item}")

    report.append("\n## Medium Priority")
    for item in priorities.get("medium_priority", []):
        if isinstance(item, dict):
            report.append(f"- {item.get('feature')}: {item.get('description')}")
        else:
            report.append(f"- {item}")

    report.append("\n## Low Priority")
    for item in priorities.get("low_priority", []):
        if isinstance(item, dict):
            report.append(f"- {item.get('feature')}: {item.get('description')}")
        else:
            report.append(f"- {item}")

    report.append("\n## MVP Scope")
    for item in priorities.get("mvp_scope", []):
        if isinstance(item, dict):
            report.append(
                f"- {item.get('component')}: {item.get('description')}"
            )
        else:
            report.append(f"- {item}")

    # Architecture Section
    architecture = analysis_results.get("architecture", {})

    report.append("\n# Recommended Architecture")

    report.append(
        f"\nArchitecture Style: {architecture.get('architecture_style', 'N/A')}"
    )

    stack = architecture.get("recommended_stack", {})

    report.append("\n## Recommended Stack")

    for category, technologies in stack.items():
        report.append(f"\n### {category.capitalize()}")

        for tech in technologies:
            report.append(f"- {tech}")

    report.append("\n## Tradeoffs")

    for tradeoff in architecture.get("tradeoffs", []):
        report.append(
            f"- {tradeoff.get('decision')}: {tradeoff.get('reason')}"
        )

    # Execution Plan Section
    execution = analysis_results.get("execution_plan", {})

    report.append("\n# Execution Plan")

    for phase in execution.get("development_phases", []):
        report.append(f"\n## {phase.get('phase')}")
        report.append(f"Goal: {phase.get('goal')}")

        for task in phase.get("tasks", []):
            if isinstance(task, dict):
                task_name = task.get("task", "")
                task_description = task.get("description")

                if task_description:
                    report.append(f"- {task_name}: {task_description}")
            else:
                report.append(f"- {task_name}")

    report.append("\n## Milestones")

    for milestone in execution.get("milestones", []):
        if isinstance(milestone, dict):
            report.append(
                f"- {milestone.get('name', milestone.get('milestone'))}: "
                f"{milestone.get('description')}"
            )
        else:
            report.append(f"- {milestone}")

    report.append("\n## Final Recommendations")

    for recommendation in execution.get("final_recommendations", []):
        if isinstance(recommendation, dict):
        
            recommendation_text = recommendation.get("recommendation", "")
    
            recommendation_reason = (
                recommendation.get("rationale")
                or recommendation.get("description")
            )
    
            if recommendation_reason:
                report.append(
                    f"- {recommendation_text}: {recommendation_reason}"
                )
            else:
                report.append(f"- {recommendation_text}")
    
        else:
            report.append(f"- {recommendation}")

    return "\n".join(report)