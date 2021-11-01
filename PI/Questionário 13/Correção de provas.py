gabarito=input()
respostas={}
while True:
  entrada=input()
  if entrada=='9999':
    break
  numero,resposta=entrada.split()
  respostas[numero]=resposta

questoes=10

notas={}
cont_notas={}
alunos_aprovados=0
for numero,resposta in respostas.items():
  for cont in range(questoes):
    if gabarito[cont]==resposta[cont]:
      notas[numero]=notas.get(numero,0)+1
  
  notas[numero]=notas.get(numero,0)
  cont_notas[notas[numero]]=cont_notas.get(notas[numero],0)+1
  if notas[numero]>=6:
    alunos_aprovados+=1
  print(numero,float(notas[numero]))

print("%.1f"%(alunos_aprovados/int(numero)*100)+"%")

acertos_e_maior_repeticao=[0,0]
for acertos, repeticoes in cont_notas.items():
  if repeticoes>acertos_e_maior_repeticao[1]:
    acertos_e_maior_repeticao[0]=acertos
    acertos_e_maior_repeticao[1]=repeticoes
  
print(float(acertos_e_maior_repeticao[0]))