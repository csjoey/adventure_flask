import constants, random

# Performs game state updates based on inputs and returns html to put in {game_content} in main.html render
def generate_game(world, action, sub_action, arg):
    game_content = ""

    # Change the game state to dead if the player is both not drinking and out of hydration
    if world['hydration'] <= 0 and not is_valid_drink(sub_action,world):
        world['game_alive'] = False

    # Handle the player 8oz of water, eg "drink" is the specified sub action
    if sub_action == "drink":
        if is_valid_drink(sub_action, world):
            world['hydration'] += 30
            world['ounces_available'] -= 8

    # If the game is dead, show game over screen in all cases by returning game over html
    if not world['game_alive']:
        game_content = constants.CONST_GAME_OVER
        return game_content

    # Handle the player going home
    if action == 'home':
        game_content = render_home(world)

    # Handle showing the player their past purchases
    if action == 'purchases':
        game_content = render_purchases(world)

    # Handle buying Fiji and displaying the shop
    if action == 'shop':
        # Necessary buffered swap due to simple_route bug
        # Not risking a workaround 4 hours before 'release'
        buffer = arg
        arg = sub_action
        sub_action = buffer
        arg = int(arg) if arg else None

        # Decrement hydration if an invalid buy is attempted and check this using is_valid_buy
        world['hydration'] -= 10 if not is_valid_buy(world['money'], sub_action,arg) else 0
        # If transaction is valid then take money and give corresponding ounces
        if is_valid_buy(world['money'], sub_action,arg):
            if arg == 1:
                world['ounces_available'] += 8
                world['money'] -= 2
            if arg == 2:
                world['ounces_available'] += 48
                world['money'] -= 10
            if arg == 3:
                world['ounces_available'] += 200
                world['money'] -= 25
            # Add purchase to history key
            world['purchases'].append(arg)

        game_content = render_shop(world)

    # Handle Showing the play the work screen
    if action == 'work':
        # Detect simple_route bug and perform necessary swap
        if arg == "solve":
            arg = sub_action
            # Try and convert user submission into and int and ignore if an error occurs ie invalid input
            try:
                if eval(world['math_challenge']) == int(arg):
                    world['money'] += 2
            except:
                pass
        # Take away 5 hydration for solve attempt and 15 for travel to work
        # Player can save a theoretical 10 hydration exploiting get injection but okay sure if you want go for it
        world['hydration'] -= 15 if action != "solve" else 5
        # Update the math challenge to be displayed before every time page is loaded
        world['math_challenge'] = generate_challenge()
        game_content = render_work(world)

    return game_content

# Main Rendering Functions
# += FIJISTATS adds current stat info to the page
# += DRINKBUTTON adds drink functionality to the page
# Player can cause an error by drinking where they're not supposed to but this has no logistical effects

def render_home(world):
    body = constants.FORMATSTR_HOME
    body += constants.FORMATSTR_FIJISTATS.format(world['hydration'],world['money'],world['ounces_available'])
    body += constants.HTMLSTR_DRINKBUTTON.format("home")
    return body

def render_purchases(world):
    body = constants.FORMATSTR_PURCHASES.format(gen_purchases(world['purchases']))
    return body

def render_shop(world):
    body = constants.FORTMATSTR_SHOP.format(world['money'])
    body += constants.FORMATSTR_FIJISTATS.format(world['hydration'],world['money'],world['ounces_available'])
    return body

def render_work(world):
    body = ""
    body += constants.FORMATSTR_WORK.format(world['math_challenge'])
    body += constants.FORMATSTR_FIJISTATS.format(world['hydration'], world['money'], world['ounces_available'])
    body += constants.HTMLSTR_DRINKBUTTON.format("work")
    return body



# Page Sub Functions

# Check that all inputs are expected and that the player has enough money
def is_valid_buy(money, sub_action,arg):
    if sub_action == "buy" and int(arg) in [1,2,3]:
        if arg == 1 and money >= 2:
            return True
        if arg == 2 and money >= 10:
            return True
        if arg == 3 and money >= 25:
            return True
    return False

# Check that the player has 'ounces' to deplete and that all inputs are expected
def is_valid_drink(sub_action,world):
    if sub_action == "drink" and world["ounces_available"] >= 8:
        return True
    else:
        return False

# Generate html img tags to inject into body as a function of world['purchases'] and a dict containing img static refs
def gen_purchases(inlist):
    html = ""
    for item in inlist:
        html += '<img src=" {} ">'.format(constants.CONST_FIJI_IMG_LIST[item-1])
    return html

# Generate a math challenge string containing + - or * as operators and terms 5-15 and 3-15
def generate_challenge():
    term1 = str(random.randint(5,15))
    term2 = str(random.randint(3,15))
    operator = ["+","-","*"][random.randint(0,2)]
    return term1+operator+term2

