def converteremX(lista,x):
    for cont in range(len(lista)):
        lista[cont]=x(lista[cont])


listadenum=input().split()
converteremX(listadenum,int)
print(max(listadenum))
