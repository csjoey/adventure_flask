from route_helper import simple_route
from flask import render_template
from main import generate_game
import constants


# INDEX HOME PAGE
@simple_route("/")
def render_index(world:dict):
    try:
        game_alive = world['game_alive']
    except:
        game_alive = False

    return render_template('index.html',
                           game_alive=game_alive,
                           CONST_GAME_SUMMARY=constants.CONST_HOW_TO_PLAY,
                           CONST_HOW_TO_PLAY=constants.CONST_HOW_TO_PLAY,
                           CONST_GITHUB_LINK=constants.CONST_GITHUB_LINK
                           )

# MAIN GAME PAGE
@simple_route("/main")
def render_main(world:dict,action=None):
    return render_template('main.html',game_content=generate_game(world))

# DEBUG PAGE
@simple_route("/debug")
def render_debug(world:dict):
    body = constants.CONST_DEBUG_HEADER
    for x in world:
        body = body + x + "<br/>"
    return body

# BEGIN FUNCTIONS





