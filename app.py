# Informações de um aluno

aluno1 = ('Maria Joaquina', [10, 8, 9, 7])

nome_aluno1 = aluno1[0]

notas_aluno1 = aluno1[1]

# Informações de uma disciplina

alunos_lb = {}

alunos_lb = {
    'matricula1': ('aluno1', [10, 8, 7, 5]),
    'matricula2': ('aluno2', [8, 8, 9, 6]),
    'matricula3': ('aluno3', [9, 8, 6, 7])
}

# Liste todas as matrículas dos alunos matriculados na disciplina

chaves = alunos_lb.keys()

print('Matrículas da disciplina Laboratório de Programação:')
for chave in chaves:
    print(chave)


# Liste todos os alunos matriculados na disciplina

valores = alunos_lb.values()

print('Alunos matriculados na disciplina Laboratório de Programação:')
for valor in valores:
    print(valor)
    