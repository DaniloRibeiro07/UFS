n=int(input())
x=s=0
while x<n:
    if not(x%3):
        s=x+s
    elif not(x%5):
        s=x+s
    x=x+1
print(s)
