def ContaDigitosPares(numero):
    if len(numero)==1:
        if int(numero)%2==0:
            return 1
        else:
            return 0
    else:
        if int(numero[0])%2==0:
            return 1+ContaDigitosPares(numero[1:])
        else:
            return ContaDigitosPares(numero[1:])

print(ContaDigitosPares(input()))