# Exercício 1

import random
x = random.sample(range(1,100),10)
maior = 0
menor = 100
for k in x:
    if k > maior:
        maior = k
    if k < menor:
        menor = k
print ('Da lista de números',x)
print ('O maior é o', maior)
print ('E o menor é o', menor)

# Exercício 2

import random
x = random.sample(range(1,100),20)
par = []
impar = []
for k in x:
    if k % 2 == 0:
        par.append(k)
    else:
        impar.append(k)
print ('Da lista de números',x)
print ('Os pares são', par)
print ('E os ímpares são', impar)

# Exercício 3

import random
x = random.sample(range(1,100),10)
y = random.sample(range(1,100),10)
z =[]
k = 0
while k < 10:
    z.append(x[k])
    z.append(y[k])
    k = k + 1
print ('Lista 1: ', x)
print ('Lista 2: ', y)
print ('Lista 3: ', z)

# Execício 4

texto = '''The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you.'''.lower()
texto = texto.replace(',','')
texto = texto.replace('.','')
texto = texto.replace('\n','')
texto = texto.split(' ')
resp = []
for palavra in texto:
    if palavra[0] in 'python' or palavra[-1] in 'python':
        resp.append(palavra)
print(resp)

# Exercício 5

texto = '''The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you.'''.lower()
texto = texto.replace(',','')
texto = texto.replace('.','')
texto = texto.replace('\n','')
texto = texto.split(' ')
resp = []
def tamanho(x):
    if len(x) > 4:
        return True
    return False
def python (x):
    for letra in x:
        if letra in 'python':
            return True
    return False
for palavra in texto:
    if python(palavra) and tamanho(palavra):
        resp.append(palavra)   
print(len(resp), 'palavras:', resp)

