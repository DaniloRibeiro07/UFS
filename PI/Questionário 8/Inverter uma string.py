texto=input()
palavrainvertida=''

for positexto in range(len(texto)-1,-1,-1):
    palavrainvertida=palavrainvertida+texto[positexto]

print(palavrainvertida)