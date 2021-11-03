dados_participante={}
while True:
    entrada=input()
    if entrada=="FIM":
        break
    participante,amigo=entrada.split()
    dados_participante[participante]=amigo

lista_dados_participantes=[]
amigo_ganho=''
for participante, amigo in dados_participante.items():
    lista_dados_participantes.append((participante,amigo))
    if len(amigo_ganho) < len(participante) and amigo=="YES":
        amigo_ganho=participante

for i in range(len(lista_dados_participantes)-1,0,-1):
    for j in range(i):
        if lista_dados_participantes[j][1] < lista_dados_participantes[j+1][1]:
            lista_dados_participantes[j],lista_dados_participantes[j+1]=lista_dados_participantes[j+1],lista_dados_participantes[j]
        if lista_dados_participantes[j][0] > lista_dados_participantes[j+1][0] and lista_dados_participantes[j][1] == lista_dados_participantes[j+1][1]:
            lista_dados_participantes[j],lista_dados_participantes[j+1]=lista_dados_participantes[j+1],lista_dados_participantes[j]
 
for dado in lista_dados_participantes:
    print(dado[0])
print()
print("Amigo do Habay:\n"+amigo_ganho)