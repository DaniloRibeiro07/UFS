def conserto(texto):
    if len(texto)<=1:
        return texto
    elif texto[0]==texto[1]:
        return conserto(texto[1:])
    else:
        return texto[0]+conserto(texto[1:])


while True:
    texto=input()
    if texto=='*':
        break
    if texto=='':
        continue
    print(conserto(texto))