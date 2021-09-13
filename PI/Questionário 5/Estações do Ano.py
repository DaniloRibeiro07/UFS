def EstacaoAno(dia,mes):
    if (dia>=21 and mes==9) or (12>mes>=10) or (dia<=20 and mes==12):
        return('PRIMAVERA')
    elif (dia>=21 and mes==12) or (3>mes>=1) or (dia<=20 and mes==3):
        return('VERAO')
    elif (dia>=21 and mes==3) or (6>mes>=4) or (dia<=20 and mes==6):
        return('OUTONO')
    else:
        return('INVERNO')

dia, mes=int(input()), int(input())
print(EstacaoAno(dia,mes))