#35
ponto_do_curso= input("insira seus pontos:")

if ponto_do_curso < 0:
    print("Impossivel")

elif ponto_do_curso > 0 or ponto_do_curso < 49:
    print("Falho")

elif ponto_do_curso > 50 or ponto_do_curso < 59:
    print("Sua nota é :1")

elif ponto_do_curso > 60 or ponto_do_curso < 69:
    print("Sua nota é: 2")

elif ponto_do_curso > 70 or ponto_do_curso < 79:
    print("Sua nota é : 3")

elif ponto_do_curso > 80 or ponto_do_curso < 89:
    print("Sua nota é : 4")

elif  ponto_do_curso > 90 or ponto_do_curso < 99:
    print("sua nota é : 5")

else :
    print("Impossivel")

