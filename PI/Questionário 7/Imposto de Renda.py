def if_inteligente(P1,P2,Multiplicador):
    if P1<=P2:
        return(P1*Multiplicador)
    else:
        return((P2)*Multiplicador)

renda=float(input())
renda=renda-2000
total=0
if renda>0:
    total=if_inteligente(renda,1000,0.08)
    renda=renda-1000
if renda>0:
    total=total+if_inteligente(renda,1500,0.18)
    renda=renda-1500
if renda>0:
    total=total+renda*0.28

if total!=0:
    print("R$ %.2f"%total) 
else:
    print("Isento")