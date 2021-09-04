entrada = input()
entrada = entrada.split()
cons_agua = float(entrada[0])
custo_l = float(entrada[1])*1000
print("%.2f" % (cons_agua*custo_l))
print("%.2f" % (cons_agua*custo_l*0.8))
print("%.2f" % (cons_agua*custo_l*(1+0.8)))
