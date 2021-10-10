tamanho=int(input())
listanum=[[],[]]
for cont in range(2):
    for cont2 in range(tamanho):
        listanum[cont].append(int(input()))

for cont in range(tamanho):
    print(listanum[0][cont])
    print(listanum[1][cont])
