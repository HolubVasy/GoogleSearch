import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

# Hardcode the Tavily API key
tavily_api_key = "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"
print(f"Using API Key: {tavily_api_key}")

tavily_client = TavilyClient(api_key=tavily_api_key)

try:
    response = tavily_client.search(query="What is the capital of France?", search_depth="basic")
    print(f"Search successful!")
    print(f"Number of results: {len(response.get('results', []))}")
    print(f"First result title: {response['results'][0]['title'] if response['results'] else 'No results'}")
except Exception as e:
    print(f"Error occurred: {str(e)}")
