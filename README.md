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
| Processing    | OpenAI GPT-5 (`llm_model.py`) |
| DevOps        | Docker, GitHub Actions, n8n |
| CI/CD         | `.github/workflows/ci.yml` |
| Deployment    | `docker-compose.yml`       |

![CI](https://github.com/eversmartcity/arx-ml-finance-intake/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)

## 🧠 MPC Architecture

This pipeline follows a modular architecture derived from the ArxMPCs (Modular Processing Components) framework, enabling orchestration of AI agents across isolated tasks:

Module Roles

- ClaimIntake: Handles API intake and schema validation
- QueueProc: Redis + Celery based job distribution
- LLMProc: GPT-4-powered fraud scoring + anomaly detection
- CI/CD: GitHub Actions-based CI/CD for compliance checks
- OpsProc: Dockerized service orchestration and deployment
### 🧩 Modular Processing Components Overview
📥 ClaimIntake → 📤 QueueProc → 🧠 LLMProc → ✅ CI/CD → 🚀 OpsProc

Each module is designed to be independently testable, replaceable, and deployable, with clear API boundaries and message-passing via Redis queues.

📊 **Architecture Diagram**

See `docs/architecture.png` for a visual overview of the pipeline — from claim intake to ML triage and CI/CD handling.

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

---

## 🧪 How to Run Locally

To run this AI/ML finance claim pipeline locally:

1. **Clone the repo**

```bash
git clone https://github.com/evermartcity/arx-ml-finance-intake.git
cd arx-ml-finance-intake

python3 -m venv venv
source venv/bin/activate     # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

docker-compose up --build

curl -X POST http://localhost:5000/claim \
  -H "Content-Type: application/json" \
  -d '{"patient_id": "123", "procedure": "MRI", "cost": 950}'
