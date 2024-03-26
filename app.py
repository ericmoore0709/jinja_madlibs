from flask import Flask, render_template, request
from stories import Story, story, StoryList, storyList

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        answers = request.form
        result = story.generate(answers)
        return render_template('result.html', result=result, title="Result")
    else:
        return render_template('form.html', story=story, title="Form")


@app.route('/<id>')
def displayFillForm(id: str):
    story = storyList.find(id)
    return render_template('form.html', story=story, title="Form")


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        # process new story
        return render_template('stories.html', stories=storyList)
    else:
        return render_template('new.html', story=Story(""), title="New")


@app.route('/stories')
def displayStories():
    return render_template('stories.html', stories=storyList, title="All Stories")
