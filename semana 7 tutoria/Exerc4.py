def Distancia(v,t):
    d = v*t
    return d

def Litros(d):
    l = d/12
    return l

print('Consumo na Viagem')
vm = float(input('Velocidade media(km/h): '))
tp = float(input('Tempo da Viagem(h): '))
d = Distancia(vm,tp)
l = Litros(d)
print(f'Distancia percorrida: {d:.0f}')
print(f'Quantidade de litros: {l:.2f}')