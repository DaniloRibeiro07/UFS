Entrada_Nsen_Capac = input().split()
nsen,capac=int(Entrada_Nsen_Capac[0]), int(Entrada_Nsen_Capac[1])
result='N'
npessoa=0
while nsen>0:
    Entrada_Saida_Entrada = input().split()
    saida,entrada=int(Entrada_Saida_Entrada[0]),int(Entrada_Saida_Entrada[1])
    npessoa=npessoa-saida
    npessoa=npessoa+entrada
    if(npessoa>capac):
        result='S'
    nsen=nsen-1
print(result)