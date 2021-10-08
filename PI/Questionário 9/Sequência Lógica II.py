entradas=input().split()

num1=int(entradas[0])
num2=int(entradas[1])

for cont in range(1,num2+1,num1):
    texto=''
    for cont2 in range(1,num1+1):
        texto=texto+str(cont)+' '
        cont+=1
        if(cont>num2):
            break
    print(texto[:-1])
