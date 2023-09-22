from biblioteca import *

loteria = inputVetor('Loteria: ',int)
bilhete = inputVetor('Bilhete: ',int)

if len(loteria) != len(bilhete):
    acertos = []
else:
    acertos = []
    for num in bilhete:
            if num in loteria:
                acertos.append(num)
    print(f'Acertos: {acertos}')
    if len(acertos) < 6:
        print('Você não ganhou!')
    else:
        print('Você ganhou!')