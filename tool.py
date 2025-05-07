# tool.py
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

def search_paper(topic, year_filter, year, citations):
    """
    Simulates a real research paper API by filtering mock data.
    """
    topic_lower = topic.lower()
    papers = mock_paper_database()

    for paper in papers:
        if (topic_lower in paper["title"].lower() or topic_lower in paper["abstract"].lower()) \
                and filter_by_year(paper, year_filter, year) \
                and paper["citations"] >= citations:
            return paper

    return {"error": "No paper found matching the criteria."}