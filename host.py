import socket
from tkinter import *
import threading
from UI import UI
import sqlite3
from datetime import datetime

conn = sqlite3.connect('connections.db')
co = conn.cursor()


try:
    co.execute("""CREATE TABLE connections
                  (ip text primary key,id text, time date)""")

    conn.commit()
except sqlite3.OperationalError:
    pass


class UIHost(UI):

    def get_string(self):
        msg = self.message.get()
        self.message.delete(0, END)
        #send_msg()


def send_msg(msg, c):
    c.send(msg.encode())
    print(c.recv(4096).decode())


class Connection(threading.Thread):

    def run(self):
        s = socket.socket()
        host = socket.gethostname()
        port = 12345
        s.bind((host, port))
        s.listen(5)

        while True:
            c, addr = s.accept()
            msg = "TEST"
            send_msg(msg, c)
            print("Got connection from ", addr, " @ ", datetime.today())
            print(c)
            z.addr_disp(addr)
            c.close()


top = Tk()
top.resizable(width=False, height=False)
x = Connection(name="Host Socket")
x.start()
z = UI(top, "HOST")

conn.close()
top.mainloop()
