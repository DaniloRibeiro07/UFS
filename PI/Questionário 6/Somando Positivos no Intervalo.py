def MaiorAB(a,b):
    return((a+b+abs(a-b))//2)

n1,n2=int(input()),int(input())
MaiorNum=MaiorAB(n1,n2)
s=0

if ((n1+n2)-MaiorNum)>0:
    x=(n1+n2)-MaiorNum
else:
    x=0

while x<=MaiorNum:
    s=s+x
    x=x+1

print(s)