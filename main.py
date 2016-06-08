from irc import *
import random

channel = b'#linuxmasterrace'
server = "irc.snoonet.org"
nickname = b"PhoenixBot3000"
command_char = "!"

# username = text.split[2]  "if username in list_of_users" should do it.

volvo_jokes = ['What do you call a Volvo with dual exhaust? A wheel barrow!',
               'Why do Volvos have rear-window heaters? So your hands don\'t get cold when you have to push it!',
               'What\'s the difference between a Volvo and the principal\'s office? It\'s less embarrassing if your friends see you leaving the principal\'s office.',
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
        'the faked moon landing', 'the NSA', 'PigGate', 'Nikola Tesla\'s arrest', 'backdooring windows', 'backdooring your computer']

crashes = ['segfaults and crashes',
           'bluescreens',
           'has his ram burn out',
           'gets a kernel panic',
           'messes up pkill and crashes',
           'gets a fatal null pointer exception',
           'dies at the hands of a memory leak',
           'breaks for no reason',
           'crashes from crappy programming',
	   'crashes after something goes wrong in factoryfactoryfactories.java',
	   'gets an off-by-one error',
	   'ponders whether his creator\'s choice to let him run pkill was a good idea'
]

linux_jokes = ['Linux is user-friendly; it\'s just picky about who its friends are.',
               'There are two major products of Berkeley. LSD and UNIX. Probably not a coincidence.',
               'Here\'s a nickel, kid. Get yourself a better computer.',
               'stop@hammertime~$ touch /this touch: cannot touch "/this": Permission denied.',
               'rm -rf /bin/laden',
	       'chown -R us ./allyourbase',
	       'touch /woman touch: cannot touch \'woman\': Permission denied',
	       '/home is where the /heart is.',
	       'I want to dress up as a UDP packet for Halloween, but I don\'t know if anyone will get it.',
	       'There is a Linux-themed resturaunt, if you ask for a Big Mac, they\'ll reply "FF:FF:FF:FF:FF:FF',
	       'make love; Make: Don\'t know how to make love. Stop.',
	       'man: why did you get a divorce?; man:: Too many arguments.'
		]

distro = ['Arch', 'Sabayon', 'Gentoo', 'Ubuntu', 'Fedora', 'Debian', 'Chakra', 'Void', 'Alpine', 'NixOS', 'CentOS']

irc = IRC()

irc.connect(server, channel, nickname)


def if_command(trigger, response):
    if b"PRIVMSG" in text and channel in text and trigger.encode().lower() in text:
        irc.send(channel, response.encode())


def if_command_action(trigger, response):
    if b"PRIVMSG" in text and channel in text and trigger.encode().lower() in text:
        irc.send_action(channel, response.encode())


def volvojoke():
    return volvo_jokes[random.randint(0, 8)]


def conspiracy():
    return who[random.randint(0, 20)] + " " + action[random.randint(0, 7)] + " " + what[random.randint(0, 11)] + "!"


def imply():
    return ">implying coconuts can migrate"


def crash():
    return crashes[random.randint(0, 11)]


def linuxjoke():
    return linux_jokes[random.randint(0, 11)]

def distro_list():
    return distro[random.randint(0, 10)]

while True:
    text = irc.get_text(channel)
    print(text)

    if_command(".kappa", "ᕙ༼ಠ͜ʖಠ༽")
    if_command("PhoenixBot3000, WAT DISTOR", distro_list())
    if_command(command_char + "volvojoke", volvojoke())
    if_command(command_char + "conspiracy", conspiracy())
    if_command("what os should I uninstall?", "WINDOWSWINDOWSWINDOWSWINDOWS WINDOOOOOOOOWS")
    if_command_action(command_char + "crash", crash())
    if_command(">implying", imply())
    if_command(command_char + "source", "https://github.com/whitephoenix0/phoenixbot")
    if_command(command_char + "cowbell", "https://www.reddit.com/r/needsmorecowbell/")
    if_command(command_char + "linuxjoke", linuxjoke())
    if_command(command_char + "help", "volvojoke, conspiracy, crash, implying, source, cowbell, linuxjoke, help")
