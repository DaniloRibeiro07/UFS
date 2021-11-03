dados_clientes={}
for x in range(100):
  nome=input()
  if nome=="SAIR":
    break
  senha=input()
  situacao_mensalidade=input()
  dados_clientes[nome]=(senha,situacao_mensalidade)

while True:
  senha_a_ser_testada=input()
  if senha_a_ser_testada=='-1':
    break

  for nome, senha_situacao_mensalidade in dados_clientes.items():
    if senha_situacao_mensalidade[0]==senha_a_ser_testada:
      if senha_situacao_mensalidade[1]=='P':
        print(nome+", seja bem-vindo(a)!")
      else:
        print("Não está esquecendo de algo,",nome+"? Procure a recepção!")

    else:
      print("Seja bem-vindo(a)! Procure a recepção!")

