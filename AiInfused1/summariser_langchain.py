import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from scrapper import fetch_website_contents

# from pathlib import Path
# import sys

# PROJECT_ROOT = Path.cwd()
# print(PROJECT_ROOT)
# sys.path.append(str(PROJECT_ROOT / "AiInfused1"))



load_dotenv()
prompt = ChatPromptTemplate.from_template(
    "Give a short, friendly summary of this website:\n\n{website}")

model  = ChatOpenAI(
  api_key=os.getenv("GROQ_API_KEY"),
  base_url="https://api.groq.com/openai/v1",
  model="openai/gpt-oss-120b",
  temperature=0.3
)

parser = StrOutputParser()    

chain = prompt | model | parser

def summarize(url):
    return chain.invoke({"website": fetch_website_contents(url)})

# print(summarize("https://www.vcluster.com/"))

