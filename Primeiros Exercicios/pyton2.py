altura = float(input("Digite a altura: "))
sexo = str(input("Digite o sexo (m ou f): "))
if sexo == 'm':
    peso = (72.7*altura)- 58
    print(f"O peso ideal é {peso:.2f}")
else:
    peso = (62.1*altura)- 44.7
    print(f"O peso ideal é {peso:.2f}")