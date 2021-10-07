repeticao=int(input())

for none in range(repeticao):
    texto=input().upper()
    texto=texto.replace(' ','')
    if texto==texto[::-1]:
        print('SIM')
    else:
        print('NAO')