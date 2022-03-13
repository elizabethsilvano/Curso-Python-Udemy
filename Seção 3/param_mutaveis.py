
def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes_1 = ['Fabrício']
clientes1 = lista_de_clientes(['Maria', 'Eliza', 'Banana'], lista_clientes_1)
clientes2 = lista_de_clientes(['José', 'Luiz', 'Vacão'])
clientes3 = lista_de_clientes(['Pepino'])

print(clientes1)
print(clientes2)
print(clientes3)
