dados_passageiros={}
while True:
  n_passagem=int(input())
  if n_passagem==-1:
    break
  for i in range(4):
    lixo=input()
  poltrona=int(input())
  idade=int(input())
  nome_passageiro=input()
  idade_e_poltrona=(idade,poltrona)
  dados_passageiros[nome_passageiro]=idade_e_poltrona

tupla_dados_passageiros=[]
idade_total=0
for nome_passageiro,idade_e_poltrona in dados_passageiros.items():
  idade_total+=idade_e_poltrona[0]
  tupla_dados_passageiros.append((nome_passageiro,idade_e_poltrona))

idade_media=idade_total/(len(tupla_dados_passageiros))
for dado in tupla_dados_passageiros:
  if dado[1][0]>=idade_media and dado[1][1]%2==0:
    print(dado[0])