def AnalisarSituacao(n1,n2,n3,n4):
    media=(n1*1+n2*2+n3*3+n4*4)/(1+2+3+4)
    if media>=9:
        return("aprovado com louvor")
    elif media>=7:
        return("aprovado")
    elif media<3:
        return('reprovado')
    else:
        return("prova final")

valores=input().split()
print(AnalisarSituacao(float(valores[0]),float(valores[1]),float(valores[2]),float(valores[3])))

