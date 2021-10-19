def fibonnaci(proximo,anterior,tamanho):
    if tamanho<=1:
        return proximo
    else:
        proximo = proximo + anterior
        anterior = proximo - anterior
        if(proximo == 0):
            proximo = proximo + 1
        return fibonnaci(proximo,anterior,tamanho-1)

def fibonnaci_invertido(tamanho):
    if tamanho==0:
        return ''
    else:
        return str(fibonnaci(0,0,tamanho))+' '+fibonnaci_invertido(tamanho-1)

print(fibonnaci_invertido(int(input())))