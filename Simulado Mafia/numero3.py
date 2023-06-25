n = int(input('Quantidade de provas: '))
cont2 = 0
pe1 = 0
pe2 = 0
cont1 = 0
emp = 0 
for i in range(0,n):
    print(f'Prova {i+1}')
    pe1 = float(input('Pontuação do primeiro participante: '))
    pe2 = float(input('Pontuação do segundo participante: '))
    if pe1 > pe2:
        cont1 += 1
    elif pe2 > pe1:
        cont2 += 1
    else:
        emp += 1
print(f'===Resultados===')
print(f'Primeiro participante: {cont1} vitórias')
print(f'Segundo participante: {cont2} vitórias')
print(f'Empates: {emp}')
if cont1 > cont2:
    print('Primeiro participante venceu')
elif cont2 > cont1:
    print('Segundo participante venceu')
else:
    print('Empate')