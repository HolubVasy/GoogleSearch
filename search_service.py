import requests
from config import Config

class SearchService:
    def __init__(self):
        self.api_key = Config.TAVILY_API_KEY
        self.base_url = "https://api.tavily.com/search"

    def search(self, query, page=1):
        params = {
            "api_key": self.api_key,
            "query": query,
            "page": page,
            "max_results": Config.RESULTS_PER_PAGE
        }
        response = requests.get(self.base_url, params=params)
        return response.json()