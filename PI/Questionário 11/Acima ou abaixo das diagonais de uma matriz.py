def processar_soma_matriz(diagonal,tipo_de_matriz,matriz):
    soma=0

    if diagonal=='acima':
        for i in range(tipo_de_matriz):
            for j in range(i+1,tipo_de_matriz):
               soma+=matriz[i][j]
    else:
        for i in range(1,tipo_de_matriz):
            for j in range(i):
                soma+=matriz[i][j]
        
    return(soma)
diagonal=input()
numero_base=int(input())
tipo_de_matriz=int(input())
matriz=[[int (i) for i in input().split()] for j in range(tipo_de_matriz)]

print(processar_soma_matriz(diagonal,tipo_de_matriz,matriz)>numero_base)
