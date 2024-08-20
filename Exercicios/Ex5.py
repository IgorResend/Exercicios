while True:
        try:
            nota = float(input("Insira a nota: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
            continue
        if nota < 0 or nota > 20:
            print("Insira um número válido entre 0 e 20.")
        elif nota >= 10:
            print("Validada")
            break  
        else:
            print("Não validada")
            break
