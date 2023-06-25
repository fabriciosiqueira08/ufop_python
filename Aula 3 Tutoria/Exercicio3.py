angulo1 = float(input("Digite o primeiro ângulo interno: "))
angulo2 = float(input("Digite o segundo ângulo interno: "))
angulo3 = float(input("Digite o terceiro ângulo interno: "))

if angulo1 == 90 or angulo2 == 90 and angulo3 == 90:
    print("O triângulo é retângulo.")
elif angulo1 > 90 and angulo2 < 90 and angulo3 < 90:
    print("O triângulo é obtusângulo.")
elif angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
    print("O triângulo é acutângulo.")
else: 
    print("TRIANGULO INEXISTENTE")