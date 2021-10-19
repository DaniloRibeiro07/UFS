def serie_de_miguelito(tamanho,teste):
    if tamanho==1:
        return 3
    else:
        if teste:
            return 4+serie_de_miguelito(tamanho-1,False)
        else:
            return 1+serie_de_miguelito(tamanho-1,True)

print(serie_de_miguelito(int(input()),True))