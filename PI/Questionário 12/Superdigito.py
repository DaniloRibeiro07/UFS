def superdigito(numero):
    if len(numero)==1:
        return numero
    else:
        cont=0
        for num in numero:
            cont+=int(num)
        return superdigito(str(cont))

numero,multi=input().split()
print(superdigito(numero*int(multi)))