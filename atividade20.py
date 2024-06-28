numero1 = "+"
numero2 = "*"
numero3 = "-"


num1 = float(input("digite o 1º número"))
num2 = float(input("digite o 2º número"))
operacao = input("digite uma operacao - Adicional multiplicar e subitarir")
adicionar = num1 + num2
multiplicar = num1 * num2
subitrair = num1 - num2

if operacao == "adicionar":
    print(adicionar)

if operacao == "multiplicar":
    print(multiplicar)

if operacao == "subtrair":
    print(subitrair)