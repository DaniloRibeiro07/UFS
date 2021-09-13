def velkmh(V0, A, T):
    return((V0+A*T)*3.6)

def entrada():
    return(float(input()))

def MenorVelocidade(a,b,c):
    x=(a+b-abs(a-b))/2
    x=(x+c-abs(x-c))/2
    return('%.1f'%x)

vel1,vel2,vel3=velkmh(entrada(),entrada(),entrada()),velkmh(entrada(),entrada(),entrada()),velkmh(entrada(),entrada(),entrada())
print(MenorVelocidade(vel1,vel2,vel3))

