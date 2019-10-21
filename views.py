from route_helper import simple_route
from flask import render_template
import constants


# INDEX HOME PAGE
@simple_route("/")
def render_index(world:dict):
    try:
        if world['gamestate'] == 'active':
            dynamic_intro = generate_intro(world)
    except KeyError:
        dynamic_intro = constants.CONST_DEFAULT_HOMEPAGE_HEADER

    return render_template('index.html',
                           dynamic_homepage_header=dynamic_intro,
                           CONST_GAME_SUMMARY=constants.CONST_HOW_TO_PLAY,
                           CONST_HOW_TO_PLAY=constants.CONST_HOW_TO_PLAY,
                           CONST_GITHUB_LINK=constants.CONST_GITHUB_LINK
                           )

# MAIN GAME PAGE
@simple_route("/main")
def render_main(world:dict,action=None):
    
    return render_template('main.html')

# DEBUG PAGE
@simple_route("/debug")
def render_debug(world:dict):
    body = constants.CONST_DEBUG_HEADER
    for x in world:
        body = body + x + "<br/>"
    return body

# BEGIN FUNCTIONS
def generate_intro(world:dict):
    return "filler"

