from huggingface_hub import InferenceClient

# Inicialitzem el client d'inferència amb el token d'Hugging Face
client = InferenceClient(
    provider="hf-inference",
    api_key="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",
)

# Model a utilitzar: Mistral-7B-Instruct
model_name = "mistralai/Mistral-7B-Instruct-v0.3"

log_entry = input ("Introdueix el log d'Apache per interpretar:\n")

# Formatar la pregunta per al model
instruction = "Quins errors hi ha en aquest log d'Apache?"
input_text = f"{instruction}\n\n{log_entry}"

# Realitzar la consulta (inferència) al model
completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    messages=[
        {
        "role": "user",
        "content": input_text,
        }
    ],
)

# Mostrar la resposta generada
print("Resposta del model:", completion.choices[0].message.content)
