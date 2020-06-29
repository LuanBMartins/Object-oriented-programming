import tkinter as tk
from tkinter import messagebox

class limitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.Tela()

    def Tela(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background='#236B8E')
        self.root.geometry("750x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=950, height=700)
        self.root.minsize(width=750, height=500)

class controlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.limite = limitePrincipal(self.root, self)

        self.root.title('Sigaa')
        # Inicia o mainloop
        self.root.mainloop()

if __name__ == '__main__':
    c = controlePrincipal()