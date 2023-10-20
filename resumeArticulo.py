import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key=api_key


def resumirText(texto, tokens, temperatura, modelo="text-davinci-002"):
    prompt=f"Por favor resume el siguiente texto: {texto}"
    respuesta=openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        temperature=temperatura,
        max_tokens=tokens
    )

    return respuesta.choices[0].text.strip()

Original = input("Pega el texto que quieres resumir")
tokens = int(input("Cuantos tokens maximos tendra tu articulo? R: " ))
temperatura = int(input("Del 1 al 10 que tan creativo quieres que sea tu articulo? - R: ")) / 10
resumen = resumirText(Original, tokens, temperatura)
print(resumen)