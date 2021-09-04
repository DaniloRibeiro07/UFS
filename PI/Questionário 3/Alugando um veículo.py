dias, quilometro = int(input()), int(input())
quilometro -= dias*100
if quilometro < 0:
    print("%.2f" % float(dias*90))
else:
    print("%.2f" % float(dias*90+quilometro*12))
