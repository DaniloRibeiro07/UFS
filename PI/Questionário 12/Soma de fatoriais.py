def fatorial(numero):
    if numero<=1:
        return(1)
    else:
        return(numero*fatorial(numero-1))

def soma_dos_multiplode3(array):
    if len(array)==1:
        if array[0]%3==0:
            return fatorial(int(array[0]))
        else:
            return 0
    else:
        if array[0]%3==0:
            return (fatorial(int(array[0]))+soma_dos_multiplode3(array[1:]))
        else:
            return 0+soma_dos_multiplode3(array[1:])

array=[int(input())for i in range(5)]
print(soma_dos_multiplode3(array))