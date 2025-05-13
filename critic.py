from autogen import AssistantAgent
import json
import re

class CriticEvaluator:
    def __init__(self, llm_config):
        self.critic = AssistantAgent(
            name="CriticAgent",
            llm_config=llm_config
        )

    def evaluate(self, task_input, paper):
        if "error" in paper:
            return {"feedback": "No evaluation — agent failed to find a paper."}

        prompt = f"""
Evaluate the AI agent’s performance in retrieving a research paper for the following task:

User Query:
Topic: {task_input['topic']}
Year filter: {task_input['year_filter']} {task_input['year']}
Minimum citations: {task_input['citations']}

Agent Response:
Title: {paper['title']}
Year: {paper['year']}
Citations: {paper['citations']}
Abstract: {paper['abstract']}

Rate the agent on:
- Completeness (1–5): Did the response meet all the user’s requirements?
- Quality (1–5): Is the result clearly presented and appropriate?
- Robustness (1–5): Would the agent perform well on challenging inputs?
- Specificity (1–5): Is the result well-justified and detailed?
- Consistency (1–5): Would the result be repeatable on similar prompts?

IMPORTANT: Return only valid JSON. Do NOT include ```json or extra text.
Return your result as:
- completeness
- quality
- robustness
- specificity
- consistency
- feedback (brief explanation)
        """

        
        response = self.critic.generate_reply([{"role": "user", "content": prompt}])
        response_text = response.get("content", "")

        
        match = re.search(r'{[\s\S]*}', response_text)
        if match:
            json_str = match.group(0)
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                return {"feedback": "❌ Failed to parse JSON", "raw": json_str}
        else:
            return {"feedback": "❌ No valid JSON found", "raw": response_text}
