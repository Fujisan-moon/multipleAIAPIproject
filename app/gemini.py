from google import genai

client = genai.Client()

response = client.models.generate_content(model="gemini-3-flash-preview", contents = "最近の金の価格動向について教えて")

print(response.text)