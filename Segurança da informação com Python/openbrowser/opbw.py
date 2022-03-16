import webbrowser
from tkinter import *

root = Tk()

root.title('Abrir browser')
root.geometry('300x200')

def google():
    webbrowser.open('google.com.br')


mygoogle = Button(root, text='Abrir', command=google).pack(pady=20)

root.mainloop()
