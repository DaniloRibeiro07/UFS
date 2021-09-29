Forca,Inteligencia,Destreza,Furtividade,Peso=int(input()),int(input()),int(input()),int(input()),int(input())

if Forca>5 and Destreza>5 and Peso>5:
    print('Knight')
elif Forca<5 and Inteligencia>5 and Furtividade>5 and Peso<5:
    print('Mage')
elif Forca>5 and Destreza>5 and Furtividade >5 and Peso<5:
    print('Paladin')
else:
    print('Orc')