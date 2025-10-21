# CodeVerdict ⚖️

**Where AI Code Stands Trial**

A comprehensive evaluation platform that puts AI-generated code through rigorous testing with a balanced 50/50 split between automated analysis and human judgment.

![Architecture](https://img.shields.io/badge/Architecture-Modular%20%26%20Scalable-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

## 👨‍💻 Created by Chin Keong Lam

**Principal AI Frontier Engineer & Founder**

Chin Keong brings over two decades of experience in AI systems, hardware acceleration, and full-stack development. Currently working on cutting-edge AI agent platforms and drug discovery acceleration at [Patho.ai](https://www.patho.ai), with previous roles at HP, Microsoft Research, and multiple successful startups. This tool reflects his passion for building robust, production-ready AI evaluation systems that bridge the gap between research and real-world applications.

*"In AI We Trust, But We Verify" - Chin Keong Lam*

## 🎯 What is CodeVerdict?

CodeVerdict is an open-source evaluation framework designed specifically for AI code generation systems. It provides:

- **🧪 Comprehensive Testing**: Evaluate AI models across multiple dimensions (correctness, efficiency, security, readability)
- **⚖️ Balanced Evaluation**: 50/50 split between automated analysis and human expert review
- **📊 Centralized Tracking**: MLflow integration for experiment tracking and reproducibility
- **🔍 Smart Triage**: AI-powered clustering and routing to optimize evaluation workflow
- **👥 Collaborative Review**: Argilla integration for distributed manual code review

🚀 Quick Start

Prerequisites

*   Python 3.8+
*   Docker (for Argilla)
*   Git

Installation

1.  Clone the Repository

bash

git clone https://github.com/cklam12345/codeverdict.git

cd codeverdict

1.  Set up Virtual Environment

bash

python -m venv venv

source venv/bin/activate _\# On Windows: venv\\Scripts\\activate_

1.  Install Dependencies

bash

pip install -r requirements.txt

1.  Start Services

bash

_\# Start MLflow, Argilla, and the application_

./scripts/setup\_services.sh

1.  Configure Environment

bash

cp .env.example .env

_\# Edit .env with your API keys and settings_

Basic Usage

1.  Run a Sample Evaluation

python

from codeverdict.orchestration.workflows import evaluation\_pipeline

result = evaluation\_pipeline(

eval\_set\_name="sample\_code\_evals",

model\_id="gpt-4",

manual\_dataset\_name="first\_evaluation"

)

print(f"Results: {result\['stats'\]}")

1.  Access the Interfaces

*   MLflow UI: [http://localhost:5000](http://localhost:5000/) (Experiment tracking)
*   Argilla UI: [http://localhost:6900](http://localhost:6900/) (Manual evaluation)
*   CodeVerdict API: [http://localhost:8000](http://localhost:8000/) (Main application)
*   API Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)

📋 Core Features

🎯 Smart Evaluation Sets

python

from codeverdict.data.models import CodePrompt, PromptType

_\# Create custom evaluation sets_

prompts = \[

CodePrompt(

prompt="Implement a secure authentication system in Python",

prompt\_type=PromptType.SECURITY\_AUDIT,

difficulty="hard",

test\_cases=\[...\]

)

\]

⚖️ Intelligent Triage Engine

*   Automatic Routing: AI-powered decision making for evaluation path
*   Quality Clustering: Phoenix-based embedding analysis
*   Dynamic Balancing: Maintains 50/50 split between auto/manual evaluation

🔧 Multi-Dimensional Evaluation

| Dimension | Automated Metrics | Manual Review |
| --- | --- | --- |
| Correctness | Unit test pass rate, Output validation | Logical accuracy, Edge cases |
| Efficiency | Time/space complexity analysis | Algorithm optimization |
| Security | Vulnerability scanning, Pattern detection | Security best practices |
| Readability | Code structure analysis, Style checking | Maintainability, Documentation |
| Style | Linter compliance, Formatting checks | Code organization, Naming |

👥 Collaborative Review

python

_\# Set up manual evaluation workspace_

from codeverdict.evaluation.manual\_evaluator import ManualEvaluationManager

manager = ManualEvaluationManager()

dataset = manager.setup\_code\_quality\_dataset(

"security\_review",

guidelines="Evaluate code for security vulnerabilities and best practices"

)

🛠️ Advanced Configuration

Custom Evaluation Criteria

python

from codeverdict.evaluation.auto\_evaluator import CodeAutoEvaluator

class CustomEvaluator(CodeAutoEvaluator):

def evaluate\_domain\_specific\_quality(self, completion):

_\# Add your custom evaluation logic_

return {

"domain\_score": 0.95,

"business\_logic\_correctness": 0.87

}

Model Integration

python

_\# Add new AI models_

from codeverdict.models.providers import ModelProvider

class CustomModelProvider(ModelProvider):

def generate\_completion(self, prompt, model\_config):

_\# Integrate with your model API_

return self.call\_model\_api(prompt, model\_config)

Custom Triage Rules

python

from codeverdict.evaluation.triage\_engine import TriageEngine

class CustomTriageEngine(TriageEngine):

def \_make\_triage\_decision(self, completion):

if "security" in completion.metadata.get('prompt\_type', ''):

return TriageDecision.MANUAL\_REVIEW

_\# Your custom logic here_

📊 Monitoring & Analytics

CodeVerdict provides comprehensive analytics:

*   Quality Trends: Track model performance over time
*   Evaluation Metrics: Pass rates, score distributions, confidence intervals
*   Cost Analysis: Evaluation time and resource usage
*   Rater Performance: Inter-rater reliability and bias detection

🤝 Collaboration Workflow

For AI Engineers

1.  Define evaluation criteria and test cases
2.  Version prompts and models in MLflow
3.  Run automated evaluation pipelines
4.  Analyze results and iterate on models

For Human Raters

1.  Access evaluation tasks through Argilla UI
2.  Use standardized rating rubrics
3.  Provide detailed feedback and scores
4.  Collaborate with team members

For Team Leads

1.  Monitor evaluation progress and quality
2.  Adjust triage rules and sampling rates
3.  Generate reports and insights
4.  Scale evaluation infrastructure

🔧 API Reference

Core Endpoints

| Endpoint | Method | Description |
| --- | --- | --- |
| /evaluate/{model_id} | POST | Run full evaluation pipeline |
| /results/{model_id} | GET | Get evaluation results |
| /prompts | GET/POST | Manage evaluation prompts |
| /datasets | GET/POST | Manage evaluation datasets |

Example API Usage

bash

_\# Trigger evaluation_

curl -X POST "http://localhost:8000/evaluate/gpt-4?eval\_set\_name=security\_audit"

_\# Get results_

curl "http://localhost:8000/results/gpt-4"

🚢 Deployment

Development

bash

./scripts/setup\_services.sh

Production with Docker

bash

docker-compose up -d

Kubernetes

bash

kubectl apply -f k8s/

📈 Scaling & Performance

*   Horizontal Scaling: Stateless services for easy scaling
*   Database Optimization: Connection pooling and indexing
*   Caching: Redis integration for frequent queries
*   Async Processing: Background task processing with Prefect

🛡️ Security & Compliance

*   Data Encryption: At rest and in transit
*   Access Control: Role-based access management
*   Audit Logging: Comprehensive activity tracking
*   GDPR Ready: Data anonymization and retention policies

🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](https://contributing.md/) for details.

1.  Fork the repository
2.  Create a feature branch (git checkout -b feature/amazing-feature)
3.  Commit your changes (git commit -m 'Add amazing feature')
4.  Push to the branch (git push origin feature/amazing-feature)
5.  Open a Pull Request

📄 License

This project is licensed under the MIT License - see the [LICENSE](https://license/) file for details.

🆘 Support

*   📚 [Documentation](https://github.com/cklam12345/codeverdict/docs)
*   🐛 [Issue Tracker](https://github.com/cklam12345/codeverdict/issues)
*   📧 Email Support

🙏 Acknowledgments

Built with amazing open-source tools including MLflow, Argilla, Phoenix, and Prefect.  
Inspired by the need for rigorous AI code evaluation in production systems.  
Supported by the AI/ML community's dedication to quality and safety.

CodeVerdict - Because every line of AI-generated code deserves a fair trial. ⚖️

"In AI We Trust, But We Verify" - Chin Keong Lam 🔍

## 🏗️ Architecture Overview

```mermaid
graph TD
    A[Code Prompts] --> B[AI Models]
    B --> C[Code Completions]
    C --> D{Triage Engine}
    D --> E[Auto Evaluation]
    D --> F[Manual Review]
    E --> G[Results Aggregation]
    F --> G
    G --> H[Quality Dashboard]
