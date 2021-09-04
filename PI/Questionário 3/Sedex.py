d = int(input())
dimensoes = input().split()
a, l, p = int(dimensoes[0]), int(dimensoes[1]), int(dimensoes[2])

if d <= a and d <= l and d <= p:
    print("S")
else:
    print("N")
