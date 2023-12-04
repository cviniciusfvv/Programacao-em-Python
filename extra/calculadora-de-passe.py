import math

while True:
    op = int(input("Qual opção você quer: 1 - saldo viagem, 2 - viagem saldo, 0 - sair: "))

    if op == 0:
        print("Saindo do programa. Até mais!")
        break  # Encerra o loop
    if op == 1:  # saldo viagem
        while True:
            tipop = int(input("Digite 1 para passe comum, 2 para passe estudante médio/técnico, 3 passe estudante universitario, 0 - sair: "))
            
            if tipop == 0:
                print("Saindo do programa. Até mais!")
                break  # Encerra o loop interno
            valorp = float(input("Digite o valor do passe que tem R$: "))
            if tipop == 1:  # passe comum
                qp1 = valorp / 5.45
                qp2 = valorp / 5.90
                print(f"Passe comum: caso você pegue 2 ônibus, você tem {math.floor(qp1)} passe(s); caso você pegue 3 ônibus, você tem {math.floor(qp2)} passe(s)")
                print(f"Total de passe R$: {valorp:.2f}")
            elif tipop == 2:  # passe estudante médio/técnico
                qp3 = valorp / 2.18
                print(f"Passe estudante: você tem {math.floor(qp3)} passe(s) de estudante médio/técnico, pois você paga 40% do passe")
                print(f"Total de passe R$: {valorp:.2f}")
            elif tipop == 3:  # passe estudante universitário
                qp4 = valorp / 2.73
                print(f"Passe estudante: você tem {math.floor(qp4)} passe(s) de estudante universitario, pois você paga 50% do passe")
                print(f"Total de passe R$: {valorp:.2f}")
            else:
                print("Opção não existe")
    elif op == 2:
        while True:
            tipop = int(input("Digite 1 para passe comum, 2 para passe estudante médio/técnico, 3 passe estudante universitario, 0 - sair: "))

            if tipop == 0:
                print("Saindo do programa. Até mais!")
                break  # Encerra o loop interno
            quant = int(input("Quantas viagens quer fazer: "))
            if tipop == 1:
                qp1 = quant * 5.45
                qp2 = quant * 5.90
                print(f"Passe comum: caso você pegue 2 ônibus, você tem R$: {qp1:.2f}; caso você pegue 3 ônibus, você tem R$: {qp2:.2f}")
                print(f"Total de viagens: {quant}")
            elif tipop == 2:
                qp3 = quant * 2.18
                print(f"Total de viagens: {quant}")
                print(f"Total de passe R$: {qp3:.2f}")
            elif tipop == 3:  # passe estudante universitário
                qp4 = quant * 2.73
                print(f"Total de viagens: {quant}")
                print(f"Total de passe R$: {qp4:.2f}")
            else:
                print("Opção não existe")
    else:
        print("Opção não existe")