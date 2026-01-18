from flask import Flask, render_template, request
from .gemini import returnAIresponse

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    question = None
    answer = None

    if request.method == "POST":
        question = request.form.get("question")
        if question:
            answer = returnAIresponse(question)

    return render_template("index.html", question=question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)