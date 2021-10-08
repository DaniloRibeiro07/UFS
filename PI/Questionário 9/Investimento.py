entrada=input().split()
montante=float(entrada[0])
juros=float(entrada[1])
anos=int(entrada[2])

for cont in range(anos*4):
    print("Rendimento: %.2f Montante: %.2f"%(montante*juros, montante*(1+juros)))
    montante=montante*(1+juros)