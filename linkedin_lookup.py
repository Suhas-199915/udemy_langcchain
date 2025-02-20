import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (create_react_agent, AgentExecutor)
from langchain import hub
from langchain.tools.tavily_search import TavilySearchResults
import ssl

ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL
def get_search_results(name:str):
    search = TavilySearchResults()
    result = search.run(f"{name}")
    return result
def linkedin_lookup(name:str)->str:
    llm = ChatMistralAI(temperature=0.5, model="mistral-large-latest")
    template = """Given the full name of the person {fullname}, I want you to get the link to their Linkedin profile page. Your answer should contain only the URL."""
    
    prompt_template = PromptTemplate(template=template, input_variables=["fullname"])
    tools_for_agent = [Tool(name= "Crawl google for a linkedin profile",
                           func= get_search_results,
                           description = "useful for when you want to get the Linkedin profile page url",
                           )]
    
    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm = llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    
    result = agent_executor.invoke(
        input= {"input":prompt_template.format_prompt(fullname = name)}
    )
    linkedin_url = result['output']
    return linkedin_url

if __name__ == "__main__":
    load_dotenv()
    linkedin_url = linkedin_lookup(name="Suhas Kulkarni")
    print (linkedin_url)
