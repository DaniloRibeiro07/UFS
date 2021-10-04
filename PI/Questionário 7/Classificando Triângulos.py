entrada=input()
while entrada!='FIM':
    entrada=entrada.split()
    l1,l2,l3=int(entrada[0]),int(entrada[1]),int(entrada[2])
    if not(abs(l2-l3)<l1<l2+l3):
        print("INVALIDO")
    elif l1==l2==l3:
        print("EQUILATERO")
    elif l1==l2 or l1==l3 or l2==l3:
        print("ISOSCELES")
    else:
        print("ESCALENO")
    entrada=input()