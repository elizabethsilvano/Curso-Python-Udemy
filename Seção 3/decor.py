
from time import time
from time import sleep


def velocidade(funcao):

    def envolve(*args, **kwargs):
        start = time()
        resultado = funcao(*args, **kwargs)
        end = time()
        tempo = (end - start) * 1000
        print(f'\nA função levou {tempo:.2f}ms para ser executada.')
        return resultado
    return envolve


@velocidade
def demora(qtd):
    for i in range(qtd):
        print(i, end='')

demora(10000)
