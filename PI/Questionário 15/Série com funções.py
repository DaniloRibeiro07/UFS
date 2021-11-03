def eh_primo(num):
    for cont in range(2,num):
        if num%cont==0:
            return False
    return True

def proximo_primo(num):
    if eh_primo(num):
        return num
    else:
        return proximo_primo(num+1)
        

def fatorial(numero):
    if numero<=1:
        return(1)
    else:
        return(numero*fatorial(numero-1))

tamanho=int(input())
resultado=0
num=0
text=""
for x in range(tamanho):
    num+=1
    den=proximo_primo(num)
    resultado+=fatorial(num)/den
    text+=str(num)+'!/'+str(den)+" + "

print(text[:-3])
print("%.2f"%resultado)
