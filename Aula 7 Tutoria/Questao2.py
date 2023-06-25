somam = 0
ap = 0
maior_massa = 0

for i in range(0,5):
    m = float(input(f'Digite a massa do lingote {i+1}: '))
   
    if m > 24.9:
        ap += 1
        somam = somam + m

        if m > maior_massa:
            maior_massa = m

pesom = somam/ap
print(f'Numero de lingotes aproveitados: {ap} kg') 
print(f'Peso medio dos lingotes aproveitados: {pesom:.1f} kg')
print(f'Maior peso entre os lingotes aproveitados: {maior_massa:.1f} kg')