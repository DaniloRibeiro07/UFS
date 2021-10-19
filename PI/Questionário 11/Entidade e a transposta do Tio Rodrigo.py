tamanho=int(input())
matriz=[[int(i)for i in input().split()]for u in range(tamanho)]
matrizmaluca=[[0 for i in range(tamanho)]for u in range(tamanho)]

for i in range(tamanho):#dobra a diagonal secundária
    matriz[i][tamanho-1-i]=str(matriz[i][tamanho-1-i]*2)

for i in range(tamanho):#inverte a diagonal principal
    matrizmaluca[i][i]=str(matriz[tamanho-1-i][tamanho-1-i])

for i in range(tamanho):#transposição
	for j in range(i+1,tamanho):
		matrizmaluca[j][i]=str(matriz[i][j])
		matrizmaluca[i][j]=str(matriz[j][i])
        

for i in matrizmaluca:#impressão
		print(" ".join(i)+' ')