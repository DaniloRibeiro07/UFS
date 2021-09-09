sal=float(input())
if sal>500:
    print("%.2f"%(sal*(1+0.1)))
elif sal>300:
    print("%.2f"%(sal*(1+0.07)))
else:
    print("%.2f"%(sal*(1+0.05)))