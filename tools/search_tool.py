from langchain_community.tools import SerpAPIWrapper
from langchain_community.tools import Tool
from config.settings import SERP_API_KEY

search = SerpAPIWrapper(api_key=SERP_API_KEY)

search_tool = Tool(
    name = "google_search",
    func= search.run,
    description="Search the web using Google's API"
)