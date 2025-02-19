from langchain_community.utilities import SerpAPIWrapper
from langchain_community.tools import Tool
from config.settings import SERPAPI_API_KEY

search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)

search_tool = Tool(
    name = "google_search",
    func= search.run,
    description="Search the web using Google's API"
)