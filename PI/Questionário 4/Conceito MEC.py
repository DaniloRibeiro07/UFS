livros,alunos=int(input()),int(input())

if livros*8>=alunos:
    print('A')
elif livros*12>=alunos:
    print('B')
elif livros*18>=alunos:
    print('C')
else:
    print("D")