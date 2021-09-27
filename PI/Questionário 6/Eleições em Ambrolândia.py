num=int(input())
cont93=cont83=contbranco=contnulo=0
while num>=0:
    if num==93:
        cont93=cont93+1
    elif num==83:
        cont83=cont83+1
    elif num==0:
        contbranco=contbranco+1
    else:
        contnulo=contnulo+1
    num=int(input())
print(cont83)
print(cont93)
print(contbranco)
print(contnulo)
if cont83>cont93:
    print('83')
else:
    print('93')
totalvotos=cont83+cont93+contbranco
print("%.2f"%(cont83*100/totalvotos))
print("%.2f"%(cont93*100/totalvotos))