from flask import request, render_template
from app import app
from flask_login import login_required
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask-ai", methods=["POST"])
@login_required
def ask_ai():
    query = request.form.get("query")
    response = openai.ChatCompletion.create(model="text-davinci-003", messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": query}])
    answer = response.choices[0].message['content']
    return render_template("response.html", answer=answer)
