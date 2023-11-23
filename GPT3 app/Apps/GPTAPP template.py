import openai

# Définissez vos clés d'API OpenAI
openai.api_key = "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"

# Définissez la taille du modèle GPT-3 que vous souhaitez utiliser
model = "text-davinci-003"


while True : 


# Définissez la taille de la requête que vous souhaitez envoyer au modèle
    prompt =   "" + input(">>>  : ")

    # Envoyez la requête au modèle et affichez la réponse
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    print(response["choices"][0]["text"])
    print()