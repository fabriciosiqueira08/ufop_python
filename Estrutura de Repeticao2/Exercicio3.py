morango = (float(input("Digite a quantidade de Morangos (em kg): ")))
maca = (float(input("Digite a quantidade de Maçãs (em kg): ")))

if morango < 0 or maca < 0:
    print("Entrada inválida")
else:
    if morango <= 5 and maca > 0:
        valor_morango = morango * 2.5
    elif morango > 5 and maca > 0:
        valor_morango = morango * 2.2

    if maca <= 5 and morango > 0:
        valor_maca = maca * 1.8
    elif maca > 5 and morango > 0:
        valor_maca = maca * 1.5

    valor_total = valor_morango + valor_maca
    print(f"O valor total da sua compra é R${valor_total:.2f}")