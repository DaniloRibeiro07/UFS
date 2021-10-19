n_arvores,tamanho=[int(i) for i in input().split()]
array_arvores=[int(i) for i in input().split()]

array_arvores.sort()
menor_tamanho=array_arvores[-1]
lista_altura=list()
lista_madeiracomida=list()
for i in range(n_arvores):
    madeira_comida=0
    for n in range(n_arvores):
        if array_arvores[n]-array_arvores[i]>0:
           madeira_comida+=array_arvores[n]-array_arvores[i]
    if madeira_comida-tamanho<0:
        continue
    lista_altura.append(array_arvores[i])
    lista_madeiracomida.append(madeira_comida)

print(lista_altura[lista_madeiracomida.index(min(lista_madeiracomida))])