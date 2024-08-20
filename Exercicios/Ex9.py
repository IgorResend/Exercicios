quantia = int(input("Quantas fotocópias quer: "))
 
if quantia <= 10:
        valor = quantia * 0.25
        print("O valor ficou: R$ " + str(round(valor, 2)))
elif quantia <= 20:
        valor = quantia * 0.20
        print("O valor ficou: R$ " + str(round(valor, 2)))
else:
        valor = quantia * 0.10
        print("O valor ficou: R$ " + str(round(valor, 2)))