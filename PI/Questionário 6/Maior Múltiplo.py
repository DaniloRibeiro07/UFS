m,n=int(input()),int(input())
x,y=1,m
if m*x<=n:
    while m*x<=n:
        y=m
        y=y*x
        x=x+1
else:
    y='sem multiplos menores que '+str(n)
print(y)