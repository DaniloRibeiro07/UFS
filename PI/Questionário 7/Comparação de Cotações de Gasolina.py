valorlitroEUA,valorlitroBR,precoDola=float(input())/3.8,float(input()),float(input())

print("Gasolina EUA: R$ %.2f"%(valorlitroEUA*precoDola))
print("Gasolina Brasil: R$ %.2f"%valorlitroBR)

if valorlitroEUA*precoDola==valorlitroBR:
    print("Igual")
elif valorlitroEUA*precoDola>valorlitroBR:
    print("Mais barata no Brasil")
else:
    print("Mais barata no EUA")


