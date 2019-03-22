from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Teste")
        self.msg['font'] = ('Verdana', '10', 'italic', 'bold')
        self.msg.pack(side=RIGHT)

        self.sair = Button(self.widget1)
        self.sair['text'] = 'Sair'
        self.sair['font'] = ('Calibri', '10')
        self.sair['width'] = 5
        #self.sair['height'] = 5
        self.sair['bg'] = '#063B75'
        #self.sair['command'] = self.widget1.quit
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack(side=LEFT)

    def mudarTexto(self, event):
        if self.msg['text'] == 'Teste':
            self.msg['text'] = 'Teste 2'
        else:
            self.msg['text'] = 'Teste'

root = Tk()
Application(root)
root.mainloop()