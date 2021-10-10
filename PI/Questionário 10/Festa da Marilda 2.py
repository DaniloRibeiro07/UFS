def ordenar_lista(lista):
    listadefeituosa=lista.copy()
    lista.clear()
    listaordenada=lista
    for cont in range(len(listadefeituosa)):
        listaordenada.append(min(listadefeituosa))
        listadefeituosa.pop(listadefeituosa.index(min(listadefeituosa)))

listanomes=list()
frescura=['-' for cont in range(50)]

while True:
    nome=input()
    if nome=='FIM':
        break
    listanomes.append(nome)

while True:
    ordenar_lista(listanomes)
    print('\n'.join(listanomes))
    tamanho=int(input())
    if tamanho==0:
        break
    for cont in range(tamanho):
        listanomes.append(input())
    print(''.join(frescura))