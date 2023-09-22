from biblioteca import *

def getDivisores(n):
    vetorn = []
    for i in range (1,n+1):
        if n%i == 0:
            vetorn.append(i)
    return vetorn

n = inputVetor('Digite os numeros: ' , int)

if len(n) == 0:
     print('Nenhum número informado')
else:
    for j in range (len(n)):
        aux = getDivisores(n[j])
        if len(aux) == 2:
            print(f'{n[j]} é um número primo.')
        else:
            print(f'{n[j]} não é um número primo.')
            print('Seus divisores são')
            print(f'{aux}')