# 🚨 Ransomware Resilience Lab: SIEM-Driven Detection & API Availability Evaluation

<<<<<<< HEAD
![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red?style=for-the-badge)
![SIEM](https://img.shields.io/badge/SIEM-Wazuh-blue?style=for-the-badge)
![API](https://img.shields.io/badge/API-FastAPI-green?style=for-the-badge)
![Automation](https://img.shields.io/badge/Automation-Python-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-black?style=for-the-badge)

## 📌 Project Overview

This project presents a cyber resilience evaluation framework that simulates ransomware-like activity within an isolated virtual lab and evaluates detection capability using Wazuh SIEM, system availability using automated API smoke testing, and organisational resilience through measurable performance metrics.

Unlike traditional security projects focused purely on detection, this work evaluates a more important operational question:

> **Can critical services remain operational during an attack?**

## 🎯 Objectives

- Simulate ransomware-like behaviour in a controlled, ethical environment
- Monitor and detect anomalies using Wazuh SIEM
- Evaluate service availability through API health monitoring
- Measure MTTD (Mean Time to Detect) and MTTR (Mean Time to Respond)
- Connect technical findings to cyber resilience strategy and business continuity
- Align recommendations with recognised frameworks such as NIST CSF and ISO/IEC 27001

## 🏗️ System Architecture

```text
=======
## 📌 Project Overview

This project presents a cyber resilience evaluation framework that simulates ransomware-like activity within an isolated virtual lab and evaluates:

Detection capability using SIEM (Wazuh)
System availability using automated API smoke testing
Organisational resilience through measurable performance metrics

Unlike traditional security projects focused purely on detection, this work evaluates:

“Can critical services remain operational during an attack?”

## 🧠 This is NOT a normal project.

This is a **controlled cyber battlefield**.

You don’t just detect attacks here —
you **watch systems survive them**.

## 🔥 What You’re About to See

* A simulated ransomware attack spreading inside a network
* A SIEM trying to detect it in real-time
* A service fighting to stay alive under pressure
* Automated tests checking if the system is still operational

> ⚡ Question this project answers:
> **“When everything is breaking… what still works?”**

## 🎯 Mission

Build a system that answers:

> **Detection ≠ Resilience**

So we measure:

* Can you detect it? ✔️
* Can you respond? ✔️
* But more importantly…
* 👉 **Can your system still function?**

## 🏗️ System Architecture

```id="6ojv8c"
>>>>>>> 6fe1009b6c741a828a95d11b65fd4aaad6a189ee
Host Machine (Windows 11)
│
├── Kali Linux (Attacker)
│        │
<<<<<<< HEAD
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

## ⚙️ Technology Stack

| Layer | Technology |
|------|-----------|
| SIEM | Wazuh |
| API | FastAPI |
| Automation | Python |
| Monitoring | File Integrity Monitoring (FIM) |
| Virtualisation | VirtualBox |
| Reporting | JSON + HTML |

## 🔬 Core Components

### 1. Safe Ransomware Simulation
- Simulates rapid file creation and modification activity
- Mimics ransomware indicators without using destructive malware
- Generates observable behaviour for SIEM monitoring and response testing

### 2. SIEM Monitoring (Wazuh)
- Real-time log analysis
- File Integrity Monitoring (FIM)
- Alert generation based on suspicious file activity

### 3. API Availability Monitoring
`GET /status`

- Tracks service uptime
- Measures response latency during simulated attack activity
- Demonstrates whether a critical service remains available during disruption

### 4. Automated Smoke Testing
- OpenAPI-based endpoint validation
- Repeated health checks against the API
- Report outputs in JSONL and HTML formats

## 📈 Evaluation Metrics

| Metric | Description |
|------|------------|
| MTTD | Time taken to detect suspicious activity |
| MTTR | Time taken to respond and stabilise |
| API Availability | Service uptime during the attack window |
| Alert Accuracy | Ratio of useful alerts to noise / false positives |
| Latency | Performance degradation during the event |

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the API
```bash
uvicorn api.app:app --host 0.0.0.0 --port 8000
```

### 3. Run the safe simulation
```bash
python simulation/ransomware_simulator.py
```

### 4. Run smoke tests
```bash
python automation/smoke_test.py
```

### 5. Review reports
- `automation/results.jsonl`
- `automation/report.html`

## 📁 Repository Structure

```text
ransomware-resilience-lab/
│
├── api/                         # FastAPI service under test
├── automation/                  # Smoke testing and report generation
├── simulation/                  # Safe ransomware-style activity generator
├── wazuh/                       # Wazuh setup and sample configuration
├── docs/                        # Report-ready academic documentation
├── .github/workflows/           # Optional CI workflow
├── README.md
├── requirements.txt
└── LICENSE
```

## 📚 Documentation

The `docs/` folder contains distinction-oriented write-ups you can adapt into your final report:
- `methodology.md`
- `architecture.md`
- `evaluation.md`
- `report_content.md`
- `presentation_notes.md`

## 📸 Evidence to Add

Place your real screenshots in `docs/screenshots/` and reference them in your report and README:
- `wazuh-alerts.png`
- `fim-events.png`
- `api-status.png`
- `smoke-test-report.png`

## 🧠 Key Contribution

This project demonstrates that detection alone is not a sufficient measure of cyber security effectiveness. A more mature resilience model evaluates whether essential services can remain available, whether monitoring can surface meaningful indicators quickly, and whether the organisation can respond in a structured and measurable way.

## 🛡️ Ethical Design

- Fully isolated lab environment
- No real malware used
- No destructive encryption
- No impact on external systems or networks
- Designed for research, portfolio, and educational use only

## 🔮 Future Work

- AI-based anomaly detection
- SOAR integration for automated response
- Cloud-based SIEM deployment
- Larger endpoint datasets and richer telemetry
- Comparative testing across multiple SIEM platforms

## 👨‍💻 Author

**Mihir Raut**  
MSc Cyber Security Management  
Ravensbourne University London

## ⭐ Final Insight

> **A secure system detects attacks. A resilient system survives them.**
=======
│        └── Simulated Attack
│
├── Windows 10 (Victim)
│        │
│        └── Logs + File Changes
│
└── Ubuntu Server
         ├── Wazuh SIEM (Detection + FIM)
         └── FastAPI Service (/status endpoint)
                  │
                  └── Smoke Testing Automation
```

## 🧱 Lab Setup (Realistic Environment)

⚙️ Technology Stack
| Layer          | Technology                      |
| -------------- | ------------------------------- |
| SIEM           | Wazuh                           |
| API            | FastAPI                         |
| Automation     | Python                          |
| Monitoring     | File Integrity Monitoring (FIM) |
| Virtualisation | VirtualBox                      |
| Reporting      | JSON + HTML                     |

```id="6ojv8c"
[ Kali Linux ]  --->  [ Windows 10 Victim ]  --->  [ Ubuntu SIEM + API ]
     Attack               Target Machine            Detection + Monitoring
```

* 🔴 Kali = attacker mindset
* 🟡 Windows = real endpoint behaviour
* 🟢 Ubuntu = brain of the system (SIEM + API)

## ⚙️ Stack That Powers This

* 🧠 Wazuh (SIEM + Detection Engine)
* ⚡ FastAPI (Service under attack)
* 🤖 Python (Automation + Simulation)
* 🔍 FIM (File Integrity Monitoring)
* 📊 JSON + HTML (Evidence + Reports)

## 💥 Core Modules

### 🧪 1. Controlled Ransomware Simulation

* No real damage (safe)
* Mimics:

  * File modifications
  * High-frequency writes
  * Suspicious patterns

### 📡 2. SIEM Detection Engine

* Real-time monitoring
* File Integrity Monitoring (FIM)
* Alert generation

### 🌐 3. Service Under Pressure

```id="ylk2y6"
GET /status
```

Simple endpoint.
But during attack → **this becomes everything.**

### 🤖 4. Smoke Testing System

* Automatically tests API health
* Outputs:

  * `results.jsonl`
  * `report.html`


## 📊 What You Measure (This is the gold)

| Metric          | Meaning               |
| --------------- | --------------------- |
| ⏱️ MTTD         | How fast you detect   |
| ⚡ MTTR          | How fast you respond  |
| 🌐 Availability | Is system still alive |
| 🎯 Accuracy     | Real alerts vs noise  |


## 🚀 Run The Chaos

### Start API

```bash id="5f1yiq"
cd api
uvicorn app:app --host 0.0.0.0 --port 8000
```

### API Availability Monitoring
```id="6ojv8c"
GET /status
```

### Trigger Attack

```bash id="9jfc8r"
cd simulation
python ransomware_simulator.py
```

### Test Survival

```bash id="6wdvlg"
cd automation
python smoke_test.py
```

### Watch SIEM

* Open Wazuh dashboard
* Observe alerts in real time

## 📸 Proof Section

* Wazuh alerts screenshot
* FIM logs
* API running during attack
* Smoke test report


## 🧠 What This Project REALLY Shows

This is not about tools.

This shows:

* You understand **real attack behaviour**
* You can build **defensive systems**
* You think in terms of **business continuity**
* You measure **what actually matters**

## 🛡️ Ethics (Important)

* Fully isolated lab
* No real malware
* No external impact


## 👨‍💻 Built By

**Mihir Raut**
Cybersecurity Engineer in the making at 
Ravensbourne University London


## ⚡ Final Thought

Most projects ask:

> “Can you detect the attack?”

This one asks:

> **“Can your system survive it?”**

## 🧠 If You're Reviewing This

You’re not just looking at a project.

You’re looking at:

* A **mini SOC lab**
* A **resilience testing framework**
* A **future security engineer mindset**
>>>>>>> 6fe1009b6c741a828a95d11b65fd4aaad6a189ee
