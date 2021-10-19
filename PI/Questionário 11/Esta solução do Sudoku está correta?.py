def processamento_sudoku(lista):
    for i in lista:
        for j in i:
            if i.count(j) != 1:
                return "NAO"

    lista2=[[lista[u][i] for u in range(9)]for i in range(9)]

    for i in lista2:
        for j in i:
            if i.count(j) != 1:
                return "NAO"
    
    return "SIM"

quant_matriz=int(input())
for cont in range(quant_matriz):
    lista=[[int(u) for u in input().split()]for i in range(9)]
    print("Instancia",cont+1)
    print(processamento_sudoku(lista))
    print()
    lista.clear()