while True:
  n_de_correcoes,n_de_linhas_texto=[int(i) for i in input().split()]
  
  if n_de_correcoes==n_de_linhas_texto==0:
    break

  correcao={}
  for i in range(n_de_correcoes):
    palavra_errada,seta,palavra_certa=input().split()
    correcao[palavra_errada]=palavra_certa

  texto_apos_traducao=list()
  for i in range(n_de_linhas_texto):
    texto=input()
    for palavra_errada, palavra_certa in correcao.items():
      texto=texto.replace(palavra_errada,palavra_certa)

    texto_apos_traducao.append(texto)

  for texto in texto_apos_traducao:
    print("".join(texto))
