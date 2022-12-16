import os
import requests
import openai

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        openai.api_key = os.getenv("OPENAI_API_KEY")
        input_text = request.form["unsum_text"]
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=1024,
        n=1,
        temperature=0.8,
    )        
        print(response)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result )

@app.route('/question', methods=["GET", "POST"])
def question():
    if request.method == "POST":
        openai.api_key = os.getenv("OPENAI_API_KEY")
        grade = request.form['grade']
        subject = request.form['subject']

        completion = openai.Completion.create(
    engine="text-davinci-002",
    max_tokens=1024,
    prompt=f"generate 10 question of subject {subject} for grade {grade} students",
    temperature=0.8
)
        return redirect(url_for('question', quest =completion.choices[0].text))
    quest = request.args.get("quest")
    return render_template("question.html", quest = quest)



@app.route('/image',methods = ["GET"])
def image_gen():
    if request.method == "POST":
        r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': request.form['image'],
        },
        headers={'api-key': ''}
    )