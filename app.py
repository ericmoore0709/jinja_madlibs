from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)


@app.route('/', methods=['GET'])
def displayForm():
    return render_template('form.html', story=story, title="Form")


@app.route('/', methods=['POST'])
def processForm():
    answers = request.form
    result = story.generate(answers)
    return render_template('result.html', result=result, title="Result")
