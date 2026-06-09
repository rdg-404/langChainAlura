from langchain.schema import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")



prompt_receita = PromptTemplate(
    template=""""
      Sugira receitas para perder peso. Dado meu interesse por {interesse}
    """,
    input_variables=["interesse"]
)


modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key
)

cadeia = prompt_receita | modelo | StrOutputParser()

resposta = cadeia.invoke(
    {"interesse": "frutas"}
)
print(resposta)