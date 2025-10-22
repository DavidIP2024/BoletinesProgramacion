artigo = input("Nome do artigo: ")
vendas = int(input("Vendas anuais: "))
if vendas <= 100:
    print("O artigo", artigo, "é de tipo baixo")
elif vendas <= 500:
    print("O artigo", artigo, "é de tipo medio")
elif vendas <= 1000:
    print("O artigo", artigo, "é de tipo alto")
else:
    print("O artigo", artigo, "é de tipo primeira necesidade")