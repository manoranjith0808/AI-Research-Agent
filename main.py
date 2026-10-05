from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from tools import web_search

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash",temperature=0)
tools=[web_search]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are a research assistant that helps generate research papers.

    Answer the user's query clearly and accurately.

    Provide:
    - The research topic
    - A concise summary
    - Sources used
    - Tools used
    """,
    response_format=ResearchResponse
)
query=input("What can I help you research?")
response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": query
        }
    ]
})

result = response["structured_response"]
print(result)
