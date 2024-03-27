from flask import Flask, render_template, request, redirect
from stories import Story, story, StoryList

app = Flask(__name__)

storyList = StoryList()
storyList.addStory(story)


@app.route('/<id>', methods=['GET', 'POST'])
def id(id: str):

    if request.method == 'POST':
        form = request.form
        id = form['id']
        answers = {key: value for key, value in form.items() if key != 'id'}
        story = storyList.find(id)

        error_messages = []

        for prompt, answer in answers.items():
            if not answer:
                error_messages.append(f'{prompt} cannot be blank.')

        if error_messages:
            return render_template('form.html', story=story, title="Form", errors=error_messages)

        story = storyList.find(id)
        result = story.generate(answers)
        if result:
            return render_template('result.html', story=story, result=result, title="Result")
        else:
            error_messages.append(
                "Failed to generate madlib. Please try again later.")
            return render_template('form.html', story=story, title="Form", errors=error_messages)

    story = storyList.find(id)

    if story:
        print(story)
        return render_template('form.html', story=story, title="Form")
    else:
        return render_template('stories.html', stories=storyList, title="All Stories")


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        # process new story
        form = request.form

        # parse prompts from form
        prompts = [pos for prompt, pos
                   in form.items()
                   if (pos and 'prompt' in prompt.strip())]

        template = form['template'].strip()

        # Form data validation
        error_messages = []

        if not prompts:
            error_messages.append("Madlib must include one prompt.")

        if not template:
            error_messages.append("Story template required.")

        for x in prompts:
            if x not in template:
                error_messages.append(f'Prompt \'{x}\' not found in template.')

        if error_messages:
            return render_template('new.html', story=Story(prompts, template), title="New", errors=error_messages)

        # attempt to process form data
        try:
            for prompt in prompts:
                if ' ' in prompt:
                    old_prompt = prompt
                    indx = prompts.index(prompt)
                    prompt = prompt.replace(' ', '_')
                    prompts.remove(old_prompt)
                    prompts.insert(indx, prompt)
                    template = template.replace(old_prompt, prompt)

            story = Story(prompts, template)
            storyList.addStory(story)
            return redirect('/')
        except Exception as ex:
            print(ex)
            return render_template('new.html', story=Story(), title="New", error="There was an error parsing your madlib story.")
    else:
        return render_template('new.html', story=Story(), title="New")


@app.route('/')
def displayStories():
    return render_template('stories.html', stories=storyList, title="All Stories")
