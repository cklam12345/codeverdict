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

Python 3.8+
Docker (for Argilla)
Git
Installation

Clone the Repository
bash
git clone https://github.com/cklam12345/codeverdict.git
cd codeverdict
Set up Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies
bash
pip install -r requirements.txt
Start Services
bash
# Start MLflow, Argilla, and the application
./scripts/setup_services.sh
Configure Environment
bash
cp .env.example .env
# Edit .env with your API keys and settings
Basic Usage

Run a Sample Evaluation
python
from codeverdict.orchestration.workflows import evaluation_pipeline

result = evaluation_pipeline(
    eval_set_name="sample_code_evals",
    model_id="gpt-4",
    manual_dataset_name="first_evaluation"
)

print(f"Results: {result['stats']}")
Access the Interfaces
MLflow UI: http://localhost:5000 (Experiment tracking)
Argilla UI: http://localhost:6900 (Manual evaluation)
CodeVerdict API: http://localhost:8000 (Main application)
API Documentation: http://localhost:8000/docs
📋 Core Features

🎯 Smart Evaluation Sets

python
from codeverdict.data.models import CodePrompt, PromptType

# Create custom evaluation sets
prompts = [
    CodePrompt(
        prompt="Implement a secure authentication system in Python",
        prompt_type=PromptType.SECURITY_AUDIT,
        difficulty="hard",
        test_cases=[...]
    )
]
⚖️ Intelligent Triage Engine

Automatic Routing: AI-powered decision making for evaluation path
Quality Clustering: Phoenix-based embedding analysis
Dynamic Balancing: Maintains 50/50 split between auto/manual evaluation
🔧 Multi-Dimensional Evaluation

Dimension	Automated Metrics	Manual Review
Correctness	Unit test pass rate, Output validation	Logical accuracy, Edge cases
Efficiency	Time/space complexity analysis	Algorithm optimization
Security	Vulnerability scanning, Pattern detection	Security best practices
Readability	Code structure analysis, Style checking	Maintainability, Documentation
Style	Linter compliance, Formatting checks	Code organization, Naming
👥 Collaborative Review

python
# Set up manual evaluation workspace
from codeverdict.evaluation.manual_evaluator import ManualEvaluationManager

manager = ManualEvaluationManager()
dataset = manager.setup_code_quality_dataset(
    "security_review",
    guidelines="Evaluate code for security vulnerabilities and best practices"
)
🛠️ Advanced Configuration

Custom Evaluation Criteria

python
from codeverdict.evaluation.auto_evaluator import CodeAutoEvaluator

class CustomEvaluator(CodeAutoEvaluator):
    def evaluate_domain_specific_quality(self, completion):
        # Add your custom evaluation logic
        return {
            "domain_score": 0.95,
            "business_logic_correctness": 0.87
        }
Model Integration

python
# Add new AI models
from codeverdict.models.providers import ModelProvider

class CustomModelProvider(ModelProvider):
    def generate_completion(self, prompt, model_config):
        # Integrate with your model API
        return self.call_model_api(prompt, model_config)
Custom Triage Rules

python
from codeverdict.evaluation.triage_engine import TriageEngine

class CustomTriageEngine(TriageEngine):
    def _make_triage_decision(self, completion):
        if "security" in completion.metadata.get('prompt_type', ''):
            return TriageDecision.MANUAL_REVIEW
        # Your custom logic here
📊 Monitoring & Analytics

CodeVerdict provides comprehensive analytics:

Quality Trends: Track model performance over time
Evaluation Metrics: Pass rates, score distributions, confidence intervals
Cost Analysis: Evaluation time and resource usage
Rater Performance: Inter-rater reliability and bias detection
🤝 Collaboration Workflow

For AI Engineers

Define evaluation criteria and test cases
Version prompts and models in MLflow
Run automated evaluation pipelines
Analyze results and iterate on models
For Human Raters

Access evaluation tasks through Argilla UI
Use standardized rating rubrics
Provide detailed feedback and scores
Collaborate with team members
For Team Leads

Monitor evaluation progress and quality
Adjust triage rules and sampling rates
Generate reports and insights
Scale evaluation infrastructure
🔧 API Reference

Core Endpoints

Endpoint	Method	Description
/evaluate/{model_id}	POST	Run full evaluation pipeline
/results/{model_id}	GET	Get evaluation results
/prompts	GET/POST	Manage evaluation prompts
/datasets	GET/POST	Manage evaluation datasets
Example API Usage

bash
# Trigger evaluation
curl -X POST "http://localhost:8000/evaluate/gpt-4?eval_set_name=security_audit"

# Get results
curl "http://localhost:8000/results/gpt-4"
🚢 Deployment

Development

bash
./scripts/setup_services.sh
Production with Docker

bash
docker-compose up -d
Kubernetes

bash
kubectl apply -f k8s/
📈 Scaling & Performance

Horizontal Scaling: Stateless services for easy scaling
Database Optimization: Connection pooling and indexing
Caching: Redis integration for frequent queries
Async Processing: Background task processing with Prefect
🛡️ Security & Compliance

Data Encryption: At rest and in transit
Access Control: Role-based access management
Audit Logging: Comprehensive activity tracking
GDPR Ready: Data anonymization and retention policies
🤝 Contributing

We welcome contributions! Please see our Contributing Guide for details.

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request
📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

🆘 Support

📚 Documentation
🐛 Issue Tracker
📧 Email Support
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
