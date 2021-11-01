#uma sequência de 37 pares inteiros, indicando numero de voo e vagas
voos={}
for x in range(37):
  numero_de_voo,vagas=[int(i) for i in input().split()]
  voos[numero_de_voo]=vagas

while True:
  entrada=input()
  if entrada=="9999":
    break
  identidade,voo_desejado=[int(i) for i in entrada.split()]

  if voos.get(voo_desejado,0):
    print(identidade)
    voos[voo_desejado]-=1
  else:
    print("INDISPONIVEL")