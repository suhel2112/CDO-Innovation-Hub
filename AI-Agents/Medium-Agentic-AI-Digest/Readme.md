🌐 Medium Agentic AI Digest — Weekly Autonomous AI Agent

A cloud-hosted, fully autonomous agent that scans Medium for Agentic AI content and delivers a curated weekly digest to your inbox.

📌 Overview

The Medium Agentic AI Digest is an autonomous Python agent that runs weekly via GitHub Actions. It scans Medium’s Agentic AI tag, collects the most recent articles, and emails a concise digest to your configured address.
This project is part of the broader AI Agents Lab within the CDO Innovation Hub.

🎯 Purpose

Agentic AI is evolving rapidly, and manual monitoring is inefficient.
This agent automatically retrieves new content, compiles a digest, and sends it directly to you, allowing hands-off tracking of trends and insights.

🧠 What This Agent Does

Each week, the agent:

Connects to Medium’s RSS feed for the agentic-ai tag

Retrieves articles from the past 7 days

Extracts metadata including:

-Title
-Publish date
-URL
-Summary snippet

Builds a clean weekly digest

Sends the digest to your email

Executes fully in the cloud via GitHub Actions

⚙️ Architecture
🟦 Python Agent

Built using:

feedparser for RSS ingestion

python-dotenv for environment variable handling

smtplib for email delivery

The agent is stateless and processes a 7-day window during each weekly run.

🟧 GitHub Actions (Serverless Execution)

A scheduled workflow triggers the agent every Saturday at 09:00 UTC.

on:
  schedule:
    - cron: "0 9 * * 6"
  workflow_dispatch: {}

🟩 Secrets Management

GitHub Actions securely stores and injects SMTP and email credentials:

-SMTP_HOST
-SMTP_PORT
-SMTP_USER
-SMTP_PASS
-TO_EMAIL
-FROM_EMAIL

No credentials are stored in code.

📁 Repository Structure
AI-Agents/
└── Medium-Agentic-AI-Digest/
    ├── medium_agent.py
    ├── smtp_test.py
    ├── README.md
    ├── .gitignore
    └── (local only) .env
.github/
└── workflows/
    └── medium-agent.yml

🚀 Execution Flow

1.GitHub Actions starts on schedule
2.Python environment is set up
3.Dependencies are installed
4.medium_agent.py runs
5.Articles from the last 7 days are collected
6.Digest email is composed
7.Email is delivered to your inbox

📬 Example Output (Plain Text)
Weekly Agentic AI Digest — 3 New Articles

- How Agentic AI is Reshaping Automation (2025-02-12)
  https://medium.com/...

- Building Autonomous Workflows with LLMs (2025-02-10)
  https://medium.com/...

- Designing Multi-Agent Architectures that Scale (2025-02-08)
  https://medium.com/...

🛠️ Local Development & Testing
1. Activate environment
conda activate agentic_env

2. Test SMTP
python smtp_test.py

3. Manual run
python medium_agent.py

🚢 Deployment (GitHub Actions)

Add all required secrets under:
Repo → Settings → Secrets and variables → Actions

Ensure the workflow file exists at:
.github/workflows/medium-agent.yml

Push changes and verify workflow under the Actions tab.

Trigger manually or wait for the weekly schedule.
