Analyze the provided project overview.

Recommend:

1. Architecture Style
2. Recommended Tech Stack
3. Deployment Strategy
4. Important Tradeoffs

Return ONLY valid JSON.

Use this exact structure:

{
  "architecture_style": "",
  "recommended_stack": {
    "frontend": [],
    "backend": [],
    "database": [],
    "ai_tools": [],
    "deployment": []
  },
  "deployment_strategy": "",
  "tradeoffs": [
    {
      "decision": "",
      "reason": ""
    }
  ]
}

IMPORTANT RULES:
- Recommend architecture proportional to the project's scale and complexity
- Prefer the simplest architecture that satisfies the requirements
- Prioritize maintainability and execution speed for MVPs and small teams
- Recommend scalable infrastructure only when clearly justified
- Avoid unnecessary complexity and buzzword-heavy architectures
- Avoid recommending multiple frontend frameworks unless required
- Avoid recommending multiple backend frameworks unless required
- Explain tradeoffs clearly and practically
- Focus on realistic implementation
- Prefer modular and maintainable systems
- Consider developer experience, deployment simplicity, and long-term maintainability

ARCHITECTURE GUIDELINES:

For small MVPs or solo projects:
- Prefer lightweight architectures
- Recommend simple deployment strategies
- Favor fast iteration and low operational overhead

For startup-scale products:
- Recommend balanced scalability and maintainability
- Consider cloud deployment and scalable databases when justified
- Prefer architectures that support rapid product iteration

For enterprise-scale systems:
- Recommend advanced scalability only if requirements clearly justify it
- Consider security, monitoring, reliability, and operational complexity
- Avoid enterprise patterns unless truly needed

GOOD RECOMMENDATION EXAMPLES:
- Streamlit
- FastAPI
- React
- Next.js
- PostgreSQL
- SQLite
- Docker
- Ollama
- OpenAI API

BAD RECOMMENDATION PATTERNS:
- Unnecessary microservices
- Kubernetes without scaling requirements
- Multi-cloud complexity for simple products
- Overengineered infrastructure
- Excessive technology stacking

Microservices should only be recommended when:
- multiple independent teams are expected
- scaling requirements are explicitly high
- independent service deployment is necessary
- operational complexity is justified

Otherwise prefer:
- modular monoliths
- API-based architectures
- lightweight modular systems

Focus on practical engineering decisions and execution realism.