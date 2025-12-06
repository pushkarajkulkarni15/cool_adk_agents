from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="google_search",
    model="gemini-2.5-flash",
    description=("This agent uses google search to answer user queris"),
    instruction=("You are a search engine which uses google_search tool to answer user queries in most descriptive way."),
    tools=[google_search]
)