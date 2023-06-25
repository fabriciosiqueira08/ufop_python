n = int(input('Digite o numero de alunos: '))
soma = 0
for i in range(0,n):
    nome = input(f'Digite o nome do aluno {i+1}: ')
    nota1 = float(input(f'Digite a nota 1: '))
    nota2 = float(input(f'Digite a nota 2: '))
    nota3 = float(input(f'Digite a nota 3: '))
    nota1t = nota1 *2
    nota2t = nota2 *3
    nota3t = nota3 *5  
    media = (nota1t + nota2t + nota3t)/10
    print(f'A media do aluno {nome} é {media:.3f}')
    soma = soma + media
mediat = soma/n
print(f'A media da turma é {mediat:.3f}')



    