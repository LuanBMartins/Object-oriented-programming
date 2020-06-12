from abc import ABC, abstractmethod

class titulacaoInvalida(Exception):
    pass

class IdadeProfessorInvalida(Exception):
    pass

class cursoInvalido(Exception):
    pass

class idadeAlunoInvalida(Exception):
    pass

class cpfDuplicado(Exception):
    pass


class Pessoa(ABC):

    def __init__(self, nome, endereco, idade, CPF):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__CPF = CPF
    
    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def getIdade(self):
        return self.__idade

    def getCPF(self):
        return self.__CPF

    @abstractmethod
    def printDescricao(self):
        pass


class Professor(Pessoa):

    def __init__(self, nome, endereco, idade, CPF, titulacao):
        super().__init__(nome, endereco, idade, CPF)
        self.__titulacao = titulacao

    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print('-- Professor cadastrado --')
        print(f'Nome: {self.getNome()}')
        print(f'Endereço: {self.getEndereco()}')
        print(f'Idade: {self.getIdade()}')
        print(f'CPF: {self.getCPF()}')
        print(f'Titulação: {self.__titulacao}')
        print()

class Aluno(Pessoa):

    def __init__(self, nome, endereco, idade, CPF, curso):
        super().__init__(nome, endereco, idade, CPF)
        self.__curso = curso

    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print('-- Aluno cadastrado --')
        print(f'Nome: {self.getNome()}')
        print(f'Endereço: {self.getEndereco()}')
        print(f'Idade: {self.getIdade()}')
        print(f'CPF: {self.getCPF()}')
        print(f'Curso: {self.__curso}')
        print()

Alunos = [
    ('Luan', 'Maria da fe', 21, '13862', 'SIN'),
    ('Joao', 'Itajuba', 20, '13822', 'CCO'),
    ('Maria', 'Itajuba', 17, '13121', 'CCO'),
    ('lucas', 'Cristina', 19, '13822', 'SIN'),
    ('Isa', 'Itajuba', 20, '11832', 'MAT')
]

Professores = [
    ('Jony', 'Campinas', 30, '11212', 'doutor'),
    ('Junior', 'Itajuba', 27, '32155', 'doutor'),
    ('Marcia', 'Itajuba', 31, '66521', 'mestre'),
    ('Lucia', 'Cristina', 45, '19892', 'doutor'),
]

cadastroAluno = {}
cadastroProfessor = {}

print('Cadastro de alunos \n') 
for nome, end, idade, cpf, curso in Alunos:
    try:
        if curso != 'SIN' and curso != 'CCO':
            raise cursoInvalido() 
        
        if idade < 18:
            raise idadeAlunoInvalida()

        if cpf in cadastroAluno:
            raise cpfDuplicado()

    except cursoInvalido:
        print(f'Erro de cadastro: Curso {curso} não permitido!\n')
    
    except idadeAlunoInvalida:
        print(f'Erro de cadastro: Idade {idade} não permitida!\n')

    except cpfDuplicado:
        print(f'Erro de cadastro: CPF {cpf} já existe!\n')

    else:
        cadastroAluno[cpf] = Aluno(nome, end, idade, cpf, curso)
        cadastroAluno[cpf].printDescricao()

print()
print('Cadastro de Professores \n') 
for nome, end, idade, cpf, titulo in Professores:
    try:
        if titulo != 'doutor':
            raise titulacaoInvalida() 
        
        if idade < 30:
            raise IdadeProfessorInvalida()

        if cpf in cadastroProfessor:
            raise cpfDuplicado()

    except titulacaoInvalida:
        print(f'Erro de cadastro: Titulo {titulo} não permitido!\n')
    
    except IdadeProfessorInvalida:
        print(f'Erro de cadastro: Idade {idade} não permitida!\n')

    except cpfDuplicado:
        print(f'Erro de cadastro: CPF {cpf} já existe!\n')

    else:
        cadastroProfessor[cpf] = Professor(nome, end, idade, cpf, titulo)
        cadastroProfessor[cpf].printDescricao()

