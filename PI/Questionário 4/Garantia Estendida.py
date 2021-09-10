valor,gano=float(input()),int(input())

if gano==0:
    print('%.2f'%valor)
elif gano==1:
    print('%.2f'%(valor*(1+0.03)))
else:
    print('%.2f'%(valor*(1+0.05)))