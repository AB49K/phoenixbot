from irc import *
import random

channel = b'#linuxmasterrace'
server = "irc.snoonet.org"
nickname = b"PhoenixBot3000"
command_char = "!"

# username = text.split[2]  "if username in list_of_users" should do it.

f_words = ['Fucking', 'Fine', 'Fabulous', 'Frickin\'', 'Freaking', 'Fantastic', 'F\'n', 'Fugging', 'Fscking']

volvo_jokes = ['What do you call a Volvo with dual exhaust? A wheel barrow!',
               'Why do Volvos have rear-window heaters? So your hands don\'t get cold when you have to push it!',
               'What\'s the difference between a Volvo and the principal\'s office? It\'s less embarrassing if your friend see you leaving the principal\'s office.',
               'Why do they put sidewalks besides most streets and highways? So Volvo owners have a safe place to walk home.',
               'What\'s the difference between a Volvo and a Porcupine? When it comes to a Volvo, the prick is on the inside.',
               'How do you make a Volvo go faster downhill? Turn off the engine.',
               'What\'s the difference between a Volvo and a shopping trolley? A shopping trolley is much easier to push.',
               'How do you double the value of a Volvo? Fill up the gas tank.',
               'What do you call a Volvo at the top of a hill? A miracle.']

who = ['Bush', 'Obama', 'The government', 'The aliens', 'The Russians', 'The French', 'Larry the cable guy', 'Lincoln',
       'Dave Cameron', 'The communists', 'Bill Nye the Science Guy', 'I', 'Edward Snowden', 'That hacker 4chan',
       '4chan', 'Guy Fieri', 'Bill Clinton', 'Donald Trump', 'Ted Cruz', 'Hillary Clinton', 'The illuminati']

action = ['did', 'caused', 'planned', 'was behind', 'helped with', 'masterminded', 'faked', 'lied about']

what = ['the moon landing', '9/11', '7/11', 'water gate', 'your mom', 'the Titanic\'s sinking',
        'the faked moon landing', 'the NSA', 'PigGate']

crashes = ['segfaults and crashes',
           'bluescreens',
           'has his ram burn out',
           'gets a kernel panic',
           'messes up pkill and crashes',
           'gets a fatal null pointer exception',
           'dies at the hands of a memory leak',
           'breaks for no reason',
           'crashes from crappy programming']

irc = IRC()

irc.connect(server, channel, nickname)


def if_command(trigger, response):
    if b"PRIVMSG" in text and channel in text and trigger.encode().lower() in text:
        irc.send(channel, response.encode())


def rtfm():
    return "Read The " + f_words[random.randint(0, 8)] + " Manual, you noob: https://wiki.archlinux.org/"


def volvojoke():
    return volvo_jokes[random.randint(0, 8)]


def conspiracy():
    return who[random.randint(0, 20)] + " " + action[random.randint(0, 7)] + " " + what[random.randint(0, 8)] + "!"


def imply():
    return ">implying coconuts can migrate"


def crash():
    return str(nickname)[2:-1] + " " + crashes[random.randint(0, 8)]


while True:
    text = irc.get_text(channel)
    print(text)

    if_command(command_char + "rtfm_test", rtfm())
    if_command(command_char + "volvojoke", volvojoke())
    if_command(command_char + "conspiracy", conspiracy())
    if_command(command_char + "crash", crash())
    if_command(command_char + "implying", imply())
    if_command(command_char + "help", "rtfm_test, volvojoke, conspiracy, crash, implying, help")
