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
story=""
answers={}


#ROUTES
@app.route('/mad-libs.html')
def mad_libs():
    """renders main page of app"""
    return render_template("mad-libs.html")

@app.route('/parts-of-speech.html', methods=["POST"])
def parts_of_speech():
    """renders page to gather user answers to prompts"""
    global story_selection 
    global story
    global title

    story_selection = request.form["story_selection"]
    if story_selection == "three_pigs":
        story = Story(three_pigs["prompts"], three_pigs['text'])
        title=three_pigs["title"]
    elif story_selection == "wolf_boy":
        story = Story(wolf_boy["prompts"], wolf_boy['text'])
        title=wolf_boy["title"]
    elif story_selection == "star_wars":
        story = Story(star_wars["prompts"], star_wars['text'])
        title=star_wars["title"]
        
    return render_template("parts-of-speech.html", prompts=story.prompts,title=title)

@app.route('/show_story.html', methods = ['POST'])
def story_generator():
    """renders finished story to story.html page"""
    for prompt in story.prompts:
        answers[prompt] = request.form[prompt]
        final_story = story.generate(answers)

    return render_template("show_story.html", final_story=final_story,title=title)
