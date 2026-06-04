from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

atividade = "musculação"
numeros_dias = 5
horas_dias = 1
prompt = f"Crie um plano de treino para um iniciante em {atividade} para {numeros_dias} dias, considerando que ele tem {horas_dias} horas para treinar por dia"

cliente = OpenAI(api_key=api_key)


resposta = cliente.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "Você é um personal trainer para iniciantes."
        },
        {
            "role": "user",
            "content": prompt
        }
    ])



print(resposta.choices[0].message.content)