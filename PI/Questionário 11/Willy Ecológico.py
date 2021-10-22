def verificar_madeira_conseguida(quantidade_arvores,arvores,madeira_necessaria):
    lista_madeira_conseguida=list()
    for i in range(quantidade_arvores):
        madeira_conseguida=0
        for n in range(i+1,quantidade_arvores):
            madeira_conseguida+=arvores[n]-arvores[i]
        lista_madeira_conseguida.append(madeira_conseguida)
        
    for i in range(quantidade_arvores-1,-1,-1):
        if lista_madeira_conseguida[i]>=madeira_necessaria:
            return i

quantidade_arvores,madeira_necessaria=[int(i) for i in input().split()]
arvores=[int(i) for i in input().split()]
arvores.sort()#ordenar tamanho arvore
posicao=verificar_madeira_conseguida(quantidade_arvores,arvores,madeira_necessaria)
print(arvores[posicao])