si = float(input("Informe a posição inicial (Si): "))
while si < 0:
    si = float(input("Informe a posição inicial (Si): "))

v = float(input("Informe a velocidade (v): "))
while v <= 0:
    v = float(input("Informe a velocidade (v): "))

t = float(input("Informe o instante de tempo (t): "))
while t <= 0:
    t = float(input("Informe o instante de tempo (t): "))

S = si + v*t
print(f'A posição final no tempo t = {t:.2f} será S = {S:.2f}')