tamanho=int(input())
matriz=[[int(i)for i in input().split()]for u in range(tamanho)]

coluna=linha=morte=ant_coluna=ant_linha=0
while True:
    if tamanho-1==coluna==linha:
        print('OK')
        break
    elif coluna==tamanho-1 and linha!=tamanho-1 and not(morte):
        if matriz[linha][coluna] and matriz[linha+1][coluna] and ant_linha!=linha+1:
            ant_linha=linha
            linha+=1
            ant_coluna=500
        elif matriz[linha][coluna] and matriz[linha][coluna-1] and coluna-1!=ant_coluna:
            ant_coluna=coluna
            coluna-=1
            ant_linha=500
        elif matriz[linha][coluna] and matriz[linha-1][coluna] and ant_linha!=linha-1:
            ant_linha=linha
            linha-=1
        else:
            morte=1
    elif linha==tamanho-1 and coluna!=tamanho-1 and not(morte):
        if matriz[linha][coluna] and matriz[linha][coluna+1] and coluna+1!=ant_coluna:
            ant_coluna=coluna
            coluna+=1
            ant_linha=500
        elif matriz[linha][coluna] and matriz[linha][coluna-1] and coluna-1!=ant_coluna:
            ant_coluna=coluna
            coluna-=1
            ant_linha=500
        elif matriz[linha][coluna] and matriz[linha-1][coluna] and ant_linha!=linha-1:
            ant_linha=linha
            linha-=1
        else:
            morte=1
    elif coluna!=0 and not(morte):
        if matriz[linha][coluna] and matriz[linha+1][coluna] and ant_linha!=linha+1:
            ant_linha=linha
            linha+=1
            ant_coluna=500
        elif matriz[linha][coluna] and matriz[linha][coluna+1] and coluna+1!=ant_coluna:
            ant_coluna=coluna
            coluna+=1
            ant_linha=500
        elif matriz[linha][coluna] and matriz[linha][coluna-1] and coluna-1!=ant_coluna:
            ant_coluna=coluna
            coluna-=1
            ant_linha=500
        elif matriz[linha][coluna] and matriz[linha-1][coluna] and ant_linha!=linha-1:
            ant_linha=linha
            linha-=1
        else:
            morte=1
    elif coluna==0 and not(morte):
        if matriz[linha][coluna] and matriz[linha+1][coluna]and ant_linha!=linha+1:
            ant_linha=linha
            linha+=1
            ant_coluna=500
        elif matriz[linha][coluna] and matriz[linha][coluna+1] and coluna+1!=ant_coluna:
            ant_coluna=coluna
            coluna+=1
        elif matriz[linha][coluna] and matriz[linha-1][coluna] and ant_linha!=linha-1:
            ant_linha=linha
            linha-=1
        else:
            morte=1
    else:
        print('NOT OK')
        break
