def fatorial(numero):
    if numero<=1:
        return(1)
    else:
        return(numero*fatorial(numero-1))

while True:
    numero=int(input())
    if numero==-1:
        break
    print(fatorial(numero))