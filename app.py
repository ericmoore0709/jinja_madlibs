from flask import Flask, render_template, request
from stories import Story, story

app = Flask(__name__)

@app.route('/', methods=['GET'])
def displayForm():
    return render_template('form.html', prompts=story.prompts)

@app.route('/', methods=['POST'])
def processForm():
    answers = request.form
    result = story.generate(answers)
    print(result)
    return render_template('result.html', result=result)