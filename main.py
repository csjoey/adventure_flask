def generate_game(world,action=None,sub_action=None,arg=None):
    game_content = ""
    world['hydration'] -= 10
    if world['hydration'] <= 0:
        world['game_alive'] = False


    if action == 'home':
        pass

    if action == 'purchases':
        pass

    if action == 'shop':
        pass

    if action == 'work':
        pass

    return game_content
