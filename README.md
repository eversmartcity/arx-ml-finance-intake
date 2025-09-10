# arx-ml-finance-intake

A simulated healthcare finance claim pipeline built to demonstrate secure, scalable, and compliant AI/ML engineering using Celery, Redis, LLMs, and GitHub Actions. Designed to emulate production-level risk scoring, anomaly detection, and asynchronous claim triage workflows suitable for regulated environments.

---

## 🧠 Use Case Overview

This system simulates how a hospital or health finance department might:

- Accept incoming claims via JSON API
- Route them through asynchronous ML processing queues
- Analyze for fraud or anomalies via LLMs (e.g., GPT-4)
- Log or trigger escalations in a compliance-safe, CI/CD-ready pipeline

This pipeline is derived from **ArxOS’s MPC framework** — a modular AI stack composed of orchestration agents designed to emulate **clinical, financial, and user-centered decision-making systems**.

---

## ⚙️ Tech Stack

| Layer         | Tech                       |
|---------------|----------------------------|
| Input         | Flask API (`claim_intake.py`) |
| Queueing      | Redis + Celery             |
| Processing    | OpenAI GPT-4 (`llm_model.py`) |
| DevOps        | Docker, GitHub Actions, n8n |
| CI/CD         | `.github/workflows/ci.yml` |
| Deployment    | `docker-compose.yml`       |

---
## 🗂️ File Structure

📁 .github/workflows/ci.yml – GitHub Actions CI/CD pipeline  
🐳 Dockerfile – Container definition for production  
🐳 docker-compose.yml – Local multi-container orchestration  
📄 claim_intake.py – Flask API endpoint to receive claims  
📄 tasks.py – Celery tasks for background processing  
📄 llm_model.py – GPT-4 prompt logic and fraud detection  
📄 requirements.txt – Python dependencies  
📄 README.md – Project documentation
