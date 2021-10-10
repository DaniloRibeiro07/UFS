listanum=[int(input()) for cont in range(101)]
#busca e apreensão
cont=0
while True:
    try:
        if listanum.count(listanum[-1])<=1:
            break
        print(listanum.index(listanum[-1])+cont)
        listanum.pop(listanum.index(listanum[-1]))
        cont+=1
    except:
        break
