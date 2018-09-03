import socket
from tkinter import *
import threading
from UI import UI
import sqlite3
from datetime import datetime

conn = sqlite3.connect('connections.db')
c = conn.cursor()


try:
    c.execute("""CREATE TABLE connections
                  (ip text primary key,id text, time date)""")

    conn.commit()
except sqlite3.OperationalError:
    pass


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
            print("Got connection from ", addr)
            c.send(msg.encode())
            print(c.recv(4096).decode())
            z.addr_disp(addr)
            c.close()


top = Tk()
top.resizable(width=False, height=False)
x = Connection(name="TEST_VAL")
x.start()
z = UI(top, "HAXOR HOST")

conn.close()
top.mainloop()
