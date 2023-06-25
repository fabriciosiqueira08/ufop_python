peso1 = float(input('Digite seu peso (em kg): '))
altura = float(input('Digite sua altura (em metros): '))
sexo = str(input('Seu sexo é masculino (M) ou feminino (F)? '))
imc = peso1 / (altura ** 2)

if sexo == 'M' and imc > 25:
    peso2 = 25 * altura ** 2
    perder = peso1 - peso2
    print(f'Você deve perder {perder:.2f}kg para ter IMC = 25')

if sexo == 'M' and imc <= 25:
    print('Você não precisa perder peso para ter IMC <= 25')

if sexo == 'F' and imc > 24:
    peso2 = 24 * altura ** 2
    perder = peso1 - peso2
    print(f'Você deve perder {perder:.2f}kg para ter IMC = 24')

if sexo == 'F' and imc <= 24:
    print('Você não precisa perder peso para ter IMC <= 24')

if sexo != 'M' and sexo != 'F':
    print('A entrada contém dados não reconhecidos')
