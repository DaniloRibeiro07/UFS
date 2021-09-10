n1,n2,n3=int(input()),int(input()), int(input())

if n1!=n2 and n1!=n3:
    print('A')
elif n2!=n1 and n2!=n3:
    print('B')
elif n3!=n1 and n3!=n2:
    print('C')
else:
    print("*")
    