def cont_buraco(palavra):
    contburaco=0
    for caractere in palavra:
        if caractere=='A' or caractere=='O' or caractere=='P' or caractere=='R' or caractere == 'D' or caractere=='Q':
            contburaco+=1
        elif caractere=='B':
            contburaco+=2
    return contburaco
    
max=int(input())

for cont in range(max):
    texto = input()
    print(cont_buraco(texto))