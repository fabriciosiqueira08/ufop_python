media = float(input('Forneça a média no semestre: '))
freq = float(input('Forneça a frequência no semestre: '))
if media >= 6 and freq >= 75:
    print('Conceito: aprovado')
elif media <= 6 and freq >= 75:
    print('Conceito: exame especial')
    just = 6 - media
    print(f'Justificativa: média {just:.2f} abaixo da mínima')
elif media >= 6 and freq <= 75:
    print('Conceito: reprovado por faltas')
    just1 = 75 - freq
    print(f'Justificativa: frequência {just1:.0f}% abaixo da mínima')
elif media < 6 and freq < 75:
    print('Conceito: reprovado por faltas')
    just2 = 75 - freq
    print(f'Justificativa: frequência {just2:.0f}% abaixo da mínima')