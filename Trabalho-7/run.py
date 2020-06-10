def getCargaHorariaOB(aluno, historico, grade1, grade2):
    cargaHoraria = 0
    #encontrando a grade do curso que o aluno não cursou
    if aluno.getCurso() == grade1.getCurso():
        for disc in historico.getHistorico():
            #encontrando as disciplinas que ele já curso da grade
            for grad in grade1.getDisciplina():
                if disc.getNomeDisciplina() == grad.getNomeDisciplina():
                    cargaHoraria += disc.getCargaHoraria()

    #encontrando a grade do curso que o aluno não cursou
    elif aluno.getCurso() == grade2.getCurso():
        for disc in historico.getHistorico():
            #encontrando as disciplinas que ele já curso da grade
            for grad in grade2.getDisciplina():
                if disc.getNomeDisciplina() == grad.getNomeDisciplina():
                    cargaHoraria += disc.getCargaHoraria()
    
    return cargaHoraria

def getCargaHorariaOP(aluno, historico, grade1, grade2):
    cargaHoraria = 0
    #encontrando a grade do curso do aluno
    if aluno.getCurso() != grade1.getCurso():
        for disc in historico.getHistorico():
            #encontrando as disciplinas que ele já curso da grade
            for grad in grade1.getDisciplina():
                if disc.getNomeDisciplina() == grad.getNomeDisciplina():
                    cargaHoraria += disc.getCargaHoraria()
    
    #encontrando a grade do curso do aluno
    elif aluno.getCurso() != grade2.getCurso():
        for disc in historico.getHistorico():
            #encontrando as disciplinas que ele já curso da grade
            for grad in grade2.getDisciplina():
                if disc.getNomeDisciplina() == grad.getNomeDisciplina():
                    cargaHoraria += disc.getCargaHoraria()
    
    return cargaHoraria


class Aluno:

    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso

    def getnroMatric(self):
        return self.__nroMatric

    def getNome(self):
        return self.__nome

    def getCurso(self):
        return self.__curso


class Historico:

    def __init__(self, aluno):
        self.__aluno = aluno
        self.__disciplinas = []

    def getAluno(self):
        return self.__aluno

    def getHistorico(self):
        return self.__disciplinas

    #Adiciona uma instancia de Disciplina Para a lista de disciplinas
    def addDisciplina(self, codigo, nome, cargaHoraria):
        disc = Disciplina(codigo, nome, cargaHoraria)
        self.__disciplinas.append(disc)


class Curso:

    def __init__(self, nome):
        self.__nome = nome
        self.__grade = None

    def getNomeCurso(self):
        return self.__nome

    def getGrade(self):
        return self.__grade


class Disciplina:

    def __init__(self, codigo, nome, cargaHoraria, grade=None):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria    
        self.__grade = grade

    def getNomeDisciplina(self):
        return self.__nome

    def getCodigo(self):
        return self.__codigo

    def getCargaHoraria(self):
        return self.__cargaHoraria

    def getGrade(self):
        return self.__grade


class Grade:

    def __init__(self, ano, curso):
        self.__ano = ano
        self.__curso = curso
        self.__disciplinas = []
    
    def getAno(self):
        return self.__ano

    def getCurso(self):
        return self.__curso

    def getDisciplina(self):
        return self.__disciplinas

    #Adiciona uma instancia de Disciplina Para a lista de disciplinas
    def addDisciplina(self, codigo, nome, cargaHoraria):
        disci = Disciplina(codigo, nome, cargaHoraria, self)
        self.__disciplinas.append(disci)


#Cria o curso e adicona disciplinas a sua grade
Curso1 = Curso('Sistemas de informação')
grade1 = Grade(2019, Curso1)
grade1.addDisciplina(1, 'AED', 64)
grade1.addDisciplina(2, 'POO', 64)
grade1.addDisciplina(3, 'COM112', 82)
grade1.addDisciplina(4, 'COM110', 82)

#Cria o curso e adicona disciplinas a sua grade
Curso2 = Curso('Fisica')
grade2 = Grade(2014, Curso2)
grade2.addDisciplina(1, 'Introducao a fisica', 64)
grade2.addDisciplina(2, 'Fisica experimental', 64)
grade2.addDisciplina(3, 'Calculo I', 82)

#Cria o aluno e adiociona disciplinas a seu historico
Aluno1 = Aluno(12, 'Luan martins', Curso1)
Historico1 = Historico(Aluno1)
Historico1.addDisciplina(1 , 'AED', 64)
Historico1.addDisciplina(2 , 'POO', 64)
Historico1.addDisciplina(3 , 'COM112', 82)
Historico1.addDisciplina(4 , 'Introducao a fisica', 64)

#Cria o aluno e adiociona disciplinas a seu historico
Aluno2 = Aluno(22, 'joao', Curso2)
Historico2 = Historico(Aluno2)
Historico2.addDisciplina(1 , 'Introducao a fisica', 64)
Historico2.addDisciplina(2 , 'Fisica experimental', 64)
Historico2.addDisciplina(3 , 'COM112', 82)

#Dados Aluno1
print(f'Aluno: {Aluno1.getNome()}')
print(f'Matricula: {Aluno1.getnroMatric()}')
print('-- Historico --')

#Percore o historico
for histor in Historico1.getHistorico():
    
    print(f'Codigo: {histor.getCodigo()},  Disciplina: {histor.getNomeDisciplina()}, Carga horaria: {histor.getCargaHoraria()}')

print(f'Total Carga Horaria Obrigatória cursada: {getCargaHorariaOB(Aluno1, Historico1, grade1, grade2)}')
print(f'Total Carga Horaria Optativa cursada: {getCargaHorariaOP(Aluno1, Historico1, grade1, grade2)}')    
print()

#Dados Aluno2
print(f'Aluno: {Aluno2.getNome()}')
print(f'Matricula: {Aluno2.getnroMatric()}')
print('-- Historico --')

#Percore o historico
for histor in Historico2.getHistorico():
    
    print(f'Codigo: {histor.getCodigo()},  Disciplina: {histor.getNomeDisciplina()}, Carga horaria: {histor.getCargaHoraria()}')
    
print(f'Total Carga Horaria Obrigatória cursada: {getCargaHorariaOB(Aluno2, Historico2, grade1, grade2)}')
print(f'Total Carga Horaria Optativa cursada: {getCargaHorariaOP(Aluno2, Historico2, grade1, grade2)}')  





