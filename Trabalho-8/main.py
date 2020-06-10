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
        print(f'Nome: {self.getNome()}')
        print(f'Endereço: {self.getEndereco()}')
        print(f'Idade: {self.getIdade()}')
        print(f'CPF: {self.getCPF()}')
        print(f'Titulação: {self.__titulacao}')

class Aluno(Pessoa):

    def __init__(self, nome, endereco, idade, CPF, curso):
        super().__init__(nome, endereco, idade, CPF)
        self.__curso = curso

    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print(f'Nome: {self.getNome()}')
        print(f'Endereço: {self.getEndereco()}')
        print(f'Idade: {self.getIdade()}')
        print(f'CPF: {self.getCPF()}')
        print(f'Curso: {self.__curso}')

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
print('Cadastro aluno')

for nome, end, idade, cpf, curso in Alunos:
    try:
        if curso != 'SIN' and curso != 'CCO':
            raise cursoInvalido() 
        
        if idade < 18:
            raise idadeAlunoInvalida()

        if cpf in cadastroAluno:
            raise cpfDuplicado()

    except cursoInvalido:
        print(f'Curso {curso} não permitido!')
    
    except idadeAlunoInvalida:
        print(f'Idade {idade} não permitida!')

    except cpfDuplicado:
        print(f'CPF {cpf} já existe!')

    else:
        cadastroAluno[cpf] = Aluno(nome, end, idade, cpf, curso)

print()
print('Cadastro Professor')
for nome, end, idade, cpf, titulo in Professores:
    try:
        if titulo != 'doutor':
            raise titulacaoInvalida() 
        
        if idade < 30:
            raise IdadeProfessorInvalida()

        if cpf in cadastroProfessor:
            raise cpfDuplicado()

    except titulacaoInvalida:
        print(f'Titulo {titulo} não permitido!')
    
    except IdadeProfessorInvalida:
        print(f'Idade {idade} não permitida!')

    except cpfDuplicado:
        print(f'CPF {cpf} já existe!')

    else:
        cadastroProfessor[cpf] = Professor(nome, end, idade, cpf, titulo)

print()
print('Alunos cadastrados!')
for chave in cadastroAluno:
    aluno = cadastroAluno.get(chave)
    aluno.printDescricao()
    print('----------------------------')

print()
print('Professores cadastrados!')
for chave in cadastroProfessor:
    prof = cadastroProfessor.get(chave)
    prof.printDescricao()
    print('----------------------------')