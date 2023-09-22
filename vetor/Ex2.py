from biblioteca import *

def getDivisores(n):
        divisores = []
        for i in range(1, n+1):
            if n%i == 0:
                divisores.append(i)
            print(divisores)
        return divisores

n = inputVetor('Digite os números: ', int)

if n == []:
    print('Nenhum número informado')
elif n/1 and n/n:
    print(f'{n} é um número primo')
else:
    divisores = getDivisores(n)