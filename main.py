from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from pydantic import Field, BaseModel
from dotenv import load_dotenv
from langchain.globals import set_debug
import os

set_debug(True)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


class Receita(BaseModel):
    receita:str = Field("A receita a ser feita")
    recomendada:str = Field("Para quem é recomendada a receita (Perder peso, ganhar massa, etc.)")

parseador = JsonOutputParser(pydantic_object=Receita)


prompt_receita = PromptTemplate(
    template=""""
      Sugira receitas para perder peso. Dado meu interesse por {interesse}.
      {formato_de_saida}
    """,

    input_variables=["interesse"],
    partial_variables={"formato_de_saida": parseador.get_format_instructions()}
)


modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key
)

cadeia = prompt_receita | modelo | parseador

resposta = cadeia.invoke(
    {"interesse": "frutas"}
)
print(resposta)