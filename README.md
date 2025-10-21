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
