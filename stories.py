"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass an (already generated) LIST of prompts, and the 
    story_template STR LITERAL of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate story_template from a story, pass in a DICTIONARY-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, prompts, story_template):
        """Create story with prompts and template story_template."""

        self.prompts = prompts
        self.template = story_template

    def generate(self, answers):
        """Substitute answers into story_template.
        answers passed in as a dictionary
        """

        story_final = self.template

        for (key, val) in answers.items():
            story_final = story_final.replace("{" + key + "}", val)

        return story_final


# Here's a story to get you started


# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )
