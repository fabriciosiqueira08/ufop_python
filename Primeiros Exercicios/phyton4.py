nome = str(input('Entre com o nome: '))
idade = float(input('Entre com a idade: '))
sexo = str(input('Entre com o sexo (m ou f): '))
anosm = 18 - idade
anosf = 21 - idade
if sexo == 'm' and idade < 18:
      print(f'Faltam {anosm:.1f} anos para {nome} atingir a maioridade') 
elif sexo == 'f' and idade < 21:
    print(f'Faltam {anosf:.1f} anos para {nome} atingir a maioridade')
elif sexo == 'm' and idade >= 18:
    print(f'{nome} tem maioridade civil')
elif sexo == 'f' and idade >= 21:
    print(f'{nome} tem maioridade civil')
    