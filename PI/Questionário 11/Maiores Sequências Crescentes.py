linha,coluna=[int(i) for i in input().split()]
matriz=[[int(u)for u in input().split()]for i in range(linha)]
sequencias=list()

for i in matriz:
    anterior=contseq=seq=0
    for u in i:
        if u>=anterior:
            contseq+=1
        else:
            contseq=1
        if contseq>seq:
            seq=contseq
        anterior=u
    sequencias.append(seq)

for i in range(len(sequencias)):
    print("Linha %d: %d"%(i,sequencias[i]))

print("Maior Sequencia:",max(sequencias))
