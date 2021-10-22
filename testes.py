txt = input().split()
linha_A = int(txt[0])
coluna_A_Linha_B = int(txt[1])
coluna_B = int(txt[2])

m1 = [[int(c) for c in input().split()] for l in range(linha_A)]
m2 = [[int(j) for j in input().split()] for line in range(coluna_A_Linha_B)]

soma = 0
m3 = []
matriz = []
for linha in range(linha_A):
    for coluna in range(coluna_B):
        soma = 0
        for coluna_linha in range(coluna_A_Linha_B):
            soma += m1[linha][coluna_linha] * m2[coluna_linha][coluna]
        matriz.append(str(soma))
    m3.append(matriz.copy())
    matriz.clear()

for i in m3:
    print(" ".join(i))