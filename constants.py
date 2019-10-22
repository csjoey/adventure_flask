#Constants file containing mostly strings for home/index page

CONST_GAME_SUMMARY: str = "A game where you are challenged to buy as much fiji water as possible without running out of " \
                          "water yourself."

CONST_HOW_TO_PLAY: str = \
"""
Start the game using the button in the upper left corner, and then get to grinding! FijiQuest
is a game where you are challenged to collect as much aesthetic Fiji brand water as possible.
But be careful! If you run out of hydration on your travels, you will fall to drought! Go
to work to collect funds for Fiji water, just like real life! Capitalism! Then spend your hard earned money on Fiji water
in the shop. During your quests, look at your FijiCount and see how much you've collected!
"""

CONST_GITHUB_LINK: str = 'https://github.com/csjoey/adventure_flask'

CONST_DEBUG_HEADER: str = '<html> <h1>CURRENT WORLD VARIABLES</h1><br/>'

CONST_FIJI_IMG_LIST: list = [
    '/static/img/fiji_single.png',
    '/static/img/fiji_sixpack.png',
    '/static/img/fiji_twentyfour_bonus.png'
]

CONST_GAME_OVER: str = """
<h2>
Ooops! you ran out of hydration! Please exit or reset your game.
</h2>
"""


FORMATSTR_HOME = """
<h4>You are relaxing in your home, watching some YouTube while enjoying some nice Fiji water.</h4>
<br><br><br><br><br>
"""

FORMATSTR_PURCHASES = """
<h4>Below are all of the bottles of Fiji you have purchased so far.</h4><br>
 {} 
"""

FORTMATSTR_SHOP = """
<h4>Welcome to the FijiShop, You currently have {} dollars.</h4><br>
<div class="row">
<div class="col">
<img src="/static/img/fiji_single.png"><br>
<a class="btn btn-primary btn" href="/main?action=shop&sub_action=buy&arg=1" role="button">Buy Single</a><br/>
$2
</div>
<div class="col">
<img src="/static/img/fiji_sixpack.png"><br>
<a class="btn btn-primary btn" href="/main?action=shop&sub_action=buy&arg=2" role="button">Buy 6 Pack</a><br/>
$10
</div>
<div class="col">
<img src="/static/img/fiji_twentyfour_bonus.png"><br>
<a class="btn btn-primary btn" href="/main?action=shop&sub_action=buy&arg=3" role="button">Buy 25 Pack</a><br/>
$25
</div>
</div>

"""

FORMATSTR_WORK = """
"""

FORMATSTR_FIJISTATS = """
<br/></br>
<h3>
Hydration Level: {}<br/>
Money: {}<br/>
Ounces of Fiji: {}<br/>
</h3>
"""

HTMLSTR_DRINKBUTTON: str = '<a class="btn btn-primary btn-lg" href="?action={}&sub_action=drink" role="button">Drink Fiji</a><br/>'






