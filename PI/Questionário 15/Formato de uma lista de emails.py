while True:
    email=input()
    if email=="sair":
        break
    if email.count('@')==1 and email.count('.')==2:
        posicao_arroba=email.index('@')
        email=email[posicao_arroba+1:]
        if posicao_arroba!=0:
            posicao_ponto=email.index('.')
            email=email[posicao_ponto+1:]
            if posicao_ponto!=0:
                posicao_ponto=email.index('.')
                email=email[posicao_ponto+1:]
                if posicao_ponto!=0 and len(email)!=0:
                    print("certo")
                else:
                    print("errado")
            else:
                print("errado")
        else:
            print("errado")
    else:
        print("errado")