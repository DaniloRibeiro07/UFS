def MaiorAB(a,b):
    return((a+b+abs(a-b))//2)

valores=input().split()
a,b,c=int(valores[0]),int(valores[1]),int(valores[2])
print(MaiorAB(MaiorAB(a,b),c), "eh o maior")