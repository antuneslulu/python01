pontosnocartao = float(input("digite a quantidade de pessoas:"))
if pontosnocartao< 100:
    taxadebonus= 0.12
if pontosnocartao > 100:
    taxadebonus= 0.16
bonus = pontosnocartao * taxadebonus
print(f"o bonus é de :{bonus} pontos")