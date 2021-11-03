def ordenar_lista(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    print("\n".join(lista))
    
def criacao_de_lista():
    lista_aux=[]
    while True:
        nome=input()
        if nome=="FIM":
            break
        lista_aux.append(nome)
    ordenar_lista(lista_aux)
    return(lista_aux)

listanomes=[]
for x in range(2):
    listanomes+=criacao_de_lista()
    print("-"*50)

ordenar_lista(listanomes)
