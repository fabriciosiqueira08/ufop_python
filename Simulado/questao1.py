def armstrong(num):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if num==sum:
        print(num,"is an armstrong number")
    else:
        print(num,"is not an armstrong number")

num = int(input('Digite um número: '))
while num <= 0:
    print('Número inválido')
    num = int(input('Digite um número: '))
aux = armstrong(num)
