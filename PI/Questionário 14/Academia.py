dados_clientes={}
for x in range(100):
  nome=input()
  if nome=="SAIR":
    break
  senha=input()
  situacao_mensalidade=input()
  dados_clientes[senha]=(nome,situacao_mensalidade)

while True:
  senha_a_ser_testada=input()
  if senha_a_ser_testada=='-1':
    break
  if senha_a_ser_testada in dados_clientes:
    (nome,situacao_mensalidade)=dados_clientes[senha_a_ser_testada]
    if situacao_mensalidade=='P':
      print(nome+", seja bem-vindo(a)!")
    else:
      print("Não está esquecendo de algo,",nome+"? Procure a recepção!")
  else:
    print("Seja bem-vindo(a)! Procure a recepção!")