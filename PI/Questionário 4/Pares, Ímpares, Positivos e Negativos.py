n=int(input())
if n>0:
    texto='POSITIVO '
elif n<0:
    texto='NEGATIVO '
if n==0:
    texto='NULO'
elif n%2==0:
    texto=texto+'PAR'
else:
    texto=texto+'IMPAR'
print(texto)