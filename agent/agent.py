from langchain_google_genai import ChatGoogleGenerativeAI  # ✅ Correct import
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from config.settings import GOOGLE_API_KEY
from tools.search_tool import search_tool
from tools.math_tool import math_tool

# ✅ Create the correct Gemini LLM instance
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

# ✅ Initialize memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# ✅ Define tools
tools = [search_tool, math_tool]

# ✅ Initialize the agent with correct LLM instance
agent_executor = initialize_agent(
    tools=tools,
    llm=llm,  # ✅ Make sure this is an actual LLM instance
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
)

# ✅ Function to run the agent
def run_agent(query):
    return agent_executor.run(query)
