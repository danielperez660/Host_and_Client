from tkinter import *


class UI:

    def __init__(self, top, title):
        top.title(title)
        frameUp = Frame(top, width=400, height=300)
        frameDown = Frame(top, width=400, height=300)
        frameUp.grid()
        frameDown.grid()

        self.message = Entry(frameDown).grid(row=0, column=0)
        send = Button(top, text='Send', command=self.get_string)

        self.label1 = Label(frameUp, text="TEST ")
        self.label1.place(x=200, y=150, anchor="center")

    def addr_disp(self, addr):
        self.label1.configure(text=addr)

    def get_string(self):
        x = self.message.get()
        self.message.delete(0, END)
        return x
