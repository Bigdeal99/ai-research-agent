from autogen import AssistantAgent, UserProxyAgent
from config import LLM_CONFIG
from tool import search_paper
from critic import CriticEvaluator
import json


assistant = AssistantAgent(
    name="ResearchAgent",
    llm_config=LLM_CONFIG
)



task_input = {
    "topic": "ethics",
    "year_filter": "in",
    "year": 2023,
    "citations": 20
}
# 1. combinations 

# task_input = {
#     "topic": "transformers",
#     "year_filter": "before",
#     "year": 2019,
#     "citations": 1000
# }

# fail combination

# task_input = {
#     "topic": "quantum computing",
#     "year_filter": "after",
#     "year": 2020,
#     "citations": 500
# }


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
    
critic = CriticEvaluator(LLM_CONFIG)
evaluation = critic.evaluate(task_input, paper)

print("\n🤖 Critic Evaluation:")
for key, value in evaluation.items():
    print(f"{key.capitalize()}: {value}")

with open("evaluation_log.json", "a") as f:
    f.write(json.dumps(evaluation, indent=2))
    f.write("\n\n")