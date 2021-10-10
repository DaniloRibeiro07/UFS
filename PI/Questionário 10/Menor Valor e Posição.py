def converteremX(lista,x):
    for cont in range(len(lista)):
        lista[cont]=x(lista[cont])

tamanho=input()
listanum=input().split()
converteremX(listanum,int)
print("Menor valor: %d"%min(listanum))
print('Posicao: %d'%(listanum.index(min(listanum))))