from ddgs import DDGS
from langchain_core.tools import tool


@tool
def web_search(query: str) -> str:
    """
    Search the web for information related to the user's query.
    Use this tool when current or external information is required.
    """

    results = DDGS().text(
        query,
        max_results=5
    )

    if not results:
        return "No search results found."

    formatted_results = []

    for result in results:
        formatted_results.append(
            f"Title: {result.get('title', '')}\n"
            f"URL: {result.get('href', '')}\n"
            f"Snippet: {result.get('body', '')}"
        )

    return "\n\n".join(formatted_results)