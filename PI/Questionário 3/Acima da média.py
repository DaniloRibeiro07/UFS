numeros = [float(input()), float(input()), float(input())]
m = (numeros[0]+numeros[1]+numeros[2])/3
n1 = n2 = 0
while n1 < 3:
    if numeros[n1] > m:
        n2 += 1
    n1 += 1
print(n2)
