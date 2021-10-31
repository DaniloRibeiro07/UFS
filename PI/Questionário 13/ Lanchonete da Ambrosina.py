quant_prod_a_cadastra=int(input())
produtos={}

for x in range(quant_prod_a_cadastra):
    codigo_do_produto=int(input())
    nome_do_produto=input()
    preco_do_produto=float(input())
    produtos[codigo_do_produto]=preco_do_produto

total=0
while True:
    pedido_codigo_do_produto=int(input())
    if pedido_codigo_do_produto==0:
        break
    quantidade_do_pedido=int(input())
    if quantidade_do_pedido<0:
        continue
    total+=produtos.get(pedido_codigo_do_produto,0)*quantidade_do_pedido

print("%.2f"%total)


