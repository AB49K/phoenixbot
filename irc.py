import socket
import irc_pass
import time


class IRC:
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send(b"PRIVMSG " + chan + b" " + msg + b"\r\n")

    def send_action(self, chan, msg):
        self.irc.send(b"PRIVMSG " + chan +b" " + b":\x01ACTION " + msg + b"\x01\n")

    def connect(self, server, channel, botnick):
        print("connecting to: " + server)
        self.irc.connect((server, 6667))
        self.irc.send(b"USER " + botnick + b" " + botnick + b" " + botnick + b" :This is a bot." + b"\r\n")
        self.irc.send(b"NICK " + botnick + b"\r\n")
        self.irc.send(b"JOIN " + channel + b"\r\n")

    def get_text(self, channel):
        text = self.irc.recv(2040)

        if text.find(b'PING') != -1:
            self.irc.send(b'PONG ' + text.split()[1] + b'\r\n')
            time.sleep(2)
            self.irc.send(b"PRIVMSG NickServ :IDENTIFY " + irc_pass.password.encode() + b"\r\n")
            self.irc.send(b"JOIN " + channel + b"\r\n")

        return text
