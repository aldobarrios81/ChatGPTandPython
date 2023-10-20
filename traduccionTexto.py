import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key=api_key


def traducir_texto(texto, idioma, modelo="text-davinci-002"):
    prompt=f"traduce el siguiente texto {texto} al idioma {idioma}: \n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        temperature=0.5,
    )
    return respuesta.choices[0].text.strip()

miTexto = input("Ingresa el texto a traducir: ")
miIdioma = input("Ingresa el idioma a traducir: ")
traduccion = traducir_texto(miTexto, miIdioma)
print(traduccion)
