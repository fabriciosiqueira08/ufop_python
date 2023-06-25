nome1= input('Forneça o nome do candidato 1: ')
n1= int(input('Forneça o número do candidato 1: '))
nome2 = input('Forneça o nome do candidato 2: ')
n2 = int(input('Forneça o número do candidato 2: '))
qtd = int(input('Forneça a quantidade de eleitores: '))

vt= 0
vi = 0
soma1 = 0
soma2 = 0
while qtd < 3:
    print ('A quantidade de eleitores é inferior a 3')
    qtd = int(input('Forneça a quantidade de eleitores: '))

print('')
print('## Votação Iniciada')

for i in range (1,qtd + 1):
    vt = int(input('Forneça o número do candidato que deseja votar: '))
    if vt != n1 and vt != n2:
        vi = vi + 1
    if vt == n1:
        soma1 = soma1 + 1
    if vt == n2:
        soma2 = soma2 + 1

total = vi + soma1 + soma2
vv = soma1 + soma2

print('## Votação Encerrada')
print('')
print(f'Votos válidos: {vv*100/total:.2f}% ({vv} votos)')
print(f'Votos inválidos: {vi*100/total:.2f}% ({vi} votos)')
if vv == 0:
    vv = 1
print(f'Votos para {nome1}: {soma1*100/vv:.2f}% ({soma1} votos)')
print(f'Votos para {nome2}: {soma2*100/vv:.2f}% ({soma2} votos)')
        