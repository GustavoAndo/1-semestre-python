#Gustavo Kenji Ando

def escolhe():
    return choice(palavras)

def desenha():
    print(forca[len(erradas)])
    for x in sorteada:
        if x in certas: print(x, end = ' ')
        else: print('_', end = ' ')       
    print('')
    
def ganhou():
    if set(certas) == set(sorteada):
        return True

def chute(x):
    while True:
        letra = input('Chute uma letra: ')
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        if letra in x:
            print('Essa letra já foi usada! Coloque novamente!')
        elif letra not in alfabeto or len(letra)!= 1:
            print('Digito incorreto! Coloque apenas uma letra sem acento e em minúsculo!')
        else:
            return letra

def jogar_novamente():
    x = input('Deseja jogar novamente?(Sim/Nao) ')
    return x
    
while True:
    forca = [ '''
    +------+
           |
           |
           |
           |
           |
 +=========+
    ''',
    '''
    +------+
    |      |
           |
           |
           |
           |
 +=========+
    ''',
    '''
    +------+
    |      |
    O      |
           |
           |
           |
 +=========+
    ''',
    '''
    +------+
    |      |
    O      |
    |      |
           |
           |
 +=========+
    ''',
    '''
    +------+
    |      |
    O      |
   /|      |
           |
           |
 +=========+
    ''',
    '''
    +------+
    |      |
    O      |
   /|\     |
           |
           |
 +=========+
    ''',
    '''
    +------+
    |      |
    O      |
   /|\     |
   /       |
           |
 +=========+
    ''',
    '''
    +------+
    |      |
    O      |
   /|\     |
   / \     |
           |
 +=========+''']
    certas = ''
    erradas = ''
    url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
    import requests
    palavras = requests.get(url).text.split()
    from random import choice
    sorteada = escolhe()    
    while True:
        desenha()
        if ganhou():
            print(f'Parabéns! A palavra correta era "{sorteada}"!')
            print('Você acertou e venceu no Jogo da Forca!')
            break
        if len(erradas) == 7:
            print('Forca! Infelizmente você perdeu no Jogo da Forca...')
            print(f'A palavra correta era "{sorteada}"')
            break
        letra = chute(certas+erradas)
        print()
        if letra in sorteada:
            certas = certas + letra
            print(f'A letra "{letra}" está correta!')
        else:
            erradas = erradas + letra
            print(f'A letra "{letra}" está errada!')
    while True:
        resposta = jogar_novamente()
        if resposta.lower() == 'sim' or resposta.lower() == 'nao': break
        else: print('Resposta inválida! Coloque "sim" ou "nao" (Sem acento).')
    if resposta.lower() == 'sim':
        print('Reiniciando o Jogo da Forca...')
        continue
    if resposta.lower() == 'nao':
        print('Saindo do Jogo da Forca...')
        break
    
