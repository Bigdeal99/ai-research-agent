from autogen import AssistantAgent, UserProxyAgent
from config import LLM_CONFIG
from tool import search_paper


assistant = AssistantAgent(
    name="ResearchAgent",
    llm_config=LLM_CONFIG
)

task_input = {
    "topic": "machine learning",
    "year_filter": "after",   # Options: 'in', 'before', 'after'
    "year": 2020,
    "citations": 100
}

print("🔍 Searching for a paper with:")
print(f"- Topic: {task_input['topic']}")
print(f"- Year filter: {task_input['year_filter']} {task_input['year']}")
print(f"- Minimum citations: {task_input['citations']}\n")


paper = search_paper(**task_input)


if "error" in paper:
    print("❌ No suitable paper found.")
    print("Reason:", paper["error"])
else:
    print("✅ Research Paper Found:")
    print(f"Title: {paper['title']}")
    print(f"Authors: {', '.join(paper['authors'])}")
    print(f"Year: {paper['year']}")
    print(f"Citations: {paper['citations']}")
    print(f"Abstract: {paper['abstract']}")
    print(f"Link: {paper['link']}")
