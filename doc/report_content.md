# Distinction-Level Report Content Draft

## 1. Introduction
Ransomware continues to represent one of the most disruptive cyber threats affecting modern organisations, not only because of its potential to compromise data, but because of its ability to interrupt business-critical services. This project was developed to evaluate cyber resilience rather than detection alone. It asks whether an organisation can continue to operate when suspicious activity is underway.

## 2. Research Problem
Many cyber security implementations generate alerts but do not directly measure whether essential services remain usable during an attack. This creates a disconnect between technical detection and operational resilience.

## 3. Aim
To evaluate cyber resilience by integrating SIEM-driven detection with API availability testing in a simulated ransomware scenario.

## 4. Objectives
- Build a safe ransomware-style simulation
- Implement Wazuh monitoring with FIM
- Develop automated API smoke tests
- Measure MTTD, MTTR, availability, and latency
- Produce strategic recommendations based on the findings

## 5. Literature Direction
The literature review should critically cover ransomware evolution, SIEM strengths and weaknesses, cyber resilience frameworks, and the gap between detection capability and service continuity measurement.

## 6. Method Summary
A quantitative experimental design is used. Controlled file activity is generated, Wazuh alerts are observed, and API smoke tests measure service behaviour throughout the event window.

## 7. Results Direction
The results section should present timestamps, alert evidence, smoke-test outcomes, uptime observations, and latency trends.

## 8. Discussion Direction
The discussion should move from descriptive findings to critical interpretation. Explain why detection alone is insufficient, how service continuity changes the evaluation of security effectiveness, and what this means for resilience strategy.

## 9. Conclusion Direction
Conclude that cyber security maturity should be assessed by a combination of detection quality, response readiness, and continuity of essential services.
