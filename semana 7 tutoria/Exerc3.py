def Potencia(A,B):
    X = A**B
    return X
a = int(input('Digite o valor da base: '))
b = int(input('Digite o valor do expoente: '))
x = Potencia(a,b)
print(f'A**B: {x}')
