n1,n2,n3=int(input()),int(input()),int(input())

if n3<=n1>=n2:
    print(n1)
    if n2>=n3:
        print(n2)
        print(n3)
    else:
        print(n3)
        print(n2)

elif n3<=n2>=n1:
    print(n2)
    if n1>=n3:
        print(n1)
        print(n3)
    else:
        print(n3)
        print(n1)
else:
    print(n3)
    if n1>=n2:
        print(n1)
        print(n2)
    else:
        print(n2)
        print(n1)