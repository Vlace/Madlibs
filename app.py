from flask import Flask, render_template, request
from stories import stories
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route("/story1")
def generate_story():
    final_story = story.generate(request.args)
    return render_template("story.html", final_story = final_story)

@app.route("/story")
def select_story():
    stories_list = stories
    return render_template("start.html", stories=stories_list)
    
@app.route("/story/prompt")
def home():
    story_id = request.args["story_id"]
    story = stories[int(story_id)]
    prompts = story.prompts
    return render_template("prompt.html", story_id=story_id, story = story, prompts = prompts)
    
    
    
    

 # story_id = request.args["story_id"]
    # story = stories[story_id]