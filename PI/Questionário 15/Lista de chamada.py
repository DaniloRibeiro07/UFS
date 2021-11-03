quant_alunos, n_sorteado=[int(i) for i in input().split()]
lista_alunos=[input() for i in range(quant_alunos)]
lista_alunos.sort()
print(lista_alunos[n_sorteado-1])