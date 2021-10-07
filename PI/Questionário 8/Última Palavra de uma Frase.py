texto=input()

if texto.rfind(' ')==-1:
    cont=0
else:
    cont=texto.rfind(' ')+1

print(texto[cont:len(texto)])
    