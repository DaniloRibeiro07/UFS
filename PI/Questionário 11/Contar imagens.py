linhas1,colunas1=[int(i)for i in input().split()]
matriz1=[[int(i)for i in input().split()]for u in range(linhas1)]

linhas2,colunas2=[int(i)for i in input().split()]
lista2=list()
for cont in range(linhas2):
    for i in input().split():
        for u in i:
            lista2.append(int(u))

segmentacao=list()
for cont_linp in range(0,linhas1):
    if cont_linp+linhas2>linhas1:
                break
    for cont_colp in range(0,colunas1):
        if cont_colp+colunas2>colunas1:
                    break
        segmentacao_aux=list()
        for cont_linaux in range(cont_linp,linhas2+cont_linp):
            for cont_colaux in range(cont_colp,colunas2+cont_colp):
                segmentacao_aux.append(matriz1[cont_linaux][cont_colaux])
        segmentacao.append(segmentacao_aux.copy())

dentro=0
for i in segmentacao: 
    if lista2==i:
        dentro+=1
print(dentro)

