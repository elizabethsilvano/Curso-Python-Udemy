"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
n = input('Digite um número inteiro: ')

if not n.isdigit():
    print('Isso não é um número inteiro')
else:
    n = int(n)

    if not n % 2 == 0:
        print(f'{n} é ímpar')
    else:
        print(f'{n} é par')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
h= input('Digite um horário (0-23): ')

if h.isdigit():
    h= int(h)

    if h< 0 or h> 23:
        print("Horário deve estar entre 0 e 23")
    else:
        if h<= 11:
            print('Boa dia!')
        elif h<= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print("Por favor, digite um horário entre 0 e 23.")
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto.')
elif tamanho <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
