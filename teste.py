class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

#Instanciação (Aluno(...))
novo_aluno = Aluno(nome="Marcio", idade=16, curso="Desenvolvimento de Sistemas")

#Manipulação do atributo (novo_aluno.nome)
print(f'Nome do aluno: {novo_aluno.nome}')
print(f'Idade do aluno: {novo_aluno.idade}')
print(f'Cursando: {novo_aluno.curso}')