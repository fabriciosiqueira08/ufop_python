ct = float(input('Forneça o capital Total para empréstimo: '))
t = 0 

while True:

    c = float(input('Forneça o capital emprestado: '))

    if c > ct:
        print(f'Empréstimo negado, capital total é de R$ {ct:.2f}.')
        break

    if c <= 10000:
        t = 0.10    
    else:
        t = 0.07
    
    if c < 10000:
        m = int(input('Forneça a quantidade de meses para quitação: '))
        print(f'Taxa de juros aplicada: {t*100:.0f}%.')
        J = c*t*m   
        total = J + c
        print(f'Juros devido: {J:.2f}.')
        print(f'Valor total: {total:.2f}.')
        ct -= c
    if c > 10000:
        m = int(input('Forneça a quantidade de meses para quitação: '))
        print(f'Taxa de juros aplicada: {t*100:.0f}%.')
        J = c*t*m
        total = J + c
        print(f'Juros devido: {J:.2f}.')
        print(f'Valor total: {total:.2f}.')
        ct -= c

    