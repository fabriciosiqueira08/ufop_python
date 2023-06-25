lote = int(input('Tipo de lote (1 ou 2): '))
if lote > 2:
    print('ERRO: Tipo de lote inválido.')
if lote == 1:
    area = float(input('Área do imovel (m²): '))
    if 0 < area < 200:
        iptu = area * 1.0
        print(f'O valor do IPTU é: R$ {iptu:.2f}')
    if area >= 200:
        iptu = area * 1.2
        print(f'O valor do IPTU é: R$ {iptu:.2f}')
if lote == 2:
    area = float(input('Área do imovel (m²): '))
    if 0 < area < 200:
        iptu = area * 1.1
        print(f'O valor do IPTU é: R$ {iptu:.2f}')
    if area >= 200:
        iptu = area * 1.3
        print(f'O valor do IPTU é: R$ {iptu:.2f}')
print('Fim do programa')

    
