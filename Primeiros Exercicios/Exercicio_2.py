import math
s1 = float(input('Digite o lado 1 do triangulo (m): '))
s2 = float(input('Digite o lado 2 do triangulo(m): '))
s3 = float(input('Digite o lado 3 do triangulo (m):'))
p = s1 + s2 + s3
s = p/2
area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(f'Perimetro do triangulo = {p} ')
print(f'Area do triangulo = {area:.4f} m^2')