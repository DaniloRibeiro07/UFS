tamanho=int(input())

cont1,cont3=1,3
texto,result='',0

while tamanho>0:
    texto=texto+str(cont1)+'/'+str(cont3)
    result=result+cont1/cont3
    cont1,cont3=cont1+1,cont3+3
    tamanho=tamanho-1
    if tamanho!=0:
        texto=texto+' + '
print(texto)
print("%.2f"%result)