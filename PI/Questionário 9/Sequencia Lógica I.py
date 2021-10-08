tamanho=int(input())
cont=cont2=cont3=1

for cont in range(1,tamanho+1):
    for x in range(2):
        print(cont, cont2, cont3)
        cont2+=1
        cont3+=1
    cont2=cont2+cont*2-1
    cont3=cont2*(cont+1)