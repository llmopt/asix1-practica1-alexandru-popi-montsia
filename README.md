# ASIX_DAW_IA
Testeig de models d'IA i primeres aplicacions.

## Pregunta-li a una IA com utilitzar el model Mistral-7B-Instruct (o un equivalent) de hugging face per a interpretar logs del Apache web server, realitzant un programa amb python. Realitza el programa i testeja’l.

Abans d’executar cap prova assegurat de saber quants recursos hardware utilitzarà, i valora si convé o no executar-lo. Si no convé executar-lo, tracta de buscar altra opció. 

Si no es viable usar aquest model, intenteu usar-ne d’altre.

Lliureu la conversa amb la IA, el programa python que heu creat i el test que heu realitzat.

## Explicació de Paraules Claus
- RAG (Retrieval Augmented Generation): És una tècnica de processament del llenguatge natural (NLP) que combina els punts forts dels models d'intel·ligència artificial basada en recuperació i generativa (IA), aixó permet a la IA recuperar informació rellevant per millorar les seves respostes generades.

- Fine-Tuned: El procés de prendre un model d'aprenentatge automàtic preentrenat i la formació contínua en un conjunt de dades més petit i dirigit.

- Temperature: Defineix la previsibilitat de la seva sortida. Les temperatures més altes produeixen resultats més creatius, mentre que les temperatures més baixes produeixen respostes més predictibles.

## Com executar l'API
- Crear un compte en [HuggingFace](https://huggingface.co/)

- Crear un token
![image](https://github.com/user-attachments/assets/86fff3a8-3312-490d-ae1f-dcb936b42d85)

- Inserim el token dins del script de Python

## Posada en marxa del fitxer "IA.py":
- Clonem el repositori:
  "git clone https://github.com/llmopt/asix1-practica1-alexandru-popi-montsia"

- Entrem dins del directori:
  "cd asix1-practica1-adamoughriss"

- Executem el script:
  "python3 IA.py"

## Resultat del test de l'IA
- Log proporcionat:
  "[Tue May 20 10:04:31.525155 2025] [mpm_event:notice] [pid 68661:tid 140321180847168] AH00489: Apache/2.4.41 (Ubuntu) configured -- resuming normal operations"
  "[Tue May 20 10:04:31.525799 2025] [core:notice] [pid 68661:tid 140321180847168] AH00094: Command line: '/usr/sbin/apache2'"

- Contestació donada per part de l'IA:
  "The log you provided is a normal Apache startup log, indicating that the server (Apache/2.4.41, running on Ubuntu) has been configured and is resuming normal
  operations. There are no errors in this log. However, it's worth noting that the date mentioned in the log seems to be from the future (May 20, 2025), which may
  be a mistake or a placeholder.

  Normally, session errors, internal server errors, or other issues would be prefaced with the text [error] instead of [notice], as in the case of Apache/2.4.41
  (Ubuntu) AH00526: Syntax error on line 123 of /etc/apache2/apache2.conf:
  Invalid command 'Fnord', despite this log line being syntactically correct, it would still be an error if found in an actual configuration file."

## Diferències entre Descarregar el Model i utilitzar l'API
| Característica             | **Model en Client (Descarregat)**                      | **Importació de l'API (Servei remot)**       |
| -------------------------- | ------------------------------------------------------ | -------------------------------------------- |
| **Accés a Internet**       | No necessari un cop descarregat                        | Necessari per cada petició                   |
| **Rendiment (latència)**   | Més ràpid, sense connexió externa                      | Pot ser més lent per latència de xarxa       |
| **Control sobre el model** | Total, es pot modificar, ajustar o entrenar            | Limitat al que ofereix el proveïdor          |
| **Actualitzacions**        | Manual (cal tornar a descarregar el model actualitzat) | Automàtiques, gestionades pel proveïdor      |
| **Cost**                   | Cost únic, infraestructura pròpia                      | Cost recurrent (per ús, subscripció)         |
| **Facilitat d'integració** | Pot requerir més configuració tècnica                  | Fàcil, només cal fer crides a l'API          |
| **Privadesa de dades**     | Màxima, les dades no surten del dispositiu             | Risc de privadesa si s’envien dades al núvol |
| **Escalabilitat**          | Limitada al maquinari local                            | Alta, gestionada pel proveïdor del servei    |
