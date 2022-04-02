# Exercício 1

n = int(input('Número: '))
k = 1
while k * (k + 1) * (k + 2) < n:
    k = k + 1
print (k * (k + 1) * (k + 2) == n)

# Exercício 2

c = int(input('Conta: '))
p = int(input('Pagamento: '))
t = c - p
n = [50, 20, 10, 5, 2, 1]
for x in n:
    while t >= x:
        print(f'Uma nota de {x}')
        t -= x

# Exercício 3

n = int(input('Número é primo: '))
k = 1
d = 0
while k <= n:
    if n % k == 0:
        d = d + 1
    k = k + 1
print(d == 2)

# Exercício 4

n = int(input('Número: '))
for k in range(2, n):
    while n % k == 0:
        print (k)
        n = n / k

# Exercício 5

n = int(input('Número: '))
n = str(n)
print ([n::-1])

n = int(input('Número: '))
inv = 0
while n > 0:
    inv *= 10
    inv += n % 10
    n //= 10
print(inv)
