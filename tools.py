from langchain.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
load_dotenv()
def get_search_results(name:str):
    search = TavilySearchResults()
    result = search.run(f"{name}")
    return result