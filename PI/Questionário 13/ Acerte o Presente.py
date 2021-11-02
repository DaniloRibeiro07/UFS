participantes=int(input())

desejos_participantes={}
for x in range(participantes):
    entrada=input().split()
    participante=entrada[0]
    desejos=[entrada[i] for i in range(1,4)]
    desejos_participantes[participante]=desejos

while True:
    entrada=input()
    if entrada=="FIM":
        break
    participante,testar_desejo=entrada.split()
    if testar_desejo in desejos_participantes[participante]:
        print("Uhul! Seu amigo secreto vai adorar")
    else:
        print("Tente Novamente!")