while True:
    valor = float(input("Digite o valor da parcela do leilão: "))
    parcelas = int(input("Digite a quantidade de parcelas: "))
    quantidade = int(input("Quantidade de cabeças: "))
    
    resultado = (valor * parcelas) * quantidade

    print(f"Valor da parcela: {valor:.2f} ")
    print("Quantidade de parcelas: ", parcelas)
    print("Quantidade de cabeças:", quantidade)
    print(f"Valor total: {resultado:.2f}")

    continuar = input("Deseja continuar? (S para sim, qualquer outra tecla para não): ").upper()
    
    if continuar != 'S':
        print("Até mais, marreco")
        break
