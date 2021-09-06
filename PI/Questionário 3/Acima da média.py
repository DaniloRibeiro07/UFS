numero1=float(input())
numero2=float(input())
numero3=float(input())

m = (numero1+numero2+numero3)/3
n = 0

if numero1>m:
    n = n+1

if numero2>m:
    n = n+1

if numero3>m:
    n = n+1

print(n)