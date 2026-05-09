from google import genai

client = genai.Client(api_key="coloque a chave aqui")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Crie um personagem que tenha um nome, nivel, pontuação de 0 a 100 no formato json"
)
print(response.text)