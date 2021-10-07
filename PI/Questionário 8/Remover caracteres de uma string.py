texto=input()
remover=input()

for letra in remover:
    texto=texto.replace(letra,'')

print(texto)
