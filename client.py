import socket
from UI import UI
from tkinter import *
import threading

top = Tk()
top.resizable(width=False, height=False)


class UIClient(UI):

    def test(self):
        self.label1.configure(text="YEET")


class Connection(threading.Thread):
    def run(self):
        s = socket.socket()
        host = socket.gethostname()
        port = 12345
        msg = "CONNECTED"

        s.connect((host, port))
        print(s.recv(4096).decode())
        s.send(msg.encode())
        s.close()


z = UIClient(top, "HAXOR CLIENT")
CSocket = Connection(name="Client Socket")
CSocket.start()
top.mainloop()
