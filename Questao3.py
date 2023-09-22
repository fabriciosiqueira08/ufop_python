from biblioteca import * 

def calculaLucros(coxinhas, quibes, lucroc, lucroq):
        lucros = []
        for i in range (len(coxinhas)):
            lucros.append(coxinhas[i] * lucroc + quibes[i] * lucroq)
        return lucros

coxinhas = inputVetor('Informe as vendas de coxinhas: ', int)
quibes = inputVetor('Informe as vendas de quibes: ', int)

if len(coxinhas) != len(quibes) or len(quibes) != len(coxinhas):
    print('Dados de vendas inválidos')
else:
    lucroc = float(input('Informe o lucro por unidade de coxinha: R$ '))
    lucroq = float(input('Informe o lucro por unidade de quibe: R$ '))
    lucros = calculaLucros(coxinhas, quibes, lucroc, lucroq)

    rounded_lucros = [round(l, 2) for l in lucros]
    print(f'Lucros: {rounded_lucros}')
    
    maiorlucro = max(lucros)
    menorlucro = min(lucros)
    print(f'Maior lucro: R$ {maiorlucro:.2f}')
    print(f'Menor lucro: R$ {menorlucro:.2f}')