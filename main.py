from irc import *
import random

channel = b'#linuxmasterrace'
server = "irc.snoonet.org"
nickname = b"PhoenixBot3000"
command_char = "!"

# username = text.split[2]  "if username in list_of_users" should do it.
def getstring(db): #Just makes things a bit cleaner - Also allows you to add new entries to the .txt's without needing to reboot phoenixbot.
	f=open(db, 'r')
	data=f.readlines()
	f.close()
	return data[random.randint(0,len(data)-1)]
#Love, AB49K.
irc = IRC()

irc.connect(server, channel, nickname)


def if_command(trigger, response):
    if b"PRIVMSG" in text and channel in text and trigger.encode().lower() in text:
        irc.send(channel, response.encode())


def if_command_action(trigger, response):
    if b"PRIVMSG" in text and channel in text and trigger.encode().lower() in text:
        irc.send_action(channel, response.encode())


def volvojoke():
    return getstring('volvo_joke.txt')


def conspiracy():
    return getstring('who.txt') + " " + getstring("action.txt") + " " + getstring("what.txt") + "!"


def imply():
    return ">implying coconuts can migrate"


def crash():
    return getstring("crashes.txt")


def linuxjoke():
    return getstring("linux_joke")

def distro_list():
    return getstring("distros.txt")

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
