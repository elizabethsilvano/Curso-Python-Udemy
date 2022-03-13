from typing import List, Union, Tuple, Dict, NewType, Callable, Sequence, \
    Iterable

numero: int = 10
flutuante: float = 10.5
booleano: bool = False
string: str = 'Elizabeth Silvano'

lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Elizabeth']
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Elizabeth')

MeuDict = Dict[str, Union[str, int, List[int]]]  # Alias

pessoa: Dict[str, Union[str, int]] = {
    'nome': 'Elizabeth Silvano', 'sobrenome': 'Miranda', 'idade': 30}
pessoa2: MeuDict = {'nome': 'Elizabeth Silvano',
                    'sobrenome': 'Miranda', 'idade': 30, 'l': [1, 2]}

UserId = NewType('UserId', int)
user_id = UserId(325456789)


def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao


def soma(x: int, y: int) -> int:
    return x + y

print(retorna_funcao(soma)(10, 20))


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')


def iterar(sequencia: Sequence[int]):
    return [x for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x for x in sequencia]


print(iterar([1, 2, 3]))
print(iterar((1, 2, 3)))
print(iterar2([1, 2, 3]))
print(iterar2((1, 2, 3)))