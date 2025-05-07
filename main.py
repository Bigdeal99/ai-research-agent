from autogen import AssistantAgent, UserProxyAgent
from config import LLM_CONFIG
from tool import search_paper

# Create the assistant agent
assistant = AssistantAgent(
    name="ResearchAssistant",
    llm_config=LLM_CONFIG
)

# Simulated user input
task_input = {
    "topic": "machine learning",
    "year_filter": "after",  # 'in', 'before', or 'after'
    "year": 2020,
    "citations": 100
}

# Optional: Print what the agent is doing
print("🔍 Searching for paper matching:", task_input)

# Use the dummy tool
paper = search_paper(**task_input)

# Print results
print("\n📄 Found Research Paper:")
print(f"Title: {paper['title']}")
print(f"Authors: {', '.join(paper['authors'])}")
print(f"Year: {paper['year']}")
print(f"Citations: {paper['citations']}")
print(f"Abstract: {paper['abstract']}")
print(f"Link: {paper['link']}")
