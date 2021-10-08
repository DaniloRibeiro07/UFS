def contar_vogais(vogais,frase):
    soma=0

    for carac in vogais:
        soma=soma+frase.count(carac)

    return soma

tamanho=int(input())

for cont in range(tamanho):
    print(contar_vogais(input(),input()))