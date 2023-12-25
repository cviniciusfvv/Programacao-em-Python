import math

while True:
    print("Lojas Tabajara")
    num_produtos = int(input("Quantos produtos você comprou? "))
    total_compra = 0
    desconto = 0

    for produto_numero in range(1, num_produtos + 1):
        preco_produto = float(input(f"Produto {produto_numero}: R$ "))
        print(f"produto {produto_numero} custou R${preco_produto:.2f}")
        total_compra += preco_produto

    if total_compra >= 100 and total_compra < 150:
        desconto = total_compra * 0.10
    elif total_compra >= 150:
        desconto = total_compra * 0.15
    elif total_compra >= 200:
        desconto = total_compra * 0.20

    total_compra_com_desconto = total_compra - desconto

    print(f"Total: R$ {total_compra:.2f}")
    dinheiro_cliente = float(input("Dinheiro: R$ "))
    print(f"Cliente deu R$: {dinheiro_cliente:.2f}")
    print(f"desconto total R$: {desconto:.2f}")
    print(f"Total com desconto R$: {total_compra_com_desconto:.2f}")

    if dinheiro_cliente >= total_compra_com_desconto:
        troco = dinheiro_cliente - total_compra_com_desconto
        print(f"Troco: R$ {troco:.2f}\n")
    else:
        print("po marreco, ve isso direito!!!!") 

    continuar = input("Deseja registrar outra compra? (S para sim, qualquer outra tecla para não): ").upper()
    if continuar != 'S':
        print("Té mais marreco")
        break
