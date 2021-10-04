def contador_programavel(P1,P2,S):
    contador=0
    
    while contador<P1 and contador<P2:
        contador=contador+1
    
    return contador*S

def contadeagua(consumo):
    total=7
    
    if consumo>10:
        total=total+contador_programavel(consumo-10,20,1)
    if consumo>30:
        total=total+contador_programavel(consumo-30,100-30,2)
    if consumo>100:
        total=total+contador_programavel(consumo-100,consumo-100,5)
    return total

consumo=int(input())

print(contadeagua(consumo))

