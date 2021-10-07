decodificador=" abcdefghijklmnopqrstuvwxyz"
while True:
    textocodificado=input().split()
    textodecodificado=''
    for num in textocodificado:
        textodecodificado=textodecodificado+decodificador[int(num)]

    if textodecodificado=='fim':
        break
    print(textodecodificado)