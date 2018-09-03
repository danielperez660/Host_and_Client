import socket
from UI import UI
from tkinter import *

top = Tk()
top.resizable(width=False, height=False)

s = socket.socket()
host = socket.gethostname()
port = 12345
msg = "CONNECTED"

s.connect((host, port))
print(s.recv(4096).decode())
s.send(msg.encode())
s.close()

z = UI(top, "HAXOR CLIENT")
top.mainloop()