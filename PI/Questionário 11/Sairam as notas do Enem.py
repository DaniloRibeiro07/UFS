def BuscaBinaria(valor,lista):
    return BuscaBinariaEm(0,len(lista)-1,valor,lista)

def BuscaBinariaEm(inicio,fim,valor,lista):
    meio=(inicio+fim)//2
    while inicio<=fim and valor != lista[meio]:
        if valor<lista[meio]:
            fim=meio-1
        else:
            inicio=meio+1
        meio=(inicio+fim)//2
    if inicio<=fim:
        return [True,meio]
    else:
        return [False]

n_inscritos_apresentados=int(input())
lista_cpf_apresentados=[int(input())for i in range(n_inscritos_apresentados)]
lista_notas=[int(input())for i in range(n_inscritos_apresentados)]
testes=int(input())

for i in range(testes):
    teste=BuscaBinaria(int(input()),lista_cpf_apresentados)
    if teste[0]:
        print(lista_notas[teste[1]])
    else:
        print("NAO SE APRESENTOU")