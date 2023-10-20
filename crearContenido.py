import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key=api_key

def crearContenido(tema, tokens, temperatura, modelo="text-davinci-002"):
    prompt=f"Por favor escribe un articulo corto sobre el tema {tema}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()


tema = input("Elije un tema para tu Articulo  - R: ")
tokens = int(input("Cuantos tokens maximos tendra tu articulo? R: " ))
temperatura = int(input("Del 1 al 10 que tan creativo quieres que sea tu articulo? - R: ")) / 10

articulo_Creado = crearContenido(tema, tokens, temperatura  )
print(articulo_Creado)