# AI Research Agent

This project is part of **Compulsory Assignment #2: AI Agents Using Autogen**.  
It implements an intelligent AI agent capable of finding research papers based on:

- A specific topic
- A publication year condition (in, before, or after)
- A minimum number of citations

The agent uses the **Autogen framework**, powered by **Mistral AI**, and is structured to support real research paper search via **Semantic Scholar API**.

---

## 🔧 Features

- ✅ CLI-based AI agent powered by Autogen and Mistral AI
- ✅ Simulated paper search tool with realistic mock data
- ✅ LLM-based Critic Agent that evaluates the agent’s response
- 🛠 Ready for Semantic Scholar API integration (API key pending)
- ✅ Separation of logic into modules (`main.py`, `tool.py`, `critic.py`)

---

## 📁 Project Structure

ai-research-agent/
├── main.py # Run the agent + critic
├── tool.py # Mock tool simulating real API logic
├── critic.py # LLM Critic evaluator class
├── config.py # Mistral LLM config (loads from .env)
├── .env # 🔒 API keys (excluded from Git)
├── .gitignore
└── requirements.txt


---

## 🚀 Setup Instructions

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate the virtual environment
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt


# 4. Run the Agent
python main.py
