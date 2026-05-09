import google.generativeai as genai # type: ignore

# Use sua chave de API aqui
GOOGLE_API_KEY=""
genai.configure(api_key=GOOGLE_API_KEY)

# Escolha o modelo que deseja usar
model = genai.GenerativeModel('gemini-2.0-flash')

# Envie um prompt
pergunta = input("Faça uma pergunta: ")
response = model.generate_content(pergunta)

# Imprima a resposta
print(response.text)
