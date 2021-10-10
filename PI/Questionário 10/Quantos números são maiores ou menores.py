tamanho=int(input())
listanum=[int(input()) for cont in range(tamanho)]
medialista=(sum(listanum)/len(listanum))
print("%.2f"%medialista)

contaux=0
for cont in listanum:
     if cont>=medialista*1.1:
         contaux+=1
print(contaux)

contaux=0
for cont in listanum:
     if cont<=medialista*0.9:
         contaux+=1
print(contaux)