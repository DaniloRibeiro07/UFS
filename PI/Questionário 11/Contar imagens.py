linhas1,colunas1=[int(i)for i in input().split()]
matriz1=[[int(i)for i in input().split()]for u in range(linhas1)]

linhas2,colunas2=[int(i)for i in input().split()]
matriz2=[[int(i)for i in input().split()]for u in range(linhas2)]

for cont in range(0,linhas1,linhas2):



'''lista2=list()
for cont in range(linhas2):
    for i in input().split():
        for u in i:
            lista2.append(int(u))


segmentacao=list()
cont_seg_ref=0
for cont in range(0,linhas1,linhas2):
    auxiliar=list()
    for cont2 in range(linhas2):
        cont_seg_aux=cont_seg_ref
        cont_seg_ref1=0
        for cont3 in range(0,colunas1,colunas2):
            
            for cont4 in range(colunas2):
                cont_seg_aux1=cont_seg_ref1
                auxiliar.append(matriz1[cont_seg_aux][cont_seg_aux1])
    segmentacao.append(auxiliar.copy())
    cont_seg_ref+=1






for colunas in range(colunas2,colunas1):
    lista1[colunas-colunas2:]



lista1=[1,2,3,4,5,6]
lista2=[1,2,3,4,5,6]
print(lista1)
'''

