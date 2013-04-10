#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import threading
import subprocess
import os
from Tkinter import *

root = Tk()
root.title("Snowflake Core Log")
text = Text()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text.config(width=100, height=30)
text.pack(side=LEFT, fill=Y)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)


proc = subprocess.Popen(['python',os.path.join(os.path.dirname(__file__),'Snowflake'),os.path.dirname(__file__)],stdout=subprocess.PIPE)


def log():
    while True:
        line = proc.stdout.readline()
        if line != '':
            #the real code does filtering here
            text.insert(END,line.rstrip() + "\n")
            text.see(END)
            text.update_idletasks()
            print line.rstrip()
        else:
            os._exit(1)
            break


def exit():
    root.destroy()
    try:
        proc.kill()
    except:
        pass


thread = threading.Thread(target=log)
thread.start()
root.protocol("WM_DELETE_WINDOW", exit)
root.update_idletasks()
root.resizable(0,0)
#root.withdraw()
root.mainloop()



