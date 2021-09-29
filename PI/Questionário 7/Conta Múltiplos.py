num1,num2=int(input()),int(input())
contador,numerosmultiplos=1,0

while contador<50:
    if not(contador%num1) and not(contador%num2):
        numerosmultiplos=numerosmultiplos+1
    contador=contador+1
print(numerosmultiplos)