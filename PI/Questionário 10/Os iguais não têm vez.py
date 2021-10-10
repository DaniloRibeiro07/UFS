def matarrepitido(lista):
    for cont in lista:
        for cont2 in range(lista.count(cont)-1):
            lista.pop(lista.index(cont))

def ordenarlista(lista):
    listadefeituosa=lista.copy()
    lista.clear()
    listaordenada=lista
    for cont in range(len(listadefeituosa)):
        listaordenada.append(min(listadefeituosa))
        listadefeituosa.pop(listadefeituosa.index(min(listadefeituosa)))

def converteremX(lista,x):
    for cont in range(len(lista)):
        lista[cont]=x(lista[cont])


tamanho=int(input())
listanum=input().split()

converteremX(listanum,int)
matarrepitido(listanum)
ordenarlista(listanum)
converteremX(listanum,str)

print(' '.join(listanum))