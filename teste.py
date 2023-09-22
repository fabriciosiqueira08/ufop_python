from biblioteca import * 

coxinhas = inputVetor('Informe as vendas de coxinhas: ', int)
quibes = inputVetor('Informe as vendas de quibes: ', int)

if len(coxinhas) != len(quibes):
    print('Dados de vendas inválidos')
else:
    lucroc = inputVetor('Informe o lucro por unidade de coxinha: R$ ', float)
    lucroq = inputVetor('Informe o lucro por unidade de quibe: R$ ', float)
    
    if len(coxinhas) != len(lucroc) or len(quibes) != len(lucroq):
        print('Dados de lucro inválidos')
    else:
        def calculaLucros(coxinhas, quibes, lucroc, lucroq):
            lucros = []
            for i in range(len(coxinhas)):
                lucros.append(coxinhas[i] * lucroc[i] + quibes[i] * lucroq[i])
            return lucros

        print(f'Lucros: {calculaLucros(coxinhas, quibes, lucroc, lucroq)}')
