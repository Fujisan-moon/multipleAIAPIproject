from flask import Flask
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def returnAIresponse():
    client = genai.Client()
    response = client.models.generate_content(model="gemini-3-flash-preview", contents = "最近の金の価格動向について教えて")
    return response.text
app
if __name__ == '__main__':
    app.run()