# ASIX_DAW_IA
Testeig de models d'IA i primeres aplicacions.


## Pregunta-li a una IA com utilitzar el model Mistral-7B-Instruct (o un equivalent) de hugging face per a interpretar logs del Apache web server, realitzant un programa amb python. Realitza el programa i testeja’l.

Abans d’executar cap prova assegurat de saber quants recursos hardware utilitzarà, i valora si convé o no executar-lo. Si no convé executar-lo, tracta de buscar altra opció. 

Si no es viable usar aquest model, intenteu usar-ne d’altre.

Lliureu la conversa amb la IA, el programa python que heu creat i el test que heu realitzat.


# Explicació de Paraules Claus
- RAG (Retrieval Augmented Generation): És una tècnica de processament del llenguatge natural (NLP) que combina els punts forts dels models d'intel·ligència artificial basada en recuperació i generativa (IA), aixó permet a la IA recuperar informació rellevant per millorar les seves respostes generades.

- Fine-Tuned: El procés de prendre un model d'aprenentatge automàtic preentrenat i la formació contínua en un conjunt de dades més petit i dirigit.

- Temperature: Defineix la previsibilitat de la seva sortida. Les temperatures més altes produeixen resultats més creatius, mentre que les temperatures més baixes produeixen respostes més predictibles.



# Diferències entre Descarregar el Model i utilitzar l'API



# Posada en marxa del fitxer IA.py

















# 🤖 Exemple bàsic d'ús de BlenderBot amb Hugging Face Transformers

Aquest exemple mostra com utilitzar el model [`facebook/blenderbot-400M-distill`](https://huggingface.co/facebook/blenderbot-400M-distill) per generar respostes a preguntes o missatges de l'usuari, utilitzant el `pipeline` de Hugging Face.

## 📦 Requisits

Assegura't de tenir instal·lades les dependències següents:

```bash
pip install transformers torch
```

## 📜 Codi complet

```python
from transformers import pipeline

# Inicialitzem el pipeline amb BlenderBot
# https://huggingface.co/facebook/blenderbot-400M-distill
chatbot = pipeline(task="text2text-generation", model="facebook/blenderbot-400M-distill")

# Missatge de l'usuari
user_message = """
What are some fun activities I can do in the winter?
"""

# Enviem el missatge al model i generem resposta
output = chatbot(user_message)

# Mostrem la resposta generada
print("Bot:", output[0]["generated_text"])
```

## 🔍 Explicació del funcionament

### 1. `chatbot = pipeline(...)`

Aquesta línia crea un objecte de tipus `Text2TextGenerationPipeline`, especialitzat en tasques de generació de text a partir de text (`text2text-generation`).

El model que s'utilitza és `facebook/blenderbot-400M-distill`, un model preentrenat per mantenir converses.

### 2. Què és `chatbot`

`chatbot` és un objecte que es pot cridar com una funció perquè implementa el mètode especial `__call__()`.

Gràcies a això, pots fer:

```python
output = chatbot(user_message)
```

### 3. Què fa `chatbot(user_message)`?

- Tokenitza el text d'entrada.
- El passa pel model preentrenat.
- Des-tokenitza la sortida i la retorna en una llista de diccionaris, on cada diccionari conté la clau `"generated_text"` amb la resposta generada.

**Exemple de sortida:**

```python
[{'generated_text': 'You can go skiing, ice skating, or drink hot chocolate by the fire.'}]
```

### 4. `print("Bot:", output[0]["generated_text"])`

Accedeix a la primera (i única) resposta generada i imprimeix el contingut textual.

## ✅ Resultat esperat

```
Bot: You can go skiing, ice skating, or drink hot chocolate by the fire.
```
