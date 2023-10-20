import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key=api_key
preguntas_anteriores=[]
respuestas_anteriores=[]

def preguntar_chat_gpt(prompt, modelo="text-davinci-002"):
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=150,
        temperature=0.5
    )
    return respuesta.choices[0].text.strip()

print("Bienvenidos a nuestro chatbot basico. Escribe 'Salir' cuando quieras terminar")

while True:
    conversacion_historica=""
    ingreso_usuario = input("\nTú:")
    if ingreso_usuario.lower() == "salir":
        break
    
    for pregunta, respuesta  in zip(preguntas_anteriores,respuestas_anteriores):
        conversacion_historica += f"El usuario pregunta {pregunta}\n"
        conversacion_historica += f"ChatGPT Responde: {respuesta}\n"

    prompt = f"El usuario pregunta: {ingreso_usuario}"
    conversacion_historica += prompt
    respuestaGTP = preguntar_chat_gpt(conversacion_historica)
    print(f" {respuestaGTP}")
    
    preguntas_anteriores.append(ingreso_usuario)
    respuestas_anteriores.append(respuestaGTP)
        

