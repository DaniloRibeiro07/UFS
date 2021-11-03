dados_pessoais={}
total=total_pessoas=0
while True:
    idade=int(input())
    if idade==-1:
        break

    dados_pessoais[idade]=input().split()
    if 18<=idade<=35 and dados_pessoais[idade] == ['f','l','v']:
        total+=1
    total_pessoas+=1

print("Mais velho:",max(dados_pessoais.items())[0])

print("Mulheres com olhos verdes, loiras com 18 a 35 anos: %.2f"%(total/total_pessoas*100) + "%")

