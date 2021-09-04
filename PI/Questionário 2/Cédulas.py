total = int(input())
n = 0
notas = [100, 50, 20, 10, 5, 2, 1]
print(total)
while n <= 6:
    print("%d nota(s) de R$ %d,00" % (total//notas[n], notas[n]))
    total = total-(total//notas[n])*notas[n]
    n += 1
