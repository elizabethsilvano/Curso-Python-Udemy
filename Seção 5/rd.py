import random
import string

inteiro = random.randrange(900, 1000, 10)
flutuante = random.random()
lista = ['Elizabeth', 'Eliza', 'Alex', 'Erica', 'Luiza', 'John', 'Felipe']
sorteio = random.sample(lista, 2)
random.shuffle(lista)
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)
