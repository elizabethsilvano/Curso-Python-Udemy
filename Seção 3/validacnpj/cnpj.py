import re

REGRES = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = apenas_n(cnpj)
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
        regres = REGRES[1:]
        novo_cnpj = cnpj[:-2]
    elif dig == 2:
        regres = REGRES
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, regressivo in enumerate(regres):
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


def apenas_n(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)
