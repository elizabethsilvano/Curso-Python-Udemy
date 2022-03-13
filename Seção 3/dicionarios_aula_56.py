print()
print('Texto explicativo')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'resp': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3x2? ',
        'resp': {
            'a': '4',
            'b': '101',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
}
print()

resp = 0
for pergunta, dados_pergunta in perguntas.items():
    print(f'{pergunta}: {dados_pergunta["pergunta"]}')

    print('Resp: ')
    for resposta, dados_resposta in dados_pergunta['resp'].items():
        print(f'[{resposta}]: {dados_resposta}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == dados_pergunta['resposta_certa']:
        print('Você acertou!')
        resp += 1
    else:
        print('Você errou!')

    print()

quantidade_perguntas = len(perguntas)
porcentagem_acerto = resp / quantidade_perguntas * 100
print(f'Você acertou {resp} resp.')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')