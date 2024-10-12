import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
    RESULTS_PER_PAGE = 15