cont,cont2=7,0
money=0
total=0
while cont>0:
    money2=float(input())
    if(money2>=money+0.5):
        cont2=cont2+1
    total=money2+total
    money=money2
    cont=cont-1
print("R$ %.2f"%total)
print(cont2-1)