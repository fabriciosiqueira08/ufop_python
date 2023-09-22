
def Custo (v,t,r,p):
    C = (v*t/r)*p
    return C

print('Custo do combustivel em uma viagem')
vm = float(input('Velocidade media(km/h): '))
tp = float(input('Tempo previsto(h): '))
rg = float(input('Rendimento com gasolina(km/l): '))
pg = float(input('Preço da gasolina(R$/l): '))
pa = float(input('Preço do alcool(R$/l): '))
cg = Custo(vm,tp,rg,pg)
rga = rg*0.7
ca = Custo(vm,tp,rga,pa)
print(f'Custo com gasolina: R$ {cg:.2f}')
print(f'Custo com alcool: R$ {ca:.2f}')