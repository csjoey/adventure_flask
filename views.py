from route_helper import simple_route
from flask import render_template
import constants

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
@simple_route("/main")
def render_main(world:dict):
    return render_template('main.html')

def generate_intro(world:dict):
    return "filler"


