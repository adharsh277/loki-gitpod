 📦 Real-Time Logging Stack using Docker, Loki, Promtail, Grafana & GitHub Actions

![Docker](https://img.shields.io/badge/Docker-Containerization-blue?logo=docker)
![Loki](https://img.shields.io/badge/Loki-Log%20Aggregation-purple?logo=grafana)
![Promtail](https://img.shields.io/badge/Promtail-Log%20Collector-orange?logo=grafana)
![Grafana](https://img.shields.io/badge/Grafana-Visualization-yellow?logo=grafana)
![CI/CD](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-green?logo=githubactions)
![DevOps](https://img.shields.io/badge/DevOps-Practices-informational?logo=dev.to)

---

## 📌 Project Overview

This project demonstrates a **containerized centralized logging system** using **Grafana Loki**, **Promtail**, and **Grafana**, deployed via **Docker Compose** and automated using **GitHub Actions CI/CD**. Logs are collected from a sample app and visualized in real-time using Grafana dashboards.

Ideal for **DevOps engineers** learning log aggregation, CI/CD, and monitoring practices.

---

## 🚀 What I Learned

- 🐳 Docker multi-service orchestration using `docker-compose`
- 🔍 Centralized **log aggregation** with Loki + Promtail
- 📊 Dashboard-based log visualization via Grafana
- 🔁 CI/CD integration using **GitHub Actions**
- 🛠️ Linux CLI, YAML automation, and Git workflows
- 🌐 Exposing & querying logs through RESTful endpoints

---

## 🧰 Tech Stack

| Layer              | Tools / Tech                         |
|-------------------|---------------------------------------|
| **Logging Agent**   | Promtail                            |
| **Log Store**       | Grafana Loki                        |
| **Visualization**   | Grafana                             |
| **CI/CD**           | GitHub Actions                      |
| **Containerization**| Docker, Docker Compose              |
| **Monitoring**      | Loki Queries via REST API           |
| **DevOps Skills**   | CI/CD, Observability, Infrastructure-as-Code |

---

## 🏗️ Project Structure

``bash
loki-gitpod/
├── app/
│   └── app.py                  # Simple app generating logs
├── promtail-config.yml         # Promtail scraping config
├── docker-compose.yml          # Service definitions
├── .github/
│   └── workflows/
│       └── docker.yml          # GitHub Actions pipeline
└── README.md                   # This file

## ⚙️ Run the Project Locally
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/adharsh277/loki-gitpod.git

## 2️⃣ Start Logging Stack
bash
Copy
Edit
docker-compose up --build
📦 Sample App Logs: stdout
🔭 Loki: http://localhost:3100
📈 Grafana: http://localhost:3001 (Login: admin / admin)
📝 Explore → Query {filename="/var/log/app.log"} or job="sample-app"

## 🔁 GitHub Actions CI/CD
This project includes a CI/CD pipeline configured using GitHub Actions:

✅ Triggers on push to main

🐳 Builds Docker images for all services

🚀 Launches services and checks Loki availability

🔍 Queries log labels to confirm ingestion

🧹 Shuts down services after validation

## 📂 Workflow File: .github/workflows/docker.yml
Key steps:

yaml
Copy
Edit
- uses: actions/checkout@v3
- run: docker compose up -d --build
- run: curl http://localhost:3100/ready
- run: curl http://localhost:3100/loki/api/v1/labels
- run: docker compose down
- 
## 📸 Screenshots
📊 Grafana Log Explorer
(Add screenshots here if available)


🧩 Loki Labels Queried

## 📚 Resources
Grafana Loki Documentation

Promtail Configuration

GitHub Actions Docs

Docker Compose Docs

## 👨‍💻 Author
Adharsh U
Cloud & DevOps Enthusiast
🔗 GitHub Profile

## ⭐ Final Note
This project is an excellent demonstration of DevOps principles, combining containerization, observability, and CI/CD in a practical and production-ready format.
Feel free to fork, contribute, or reach out if you found it helpful!

yaml
Copy
Edit

cd loki-gitpod
