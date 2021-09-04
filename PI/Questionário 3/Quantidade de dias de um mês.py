mes = int(input())
ano = int(input())
anos31 = [1, 3, 5, 7, 8, 10, 12]
x = 0
if mes == 2:
    if ano % 4 == 0:
        print(29)
    else:
        print(28)
else:
    while x < 7:
        if(anos31[x] == mes):
            print(31)
            exit()
        x += 1
    print(30)
