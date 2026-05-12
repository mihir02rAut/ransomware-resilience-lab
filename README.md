# 🚨 Ransomware Resilience Lab: SIEM-Driven Detection & API Availability Evaluation

![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red?style=for-the-badge)
![SIEM](https://img.shields.io/badge/SIEM-Wazuh-blue?style=for-the-badge)
![API](https://img.shields.io/badge/API-FastAPI-green?style=for-the-badge)
![Automation](https://img.shields.io/badge/Automation-Python-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-black?style=for-the-badge)

# 📌 Project Overview

This project presents a cyber resilience evaluation framework that simulates ransomware-like activity within an isolated virtual lab and evaluates:

* Detection capability using SIEM (Wazuh)
* System availability using automated API smoke testing
* Organisational resilience through measurable performance metrics

Unlike traditional security projects focused purely on detection, this work evaluates a more important operational question:

> **Can critical services remain operational during an attack?**

# 🧠 This is NOT a normal project

This is a controlled cyber battlefield.

You do not just detect attacks here —
you evaluate whether systems can continue functioning during disruption.


# 🔥 What This Project Demonstrates

* Simulated ransomware activity inside a controlled environment
* Real-time SIEM monitoring and alerting
* API availability validation during attack conditions
* Automated smoke testing for operational continuity

> ⚡ Core Question:
> **“When systems are under attack, what still works?”**


# 🎯 Objectives

* Simulate ransomware-like behaviour in a controlled, ethical environment
* Monitor and detect anomalies using Wazuh SIEM
* Evaluate service availability through API health monitoring
* Measure MTTD (Mean Time to Detect) and MTTR (Mean Time to Respond)
* Connect technical findings to cyber resilience strategy and business continuity
* Align recommendations with recognised frameworks such as NIST CSF and ISO/IEC 27001


# 🏗️ System Architecture

```text
Host Machine (Windows 11)
│
├── Kali Linux (Attacker)
│        │
│        └── Simulated attack activity
│
├── Windows 10 (Victim)
│        │
│        └── File changes and endpoint telemetry
│
└── Ubuntu Server
         ├── Wazuh SIEM (alerting + FIM)
         └── FastAPI service (/status endpoint)
                  │
                  └── Smoke testing automation
```


# ⚙️ Technology Stack

| Layer          | Technology                      |
| -------------- | ------------------------------- |
| SIEM           | Wazuh                           |
| API            | FastAPI                         |
| Automation     | Python                          |
| Monitoring     | File Integrity Monitoring (FIM) |
| Virtualisation | VirtualBox                      |
| Reporting      | JSON + HTML                     |

# 🔬 Core Components

## 🧪 1. Safe Ransomware Simulation

* Simulates rapid file creation and modification activity
* Mimics ransomware indicators without destructive malware
* Generates observable behaviour for SIEM monitoring and response testing

## 📡 2. SIEM Monitoring (Wazuh)

* Real-time log analysis
* File Integrity Monitoring (FIM)
* Alert generation based on suspicious activity

## 🌐 3. API Availability Monitoring

```bash
GET /status
```

* Tracks service uptime
* Measures response latency during simulated attack activity
* Demonstrates whether a critical service remains operational during disruption


## 🤖 4. Automated Smoke Testing

* OpenAPI-based endpoint validation
* Repeated health checks against the API
* Generates:

  * `results.jsonl`
  * `report.html`

---

# 📊 Evaluation Metrics

| Metric           | Description                              |
| ---------------- | ---------------------------------------- |
| MTTD             | Time taken to detect suspicious activity |
| MTTR             | Time taken to respond and stabilise      |
| API Availability | Service uptime during attack activity    |
| Alert Accuracy   | Useful alerts vs false positives         |
| Latency          | Performance degradation during the event |

---

# 🚀 Quick Start

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

## 2. Start the API

```bash
uvicorn api.app:app --host 0.0.0.0 --port 8000
```

## 3. Run the simulation

```bash
python simulation/ransomware_simulator.py
```

## 4. Execute smoke tests

```bash
python automation/smoke_test.py
```

# 📁 Repository Structure

```text
ransomware-resilience-lab/
│
├── api/                         # FastAPI service under test
├── automation/                  # Smoke testing and reporting
├── simulation/                  # Safe ransomware activity simulation
├── wazuh/                       # Wazuh setup and configuration
├── docs/                        # Academic and project documentation
├── .github/workflows/           # CI workflow
├── README.md
├── requirements.txt
└── LICENSE
```

# 📚 Documentation

The `docs/` directory contains distinction-oriented academic content:

* `methodology.md`
* `architecture.md`
* `evaluation.md`
* `report_content.md`
* `presentation_notes.md`

# 📸 Evidence to Add

Add your screenshots inside:

```text
docs/screenshots/
```

Recommended screenshots:

* `wazuh-alerts.png`
* `fim-events.png`
* `api-status.png`
* `smoke-test-report.png`

# 🧠 Key Contribution

This project demonstrates that detection alone is not a sufficient measure of cybersecurity effectiveness.

A mature resilience strategy must evaluate:

* operational continuity
* service availability
* detection capability
* response effectiveness

during active cyber incidents.

# 🛡️ Ethical Design

* Fully isolated lab environment
* No real malware used
* No destructive encryption
* No impact on external systems
* Educational and research purposes only

# 🔮 Future Work

* AI-based anomaly detection
* SOAR integration
* Cloud-based SIEM deployment
* Richer telemetry datasets
* Comparative SIEM evaluation

# 👨‍💻 Author

**Mihir Raut**
MSc Cyber Security Management
Ravensbourne University London

# ⭐ Final Insight

> **A secure system detects attacks.
> A resilient system survives them.**
