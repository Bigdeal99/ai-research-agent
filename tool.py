def search_paper(topic, year_filter, year, citations):
    """
    Dummy function that simulates a research paper search.
    In real version, call Semantic Scholar API or similar.
    """
    return {
        "title": f"Recent Trends in {topic.title()}",
        "authors": ["Alice Researcher", "Bob Scientist"],
        "year": 2022,
        "citations": 245,
        "abstract": f"This paper explores advances in {topic}.",
        "link": "https://example.com/research-paper"
    }
