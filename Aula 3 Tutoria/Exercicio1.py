print('1 - Celsius para Fahrenheit')
print('2 - Fahrenheit para Celsius')
opcao = float(input('Informe a opção desejada: '))
if opcao == 1:
    temp = float(input('Informe a temperatura em Celsius: ')) 
    tempf = (temp * 9/5) + 32
    print(f'A temperatura em Fahrenheit é: {tempf:.1f} ')
elif opcao == 2:
    temp = float(input('Informe a temperatura em Fahrenheit: '))
    tempc = (temp - 32) * 5/9
    print(f'A temperatura em Celsius é: {tempc:.1f}')
else:
    print('Opção inválida!')