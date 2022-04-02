# Exercício 1

while True:
    x = int(input('Digite um número de 0 a 10: '))
    if x > 10 or x < 0: print('Número inválido')
    else: break

# Exercício 2

while True:
    n = input('Digite seu nome de usuário: ')
    s = input('Digite sua senha: ')
    if n == s: print('Nome de usuário e senha iguais! Coloque novamente.')
    else: break

# Exercício 3

a = 80000
b = 200000
x = 0
while a <= b:
    a = a + a * 0.03
    b = b + b * 0.015
    x = x + 1
print(x, 'anos')

# Exercício 4

n = int(input('Digite um número e descubra seu Fibonacci: '))
a = 1
b = 1
x = 1
while x <= n - 2:
    a, b = b, a
    b = a + b
    x = x + 1
print (b)

# Exercício 5

n1 = int(input('Descubra o MDC de dois números: '))
n2 = int(input('Descubra o MDC de dois números: '))
while n1 % n2 != 0:
    n1 = n1 % n2
    n1, n2 = n2, n1
print(n2)
    

