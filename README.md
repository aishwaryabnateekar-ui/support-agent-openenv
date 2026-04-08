# support-agent-openenv
OpenEnv-based reinforcement learning environment for simulating real-world customer support workflows including ticket classification, priority assignment, and automated resolution.

# 🚀 Support Agent OpenEnv Environment

## 📌 Overview
This project simulates a real-world customer support system where an AI agent handles user issues step-by-step.

## 🎯 Tasks
1. **Classification (Easy)**  
   Identify the type of issue (e.g., billing issue)

2. **Priority Assignment (Medium)**  
   Assign urgency (high/low)

3. **Resolution (Hard)**  
   Respond and resolve the issue completely

## ⚙️ Environment Design
- Observation: Customer ticket
- Actions:
  - classify
  - set_priority
  - respond
  - resolve
- Rewards:
  - Classification: +0.3
  - Priority: +0.2
  - Response: +0.4
  - Resolve: +0.5
  - Invalid action: -0.2

## 🧪 Running the Project

```bash
docker build -t support-env .
docker run support-env
