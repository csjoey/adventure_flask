import constants,random

def generate_game(world,action,sub_action,arg):

    game_content = ""
    # Change the game state to dead if the player is both not drinking and out of hydration
    if world['hydration'] <=0 and not is_valid_drink(sub_action,world):
        world['game_alive'] = False

    # Handle the player drinking 8oz of water
    if sub_action == "drink":
        if is_valid_drink(sub_action,world):
            world['hydration'] += 30
            world['ounces_available'] -= 8

    # If the game is dead, show game over screen in all cases
    if not world['game_alive']:
        game_content = constants.CONST_GAME_OVER
        return game_content

    # Handle the player going home
    if action == 'home':
        game_content = render_home(world, sub_action, arg)

    # Handle showing the player their past purchases
    if action == 'purchases':
        game_content = render_purchases(world, sub_action, arg)

    # Handle buying Fiji and displaying the shop
    if action == 'shop':
        buffer = arg
        arg = sub_action
        sub_action = buffer
        arg = int(arg) if arg else None
        world['hydration'] -= 10 if not is_valid_buy(world['money'],sub_action,arg) else 0
        if is_valid_buy(world['money'],sub_action,arg):
            if arg == 1:
                world['ounces_available'] += 8
                world['money'] -= 2
            if arg == 2:
                world['ounces_available'] += 48
                world['money'] -= 10
            if arg == 3:
                world['ounces_available'] += 200
                world['money'] -= 25

            world['purchases'].append(arg)

        game_content = render_shop(world, sub_action, arg)

    if action == 'work':
        if arg == "solve":
            buffer = arg
            arg = sub_action
            sub_action = buffer
            print(action,sub_action,arg)
            try:
                if eval(world['math_challenge']) == int(arg):
                    world['money'] += 2
            except:
                pass
        world['hydration'] -= 15 if action != "solve" else 5
        world['math_challenge'] = generate_challenge()
        game_content = render_work(world, sub_action, arg)

    return game_content

# Main Rendering Functions

def render_home(world,sub_action,arg):
    body = constants.FORMATSTR_HOME
    body += constants.FORMATSTR_FIJISTATS.format(world['hydration'],world['money'],world['ounces_available'])
    body += constants.HTMLSTR_DRINKBUTTON.format("home")
    return body

def render_purchases(world,sub_action,arg):
    body = constants.FORMATSTR_PURCHASES.format(gen_purchases(world['purchases']))
    return body

def render_shop(world,sub_action,arg):
    body = constants.FORTMATSTR_SHOP.format(world['money'])
    body += constants.FORMATSTR_FIJISTATS.format(world['hydration'],world['money'],world['ounces_available'])
    return body

def render_work(world,sub_action,arg):
    body = ""
    body += constants.FORMATSTR_WORK.format(world['math_challenge'])
    body += constants.FORMATSTR_FIJISTATS.format(world['hydration'], world['money'], world['ounces_available'])
    body += constants.HTMLSTR_DRINKBUTTON.format("work")
    return body



# Page Sub Functions

def is_valid_buy(money,sub_action,arg):
    if sub_action == "buy" and int(arg) in [1,2,3]:
        if arg == 1 and money >= 2:
            return True
        if arg == 2 and money >= 10:
            return True
        if arg == 3 and money >= 25:
            return True
    return False

def is_valid_drink(sub_action,world):
    if sub_action == "drink" and world["ounces_available"] >= 8:
        return True
    else:
        return False

def gen_purchases(inlist):
    html = ""
    for item in inlist:
        html += '<img src=" {} ">'.format(constants.CONST_FIJI_IMG_LIST[item-1])
    return html

def generate_challenge():
    term1 = str(random.randint(5,15))
    term2 = str(random.randint(3,15))
    operator = ["+","-","*"][random.randint(0,2)]
    return term1+operator+term2

