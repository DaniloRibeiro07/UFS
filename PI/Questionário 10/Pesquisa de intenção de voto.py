def vantagem(candidato,concorrente,x):
    converteremX(candidato,float)
    converteremX(concorrente,float)
    maiordiferenca=0
    for cont in range(x):
        diferenca=candidato[cont]-concorrente[cont]
        if diferenca>maiordiferenca:
            maiordiferenca=diferenca
    return(maiordiferenca)

def converteremX(lista,x):
    for cont in range(len(lista)):
        lista[cont]=x(lista[cont])


tamanho=int(input())
intencaocandidato=input().split()
intencaoconcorrente=input().split()

print("%.2f"%vantagem(intencaocandidato,intencaoconcorrente,tamanho))
