while True:
    a,b=[int(i) for i in input().split()]
    if a==b==0:
        break
    repeticoes={}
    for x in range(10):
            repeticoes[str(x)]=0
    for i in range(a,b+1):
        for x in range(len(str(i))):
            repeticoes[str(i)[x]]+=1
    lista_repeticoes=[]
    for numero, repeticao in repeticoes.items():
        lista_repeticoes.append(str(repeticao))
    print(" ".join(lista_repeticoes))
