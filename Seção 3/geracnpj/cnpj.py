import re
import random

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def valida(cnpj):
    cnpj = apenas_numeros(cnpj)

    try:
        if eh_sequencia(cnpj):
            return False
    except:
        return False

    try:
        novo_cnpj = calcula_dig(cnpj=cnpj, dig=1)
        novo_cnpj = calcula_dig(cnpj=novo_cnpj, dig=2)
    except Exception as e:
        return False

    if novo_cnpj == cnpj:
        return True
    else:
        return False

def calcula_dig(cnpj, dig):
    if dig == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif dig == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo

    dig = 11 - (total % 11)
    dig = dig if dig <= 9 else 0

    return f'{novo_cnpj}{dig}'

def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False

def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def gera():
    primeiro_dig = random.randint(0, 9)
    segundo_dig = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'

    inicio_cnpj = f'{primeiro_dig}{segundo_dig}{segundo_bloco}' \
        f'{terceiro_bloco}{quarto_bloco}00'

    novo_cnpj = calcula_dig(cnpj=inicio_cnpj, dig=1)
    novo_cnpj = calcula_dig(cnpj=novo_cnpj, dig=2)

    return novo_cnpj

def formata(cnpj):
    cnpj = apenas_numeros(cnpj)
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado
