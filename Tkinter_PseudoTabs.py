'''
Created on Oct 12, 2014

@author: Max Ruiz
'''
from tkinter import *
from tkinter import filedialog
import sys

class Main(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title('Main Window')
        self.pack()

        self.initGUI()

    def initGUI(self):
        self.staticFrame()
        self.initTab()
        pass

    def tab1(self):
        self.mainFrame.pack_forget()
        self.tab1Frame = LabelFrame(self, text='Tab 1')
        self.mainFrame = self.tab1Frame
        self.mainFrame.pack()

        l1 = Label(self.mainFrame, text='Tab 1', fg='red')
        l1.pack()

    def tab2(self):
        self.mainFrame.pack_forget()
        self.tab2Frame = LabelFrame(self, text='Tab 2')
        self.mainFrame = self.tab2Frame
        self.mainFrame.pack()

        l2 = Label(self.mainFrame, text='Tab 2', fg='blue')
        l2.pack()

    def initTab(self):
        self.tab1Frame = LabelFrame(self, text='Tab 1')
        self.mainFrame = self.tab1Frame
        self.mainFrame.pack()

        l1 = Label(self.mainFrame, text='Tab 1', fg='red')
        l1.pack()

    def staticFrame(self):
        self.sF = LabelFrame(self, text='Static Frame')
        b1 = Button(self.sF, text='tab 1', command=self.tab1)
        b1.pack(side='left')

        b2 = Button(self.sF, text='tab 2', command=self.tab2)
        b2.pack(side='left')

        self.sF.pack(side='top', fill=BOTH)

root = Tk()
app = Main(master=root)
app.mainloop()
