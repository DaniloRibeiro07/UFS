lista_progII=[i for i in input().split()]
lista_progIII=[i for i in input().split()]
lista_alunos_dupla=[]
for aluno in lista_progII:
    if aluno in lista_progIII:
        lista_alunos_dupla.append(aluno)

print(" ".join(lista_alunos_dupla))