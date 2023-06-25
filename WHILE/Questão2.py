numero = int(input('Informe o número que deseja calcular o Fatorial: '))
while numero < 0:
    numero = float(input('Número inválido, defina outro: '))
while numero == 0:
    numero = float(input('Número inválido, defina outro: '))

fatorial = 1
i = 1

while i <= numero:
    fatorial = fatorial * i
    i = i + 1

print(f'O fatorial de {numero:.0f} é: {fatorial}')