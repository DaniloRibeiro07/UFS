
dict_paises_dados={}
while True:
  entrada=input()
  if entrada=='*':
    break
  pais,medalha=entrada.split(',')
  if pais not in dict_paises_dados:
    dict_paises_dados[pais]={}
  dict_paises_dados[pais][medalha]=dict_paises_dados[pais].get(medalha,0) +1
  
count=0
for pais, medalha_quantidade in dict_paises_dados.items():
  count+=1
  lista_medalhas=list()
  for medalhas in ["ouro","prata","bronze"]:
    if medalhas in dict_paises_dados[pais]:
      lista_medalhas.append(dict_paises_dados[pais][medalhas])
    else:
      lista_medalhas.append(0)
  
  print("%d)"%count+pais,"ouro:%d prata:%d bronze:%d"%(lista_medalhas[0],lista_medalhas[1],lista_medalhas[2]))

