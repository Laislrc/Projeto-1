nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if not nome and not idade:
    print('Desculpe, voce deixou campos vazios.')

else:
    print(f'O seu nome é {nome}')

    nome_invertido = (nome[::-1])
    print('O seu nome invertido é ', nome_invertido)

    if ' ' in nome:
            print('Seu nome contem espacos')
    else:
            print('Seu nome NAO contem espacos')

    n_letras = len(nome)
    print('Seu nome tem ', n_letras, 'letras')

    letra = (nome[0])
    print('A primeira letra do seu nome é ', letra)

    letra = (nome[-1])
    print('A ultima letra do seu nome é ', letra)