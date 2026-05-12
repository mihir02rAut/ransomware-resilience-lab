# Wazuh Setup Guide

## Steps
1. Install Wazuh on Ubuntu Server
2. Configure agent on Windows 10
3. Set manager IP to:
   192.168.56.10

## Enable FIM
Edit agent config:

<syscheck>
  <frequency>43200</frequency>
  <directories check_all="yes">C:\Users\Public\DData</directories>
</syscheck>

Restart the agent after changes.
