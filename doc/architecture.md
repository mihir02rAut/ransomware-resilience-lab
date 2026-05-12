# Architecture

## Overview
The architecture was intentionally kept small enough for academic implementation while still representing a realistic defensive workflow.

```text
Kali Linux  --->  Windows 10  --->  Ubuntu Server
  attack         monitored        Wazuh + FastAPI
 simulation       endpoint           SIEM/API
```

## Component Roles
### Kali Linux
Used to represent an attacker perspective or a host from which controlled simulation workflows may be launched.

### Windows 10 Endpoint
Acts as the primary monitored endpoint. File activity on a designated folder is captured by the Wazuh agent and forwarded to the manager.

### Ubuntu Server
Hosts the Wazuh stack and the FastAPI service used for availability validation.

## Design Rationale
This design supports both detection-oriented and resilience-oriented analysis. Instead of asking only whether malicious behaviour is detected, the architecture also allows measurement of whether a critical service remains responsive while the event unfolds.
