# Exercício 1

n1 = int(input('Primeiro número da soma: '))
n2 = int(input('Segundo número da soma: '))
print(n1 + n2)

# Exercício 2

n = float(input('Número em m para converter em mm: '))
print(f'{n * 1000:.1f} mm')

# Exercício 3

d = int(input('Dias: '))
h = int(input('Horas: '))
m = int(input('Minutos: '))
s = int(input('Segundos: '))
print(f'{d*24*60*60+h*60*60+m*60+s} segundos')

# Exercício 4

v = float(input('Valor do salário: '))
p = float(input('Porcentagem de aumento: '))
print(f'{v+v*p/100:.2f} reais')

# Exercício 5

m = float(input('Preço da mercadoria: '))
p = float(input('Porcentagem de desconto: '))
print(f'Desconto: {m*p/100:.2f} reais')
print(f'Preço a pagar: {m-m*p/100:.2f} reais')

# Exercício 6

v = float(input('Velocidade média do carro: '))
s = float(input('Espaço percorrido: '))
print(f'{s/v:.1f}')

# Exercício 7

c = float(input('Temperatura em graus Celsius: '))
print(9*c/5 + 32, 'ºF')

# Exercício 8

f = float(input('Temperatura em graus Fahrenheit: '))
print((f-32)*5/9,'ºC')

# Exercício 9

s = int(input('Km percorridos com o carro: '))
d = int(input('Dias com o carro alugado: '))
print (f'{60*d + 0.15*s:.2f} reais')

# Exercício 10

c = int(input('Cigarros fumados por dia: '))
a = int(input('Anos fumando: '))
print(f'{c*365*a*10/1440:.0f} dias')

# Exercício 11

print(len(str(2**1000000)))

