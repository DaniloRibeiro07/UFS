dict_paises_dados={}
while True:
  entrada=input()
  if entrada=='*':
    break
  pais,medalha=entrada.split(',')
  if pais not in dict_paises_dados:
    dict_paises_dados[pais]={}
    for medalha2 in ["ouro","prata","bronze"]:
      if medalha2 not in dict_paises_dados[pais]:
        dict_paises_dados[pais][medalha2]=0
  dict_paises_dados[pais][medalha]=dict_paises_dados[pais].get(medalha,0) +1
 
lista_paises_dados=list()
for pais, medalha_quantmedalha in dict_paises_dados.items():
  lista_aux=[]
  for medalha, quantmedalha in medalha_quantmedalha.items():
    lista_aux.append(quantmedalha) 
  lista_paises_dados.append((pais,lista_aux[0],lista_aux[1],lista_aux[2])) 

for i in range(len(lista_paises_dados)-1,0,-1):
  for j in range(i):
    if lista_paises_dados[j][1]<lista_paises_dados[j+1][1]:
      lista_paises_dados[j],lista_paises_dados[j+1]=lista_paises_dados[j+1],lista_paises_dados[j]
    if lista_paises_dados[j][2]<lista_paises_dados[j+1][2] and lista_paises_dados[j][1]<=lista_paises_dados[j+1][1]:
      lista_paises_dados[j],lista_paises_dados[j+1]=lista_paises_dados[j+1],lista_paises_dados[j]
    if lista_paises_dados[j][3]<lista_paises_dados[j+1][3] and lista_paises_dados[j][2]<=lista_paises_dados[j+1][2] and lista_paises_dados[j][1]<=lista_paises_dados[j+1][1]:
      lista_paises_dados[j],lista_paises_dados[j+1]=lista_paises_dados[j+1],lista_paises_dados[j]

cont=0
for dado in lista_paises_dados:
  cont+=1
  print("%d)%s ouro:%d prata:%d bronze:%d"%(cont,dado[0],dado[1],dado[2],dado[3]))