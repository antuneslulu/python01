# print("olá mundo")
# print("bem vindo á programação")
# print("primeiro estamos praticando o comando print")
# print("esse comando printa 3 linhas de texto")
# print("luana dukeviski antunes")
# print("Rua Presidente João Gulart")
# print(17)

# #MEU PRIMEIRO SCRYPTI 
# nome = input("digite seu nome")
# print("olá" + nome)

# #String F
# resultado = 25
# resultado2 = 30
# print("o resultado da conta é:{}, e a conta de dois valores é {}".format(resultado,resultado2) )
# print(f"o resultado da conta é:{resultado},e a conta de dois valores é {resultado2}")


# #PRATICA 
# nome = "luana"
# idade = 17
# skill1 = "python"
# level1 = "iniciante"
# skill2 = "java"
# level2 = "senior"
# skill3 = "c++"
# level3 = "pleno"
# baixo = 2000
# alto = 3000

# print(f"meu nome é{nome},tenho {idade} anos")
# print(f"minhas habilidades são{skill1},{level1},{skill2},{level2},{skill3},{level3}")
# print(f"procuro um emprego com um salário de {baixo} a {alto} euros por mês")


# #operadores
# ano =int(input("coloque aqui o ano de nscimento"))
# input(f"ao final do ano voce terá: {2024 - ano}")

# #exemplos
# altura = float(input("qual sua altura?"))
# peso = float(input("qual seu peso?"))

# imc = peso/(altura/100)**2

# print(f"o IMC é: {imc}")


# #estrutura cindicinal
# idade = 18
# if idade>=18:
#     print("voce é maior de idade")

# #operadors de comparação
# numero = int(input("entre com um numero:"))

# if numero < 0:
#     print("esse número é negativo")

# if numero >0:
#     print("esse numero é positivo")

# if numero ==0:
#     print("o numero é 0")


# a = 3
# condicao = a < 5 
# print(condicao)
# if condicao:
#     print("a é menor que 5")
    

# numero = int(input("por favor coloque um numero:"))

# if numero < 0:
#     print("u numero é negativo")

# else: 
#     print(" o número é possitivo e verdadeiro")
    

#
# numero = int(input("entre com um numero:"))

# if numero >= 5 and numero <= 8 :
#     print("o numero está entre 5 e 8")



#    #exemplo do or 
# numero = int(input("entre com um numero:"))

# if numero < 5 or  numero > 8 :
#     print("o numero está entre 5 e 8")


#em python
# while True :
#     codigo = input("por favor, insira o PIN:")
#     if codigo == "1234":
#         break
#     print("Errado!...tente de novo")
#     print("programa encerrado, obgd!")

# #auxiliares
# tentativas = 0
# while True :
#     codigo =  input("por favor,digite seu PIN:")
#     tentativas +=1
#     if codigo == "1234":
#         sucesso = True
#         break
#     if tentativas == 3:
#         sucesso = False
#         break
#     print("incorreto...tente novamente")
# if sucesso:
#     print("PIN correto incerido!")
# else:
#     print("muitas tentativas...")

# #LOOP COM CONDIÇÃO
# numero = int(input("Por favor, digite um numero "))

# while numero < 10 :
#     print(numero)
#     numero += 1

# print ("Execulção finalizada.")




#Bibliotecas

import re 
print (re.search("[A,Z]", "Senha"))
print (re.search("[a,z]", "Senha"))
print (re.search("[8,9]", "Senha"))


import random
numero_secreto= random.randint(1,100)

print(numero_secreto)