import requests
from config import config
from logger import logger

class WebSearch:
    def __init__(self):
        self.enabled = config.WEB_SEARCH_ENABLED
        self.provider = config.SEARCH_PROVIDER
        self.api_key = config.SEARCH_API_KEY

    def search(self, query: str) -> str:
        if not self.enabled:
            return "Web search is disabled in configuration."

        logger.info(f"Performing web search query: {query}")
        # Placeholder / DuckDuckGo Instant Answer / Tavily integration
        try:
            # Basic non-API duckduckgo instant answer API demonstration
            url = f"https://api.duckduckgo.com/?q={query}&format=json"
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                data = res.json()
                abstract = data.get("AbstractText", "")
                if abstract:
                    return f"[Web Search Result]: {abstract}"
            return "[Web Search Result]: No instant answer available."
        except Exception as e:
            logger.error(f"Web search error: {e}")
            return f"Web search failed: {e}"

web_search = WebSearch()
