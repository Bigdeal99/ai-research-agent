# tool.py

# import requests
# import os
# from dotenv import load_dotenv
# load_dotenv()
# API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")

def mock_paper_database():
    return [
        {
            "title": "Deep Learning Advances",
            "authors": ["Yann LeCun", "Geoffrey Hinton"],
            "year": 2019,
            "citations": 9000,
            "abstract": "A comprehensive overview of deep learning methods.",
            "link": "https://example.com/deep-learning"
        },
        {
            "title": "Transformers in NLP",
            "authors": ["Ashish Vaswani", "Jakob Uszkoreit"],
            "year": 2017,
            "citations": 20000,
            "abstract": "Introduction of the Transformer architecture.",
            "link": "https://example.com/transformers"
        },
        {
            "title": "Recent Trends in Machine Learning",
            "authors": ["Alice Researcher"],
            "year": 2021,
            "citations": 230,
            "abstract": "An updated look at ML trends post-2020.",
            "link": "https://example.com/ml-trends"
        },
        {
            "title": "Ethics in AI",
            "authors": ["Bob Ethical"],
            "year": 2023,
            "citations": 30,
            "abstract": "Discusses the ethical implications of artificial intelligence.",
            "link": "https://example.com/ethics-ai"
        }
    ]

def filter_by_year(paper, year_filter, year):
    if year_filter == "in":
        return paper["year"] == year
    elif year_filter == "before":
        return paper["year"] < year
    elif year_filter == "after":
        return paper["year"] > year
    return False

# def search_semantic_scholar(topic, year_filter, year, citations):
#     year_query = f"year:{year}" if year_filter == "in" else \
#                  f"year:>{year}" if year_filter == "after" else \
#                  f"year:<{year}"
#     query = f"{topic} {year_query}"

#     url = "https://api.semanticscholar.org/graph/v1/paper/search"
#     params = {
#         "query": query,
#         "limit": 1,
#         "fields": "title,year,authors,citationCount,abstract,url"
#     }
#     headers = {
#         "x-api-key": API_KEY
#     }

#     try:
#         response = requests.get(url, params=params, headers=headers)
#         response.raise_for_status()
#         data = response.json()

#         if not data["data"]:
#             return None

#         paper = data["data"][0]
#         if paper["citationCount"] < citations:
#             return None

#         return {
#             "title": paper["title"],
#             "authors": [a["name"] for a in paper["authors"]],
#             "year": paper["year"],
#             "citations": paper["citationCount"],
#             "abstract": paper.get("abstract", "No abstract available."),
#             "link": paper["url"]
#         }

#     except Exception as e:
#         print("Semantic Scholar API failed:", e)
#         return None
def search_paper(topic, year_filter, year, citations):
    # paper = search_semantic_scholar(topic, year_filter, year, citations)
    # if paper:
    #     return paper
    topic_lower = topic.lower()
    papers = mock_paper_database()

    for paper in papers:
        if (topic_lower in paper["title"].lower() or topic_lower in paper["abstract"].lower()) \
                and filter_by_year(paper, year_filter, year) \
                and paper["citations"] >= citations:
            return paper

    return {"error": "No paper found matching the criteria."}