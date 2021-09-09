l1,l2,l3=int(input()), int(input()), int(input())

if l1==l2==l3:
    print("equilatero")
elif l1==l2 or l1==l3 or l2==l3:
    print("isosceles")
else:
    print("escaleno")