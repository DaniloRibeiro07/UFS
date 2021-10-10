def converteremX(lista,x):
    for cont in range(len(lista)):
        lista[cont]=x(lista[cont])



tamanho=input()
listanum=input().split()
listanum.reverse()
print(' '.join(listanum))
listanum.reverse()

listanum.append(listanum[0])
listanum.pop(0)
print(' '.join(listanum))

converteremX(listanum,int)
listanum.sort(reverse=True)
converteremX(listanum,str)
print(' '.join(listanum))
