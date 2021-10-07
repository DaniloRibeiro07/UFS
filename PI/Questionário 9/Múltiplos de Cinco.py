import math

entrada=input().split()
comeco=math.ceil(int(entrada[0])/5)*5
fim=int(entrada[1])
texto=str(comeco)
print(comeco)

for num in range(comeco+5,fim+1,5):
    texto=texto+'|'
    texto=texto+str(num)
    
print(texto)
