mes, ano = int(input()), int(input())

if mes == 2 and ano % 4 == 0:
    print(29)
if mes == 2 and ano % 4 != 0:
    print(28)

if mes==1 or mes==3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print(31)
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print(30) 