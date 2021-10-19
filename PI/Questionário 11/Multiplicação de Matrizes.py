#configuração das matrizes
linA,colA_linB,colB=[int(i) for i in input().split()]
#receber matrizes
matrizA=[[int(j) for j in input().split()]for i in range(linA)]
matrizB=[[int(j) for j in input().split()]for i in range(colA_linB)]
#multiplicação
lista=list()
matriz_result=list()
for i in range(linA):
    for u in range(colB):
        soma=0
        for j in range(colA_linB):
            soma+=matrizA[i][j]*matrizB[j][u]
        lista.append(str(soma))
    matriz_result.append(lista.copy())
    lista.clear()
#resultado
for i in matriz_result:
    print(" ".join(i))