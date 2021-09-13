def ClassificaAluno(media,faltas):
    if faltas>10:
        return('REPROVADO POR FALTAS')
    elif media>=9.5:
        return("APROVADO COM LOUVOR")
    elif media>=7:
        return("APROVADO")
    else:
        return("REPROVADO")

print(ClassificaAluno(float(input()),int(input())))