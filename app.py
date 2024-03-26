from flask import Flask, render_template, request
from stories import Story, story, StoryList, storyList

app = Flask(__name__)


@app.route('/<id>', methods=['GET', 'POST'])
def displayFillForm(id: str):

    if request.method == 'POST':
        answers = request.form
        story = storyList.find(id)
        result = story.generate(answers)
        return render_template('result.html', story=story, result=result, title="Result")

    story = storyList.find(id)
    return render_template('form.html', story=story, title="Form")


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        # process new story
        return render_template('stories.html', stories=storyList)
    else:
        return render_template('new.html', story=Story(""), title="New")


@app.route('/')
def displayStories():
    return render_template('stories.html', stories=storyList, title="All Stories")
