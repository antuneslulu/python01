tentativas = 0
while True :
    codigo =  input("por favor,digite seu PIN:")
    tentativas +=1
    if codigo == "4321":
        sucesso = True
        break
    if tentativas == 2:
        sucesso = False
        break
    print("incorreto...tente novamente")
if sucesso:
    print("PIN correto incerido!")
else:
    print("muitas tentativas...")