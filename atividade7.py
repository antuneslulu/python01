preco = float(input("digite preço do produto:"))
porcentagem = float(input("digite a porcentagem"))
desconto = preco * porcentagem / 100
print(f"o valor do desconto é {desconto} e o novo preço será {preco - desconto}")