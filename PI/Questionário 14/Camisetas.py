while True: 
  quantidade_camisas=int(input())
  if quantidade_camisas==0:
    break
  dados_camisas={}
  for i in range(quantidade_camisas):
    aluno=input()
    dados_camisas[aluno]=input().split()
  lista_dados_camisas=list()
  for aluno, cor_tamanho in dados_camisas.items():
    lista_dados_camisas.append((cor_tamanho[0],cor_tamanho[1],aluno))

  for i in range(len(lista_dados_camisas)-1,0,-1):
    for j in range(i):
      if lista_dados_camisas[j][0]>lista_dados_camisas[j+1][0]:
        lista_dados_camisas[j],lista_dados_camisas[j+1]=lista_dados_camisas[j+1],lista_dados_camisas[j]
      if lista_dados_camisas[j][1]<lista_dados_camisas[j+1][1] and lista_dados_camisas[j][0]==lista_dados_camisas[j+1][0]:
        lista_dados_camisas[j],lista_dados_camisas[j+1]=lista_dados_camisas[j+1],lista_dados_camisas[j]
      if lista_dados_camisas[j][2]>lista_dados_camisas[j+1][2] and lista_dados_camisas[j][0]==lista_dados_camisas[j+1][0] and lista_dados_camisas[j][1]==lista_dados_camisas[j+1][1]:
        lista_dados_camisas[j],lista_dados_camisas[j+1]=lista_dados_camisas[j+1],lista_dados_camisas[j]

  for dado in lista_dados_camisas:
    print(" ".join(dado))
  print()