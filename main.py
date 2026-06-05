from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

atividade = "calistenia"
numeros_dias = 5
horas_dias = 1

modelo_de_prompt = PromptTemplate(
    template=""""
        Crie um plano de treino de {atividade} para {dias} dias, com duração de {horas_dias} horas por dia.
    """
)

prompt = modelo_de_prompt.format(
    atividade=atividade,
    dias=numeros_dias,
    horas_dias=horas_dias
)

print(f"Prompt : \n", prompt)


modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key
)

resposta = modelo.invoke(prompt)
print(resposta.content)