from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

atividade = "calistenia"
numeros_dias = 5
horas_dias = 1

prompt = f"Crie um plano de treino de {atividade} para {numeros_dias} dias, com duração de {horas_dias} horas por dia."

modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key
)

resposta = modelo.invoke(prompt)
print(resposta.content)