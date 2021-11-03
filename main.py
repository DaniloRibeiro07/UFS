figurinhas= int(input())
cont_joao=0
cont_maria=0
lista_series=[]
lista_j=[]
lista_m=[]
for i in range(figurinhas):
    serie= int(input())
    lista_series.append(serie)


for valor in lista_series:
    if valor%2==0:
        cont_joao+=1
        if  valor not in lista_j:
            lista_j.append(valor)
    else:
        cont_maria+=1
        if valor not in lista_j:
            lista_m.append(valor)

if sum(lista_m)>sum(lista_j):
    print(lista_m)
else:
    print(lista_j)

print(cont_joao)
print(cont_maria)