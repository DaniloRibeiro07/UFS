s = int(input())
m = 0
h = 0
if s >= 3600:
    h = int(s/3600)
    s = s-h*3600
if s >= 60:
    m = int(s/60)
    s = int(s-m*60)
print("%d:%d:%d" % (h, m, s))
