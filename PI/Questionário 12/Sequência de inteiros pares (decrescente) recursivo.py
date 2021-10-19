def imprimir_decrescente(numero):
    if numero%2!=0:
        return imprimir_decrescente(numero-1)
    else:
        print(numero)
        if numero==0:
            return 0
        else:
            imprimir_decrescente(numero-2)

imprimir_decrescente(int(input()))