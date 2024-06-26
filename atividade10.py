preco= float(input("digite p preço do seu produto:"))
porcentagem= float(input("digite a porcentagem:"))
desconto =preco  * porcentagem / 100
print(f"o valor do desconto é {desconto}[e o no preço do produto será {preco + desconto}")

