import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import estudante as est 
import disciplina as disc

class codigoInvalido(Exception):
    pass

class Turma:

    def __init__(self, codigo, disciplina, estudantes):
        self.__codigo = codigo
        self.__disciplina = disciplina
        self.__estudantes = estudantes

    def getCodigo(self):
        return self.__codigo
    
    def getDisciplina(self):
        return self.__disciplina

    def getEstudantes(self):
        return self.__estudantes


class LimiteInsereTurma(tk.Toplevel):
    def __init__(self, controle, listaCodDiscip, listaNroMatric):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Disciplina")
        self.controle = controle

        self.frameCodTurma = tk.Frame(self)
        self.frameDiscip = tk.Frame(self)
        self.frameEstudante = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodTurma.pack()
        self.frameDiscip.pack()
        self.frameEstudante.pack()
        self.frameButton.pack()        

        self.labelCodTurma = tk.Label(self.frameCodTurma,text="Informe o código da turma: ")
        self.labelCodTurma.pack(side="left")
        self.inputCodTurma = tk.Entry(self.frameCodTurma, width=20)
        self.inputCodTurma.pack(side="left")

        self.labelDiscip = tk.Label(self.frameDiscip,text="Escolha a disciplina: ")
        self.labelDiscip.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameDiscip, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCodDiscip
          
        self.labelEst = tk.Label(self.frameEstudante,text="Escolha o estudante: ")
        self.labelEst.pack(side="left") 
        self.listbox = tk.Listbox(self.frameEstudante)
        self.listbox.pack(side="left")
        for nro in listaNroMatric:
            self.listbox.insert(tk.END, nro)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Aluno")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereAluno)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Turma")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaTurma)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)    

class LimiteConsultaTurmas(tk.Toplevel):

    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consulta")
        self.controle = controle
        self.framesTela(self.controle)

    def framesTela(self, controle):
        self.frameNro = tk.Frame(self)
        self.frameNro.pack()

        self.labelNro = tk.Label(self.frameNro, text="Código")
        self.labelNro.pack(side='left')
        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side='left')

        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        self.buttonConsulta = tk.Button(self.frameButton, text='Consultar')
        self.buttonConsulta.pack(side='left')
        self.buttonConsulta.bind("<Button>", controle.consultHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)        

class LimiteMostraTurmas():
    def __init__(self, str):
        messagebox.showinfo('Lista de turmas', str)

class CtrlTurma():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaTurmas = []
        self.listaAlunosTurma = []

        self.listaNroMatric = []

    def insereTurmas(self):        
        self.listaAlunosTurma = []
        listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        self.listaNroMatric = self.ctrlPrincipal.ctrlEstudante.getListaNroMatric()
        self.limiteIns = LimiteInsereTurma(self, listaCodDisc, self.listaNroMatric)

    def criaTurma(self, event):
        codTurma = self.limiteIns.inputCodTurma.get()
        discSel = self.limiteIns.escolhaCombo.get()
        disc = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(discSel)
        turma = Turma(codTurma, disc, self.listaAlunosTurma)
        self.listaTurmas.append(turma)
        self.limiteIns.mostraJanela('Sucesso', 'Turma criada com sucesso')
        self.limiteIns.destroy()


    def insereAluno(self, event):
        alunoSel = self.limiteIns.listbox.get(tk.ACTIVE)
        aluno = self.ctrlPrincipal.ctrlEstudante.getEstudante(alunoSel)
        self.listaAlunosTurma.append(aluno)
        self.limiteIns.mostraJanela('Sucesso', 'Aluno matriculado')
        self.limiteIns.listbox.delete(tk.ACTIVE)

    def consultaTurmas(self):
        self.limiteCon = LimiteConsultaTurmas(self)

    def consultHandler(self, event):
        codigo = self.limiteCon.inputNro.get()
        analise = True
        turm = []
        
        try:
            for cod in self.listaTurmas:
                if cod.getDisciplina().getCodigo() == codigo:
                    analise = False
                    turm.append(cod)

            if analise:
                raise codigoInvalido()

        except codigoInvalido:
            self.limiteCon.mostraJanela('Erro!', 'Codigo de disciplina invalido!')
        
        else:
            str = ''
            for turma in turm:
                str += 'Código: ' + turma.getCodigo() + '\n'
                str += 'Disciplina: ' + turma.getDisciplina().getCodigo() + '\n'
                str += 'Estudantes: \n'
                for estud in turma.getEstudantes():
                    str += estud.getNroMatric() + ' - ' + estud.getNome() + '\n'
                str += '------ \n'

            self.limiteCon.mostraJanela('Turmas(s)', str)

        
    def mostraTurmas(self):
        str = ''
        for turma in self.listaTurmas:
            str += 'Código: ' + turma.getCodigo() + '\n'
            str += 'Disciplina: ' + turma.getDisciplina().getCodigo() + '\n'
            str += 'Estudantes:\n'
            for estud in turma.getEstudantes():
                str += estud.getNroMatric() + ' - ' + estud.getNome() + '\n'
            str += '------\n'

        self.limiteLista = LimiteMostraTurmas(str)
    