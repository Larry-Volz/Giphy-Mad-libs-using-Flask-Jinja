from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *
from story_data import *

app = Flask(__name__)

app.config['SECRET_KEY']='FOO'
app.debug=True
debug=DebugToolbarExtension(app)

#VARIABLES
story_selection=""
answers={}
story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")

#ROUTES
@app.route('/mad-libs.html')
def mad_libs():
    """renders main page of app"""
    return render_template("mad-libs.html")

@app.route('/parts-of-speech.html', methods=["POST"])
def parts_of_speech():
    """renders page to gather user answers to prompts"""
    global story_selection 
    story_selection = request.form["story_selection"]
    return render_template("parts-of-speech.html", story_selection=story_selection, prompts=story.prompts)

@app.route('/show_story.html', methods = ['POST'])
def story_generator():
    """renders finished story to story.html page"""
    #TODO: Get story from parts-of-speech.html next instead of hard-coding
    for prompt in story.prompts:
        answers[prompt] = request.form[prompt]
        final_story = story.generate(answers)

    return render_template("show_story.html", story_selection=story_selection, final_story=final_story)
