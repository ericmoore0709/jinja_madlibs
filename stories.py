import uuid

"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words=[], text=""):
        """Create story with words and template text."""
        self.id = uuid.uuid4()
        self.prompts = words
        self.template = text

    def getId(self) -> str:
        return str(self.id)

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

    def __repr__(self) -> str:
        """String representation of the story."""
        return str.format("Story({}, {})", self.prompts, self.template)


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


class StoryList:
    "An encapsulated Story list."

    def __init__(self, stories: list[Story] = []):
        "Creates an instance of the story list."
        self.storiesList = stories

    def getStories(self):
        "Returns all stories in the story list."
        return self.storiesList

    def addStory(self, story):
        "Attempts to add story to the story list."
        try:
            if not isinstance(story, Story):
                story = Story(story)
            self.storiesList = [*self.storiesList, story]
        except Exception as ex:
            print(ex)

        return story

    def find(self, id: str) -> Story:
        "Finds the story with the given ID string."
        for story in self.storiesList:
            if story.getId() == id:
                return story


storyList = StoryList()
storyList.addStory(story)
