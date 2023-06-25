P = float(input('Digite a pressão em atm: '))
n = float(input('Digite a qtd de mols: '))
R = 0.082
C = float(input('Digite a temperatura em Celsius: '))
T = C + 273.15
V = (n*R*T)/P
print(f'{n:} mols de um gás a {C} graus celcius e a {P} atm, ocupam {V:.4f} litros')
