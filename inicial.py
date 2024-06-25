print("olá mundo")
print("bem vindo á programação")
print("primeiro estamos praticando o comando print")
print("esse comando printa 3 linhas de texto")
print("luana dukeviski antunes")
print("Rua Presidente João Gulart")
print(17)

#MEU PRIMEIRO SCRYPTI 
nome = input("digite seu nome")
print("olá" + nome)

#String F
resultado = 25
resultado2 = 30
print("o resultado da conta é:{}, e a conta de dois valores é {}".format(resultado,resultado2) )
print(f"o resultado da conta é:{resultado},e a conta de dois valores é {resultado2}")


#PRATICA 
nome = "luana"
idade = 17
skill1 = "python"
level1 = "iniciante"
skill2 = "java"
level2 = "senior"
skill3 = "c++"
level3 = "pleno"
baixo = 2000
alto = 3000

print(f"meu nome é{nome},tenho {idade} anos")
print(f"minhas habilidades são{skill1},{level1},{skill2},{level2},{skill3},{level3}")
print(f"procuro um emprego com um salário de {baixo} a {alto} euros por mês")


#operadores
ano =int(input("coloque aqui o ano de nscimento"))
input(f"ao final do ano voce terá: {2024 - ano}")

#exemplos
altura = float(input("qual sua altura?"))
peso = float(input("qual seu peso?"))

imc = peso/(altura/100)**2

print(f"o IMC é: {imc}")