import os
import openai
import spacy
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

##modelos=openai.Model.list()
##print(modelos)
modelo = "text-davinci-002"
prompt="Cuenta una historia breve"

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=1,
    # temperature=0.1
    max_tokens=100
)
texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)

# for idx, opcion in enumerate(respuesta.choices):
#     texto_generado=opcion.text.strip()
#     print(f"Respuesta {idx + 1}: {texto_generado}\n")

print("***")

modelo_spacy = spacy.load("es_core_news_md")
analisis = modelo_spacy(texto_generado)

# for token in analisis:
#     print(token.text, token.pos_, token.dep_, token.head.text)

# print("%%%%%%%%%%%%%%%%")

# for ent in analisis.ents:
#     print(ent.text, ent.label_)


ubicacion = None


for ent in analisis.ents:
    if ent.label_ == "LOC":
        ubicacion = ent
        break

if ubicacion:
    enunciado=f"Dime más acerca de {ubicacion}"
    response2 = openai.Completion.create(
    engine=modelo,
    prompt=enunciado,
    n=1,
    max_tokens=100
)
    print(response2.choices[0].text.strip())