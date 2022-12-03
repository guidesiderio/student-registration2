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

matriculas = alunos_lb.keys()

print('Matrículas da disciplina Laboratório de Programação:')
for matricula in matriculas:
    print(matricula)

print()

# Liste todos os alunos matriculados na disciplina

alunos = alunos_lb.values()

print('Alunos matriculados na disciplina Laboratório de Programação:')
for aluno in alunos:
    print(aluno)
    
print()

# Liste apenas os nomes dos alunos matriculados

print('Nome dos alunos matriculados na disciplina Laboratório de Programação:')
for nome in alunos:
    print(nome[0])

print()    

# Liste os nomes dos alunos com suas respectivas notas

print('Alunos com suas respectivas notas:')
for nome, notas in alunos:
    print(f'Nome: {nome}, Notas: {notas}')

print()

# Liste os nomes dos alunos, suas notas e a média final

for nome, notas in alunos:
    soma_notas = 0
    media_final = 0
    quant_notas = 0

    for nota in notas:
        soma_notas += nota
        quant_notas += 1

    media_final = soma_notas / quant_notas

    print(f'Nome: {nome}, Notas: {notas}, Média Final: {media_final}')        

print()   

# Calcule a média aritmética geral da turma

for nome, notas in alunos:
    soma_notas = 0
    quant_notas = 0
    soma_total_notas = 0
    quant_total_notas = 0

    for nota in notas:
        soma_notas += nota
        quant_notas += 1

    soma_total_notas += soma_notas
    quant_total_notas += quant_notas

media_geral = soma_total_notas / quant_total_notas
print(f'Média Geral da turma de Laboratório de Programação: {media_geral}')

print()
