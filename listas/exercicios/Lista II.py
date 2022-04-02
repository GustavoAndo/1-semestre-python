# Exercício 1

a = float(input('Lado 1 do triângulo: '))
b = float(input('Lado 2 do triângulo: '))
c = float(input('Lado 3 do triângulo: '))
if a > b + c or b > a + c or c > a + b:
    print('Isso não pode ser um triângulo!')
else:
    print('Isso pode ser triângulo!')
    if a == b == c:
        print('Além disso, ele é um triângulo equilátero!')
    elif a == b or b == c or c == a:
        print('Além disso, ele é um triângulo isóceles!')
    else:
        print('Além disso, também é um triângulo escaleno!')

# Exercício 2

a = int(input('Digite um ano: '))
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print (f'{a} é um ano bissexto!')
else:
    print (f'{a} não é um ano bissexto!')

# Exercício 3

p = int(input('Digite o peso em quilos: '))
if p > 50:
    excesso = peso - 50
    multa = excesso * 40
else:
    multa = excesso = 0
    print (f'Multa de {multa:.2f} reais')
    print (f'Excesso de {excesso:.2f')
    
# Exercício 4

a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))
if a >= b and a >= c:
    maior = a
elif b >= c:
    maior = b
else:
    maior = c
print(maior, 'é o maior')

a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))
print(f'{max(a,b,c)} é o maior')

# Exercício 5

a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))
if a <= b and a <= c:
    menor = a
elif b <= c:
    menor = b
if c <= b and c <= a:
    menor = c
print(menor, 'é o menor')

a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))
print(f'{min(a,b,c)} é menor')

# Exercício 6

g = float(input('Ganho por hora: '))
h = float(input('Horas trabalhadas no mês: '))
sb = g * h
ir = sb * 11/100
inss = sb * 8/100
s = sb * 5/100
sl = sb - ir - inss - s
print(f'Salário Bruto: {sb:.2f} reais')
print(f'IR: {ir:.2f}')
print(f'INSS: {inss:.2f}')
print(f'Sindicato: {s:.2f}')
print(f'Salário Líquido: {sl:.2f}')

# Exercício 7

m = float(input('Área que quer pintar em metros quadrados: '))
if m % 54 == 0:
    latas = m/54
else:
    latas = int(m/54) + 1
print(f'Será utilizado {latas}')
print(f'E você terá que pegar {latas*80}')
    
          
