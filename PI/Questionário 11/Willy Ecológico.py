n_arvores,tamanho=[int(i) for i in input().split()]
array_arvores=[int(i) for i in input().split()]

array_arvores.sort()
menor_tamanho=array_arvores[-1]
soma=0
for i in range(n_arvores):
    for n in range(n_arvores):
        if array_arvores[n]-array_arvores[i]>0:
           soma+=array_arvores[i]-array_arvores[n]
    if menor_tamanho>soma and soma>=tamanho:
        menor_tamanho=array_arvores[i]
        
print(menor_tamanho)