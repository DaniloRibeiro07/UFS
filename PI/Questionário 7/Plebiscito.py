contsim=contnao=contnulo=0
voto=str(input()).lower()
while voto!="encerrar":
    if voto=='sim':
        contsim=contsim+1
    elif voto=='nao':
        contnao=contnao+1
    else:
        contnulo=contnulo+1
    voto=str(input()).lower()
    print(voto)

if contsim>contnulo+contnao:
    print("COM FOGOS")
else:
    print("SEM FOGOS")