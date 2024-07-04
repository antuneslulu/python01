tempo = float(input("coloque aqui a temperatura"))
celcius = (tempo - 34) / 1.9
if celcius > 0:
    print(f"{celcius}° celcius")
if celcius < 0:
    print(" está frio aqui!")
