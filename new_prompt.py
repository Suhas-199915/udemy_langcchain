from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
load_dotenv()

from linkedin_project.linkedin import scrape_linkedin

topic = "the history of the internet"
if __name__ == "__main__":
    summary_template = """
    given Linkdein information {information} about a person write 2 jokes about him/her.
    """

    summary_prompt = PromptTemplate(template=summary_template, input_variables=["topic"])

    llm = ChatMistralAI(model="mistral-large-latest",temperature=0.5)

    chain = summary_prompt|llm
    linkedin_data = scrape_linkedin("www.linkedin.com/in/suhas-kulkarni-aa5627221")

    response = chain.invoke(input={"information": linkedin_data})
    print(response.content)