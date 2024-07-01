salario = float(input("DIGITE O VALOR DA HORA :"))
quantodehora= float(input("digite a quantidade de horas:"))
dia = input("digite o dia da semana:")
salario = salario * quantodehora
if dia =="domingo":
    print(salario * 2)