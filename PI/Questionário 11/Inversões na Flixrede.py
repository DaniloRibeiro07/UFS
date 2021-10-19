tamanho_array=int(input())
array=[int(input())for i in range(tamanho_array)]
cont=0
for i in range(tamanho_array-1,0,-1):
    for j in range(i):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
            cont+=1

print(cont)