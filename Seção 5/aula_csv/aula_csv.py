"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv

with open('/home/elizabeths/Documentos/Cursos Itflex/Curso_Python/Seção 5/aula_csv/clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]

with open('/home/elizabeths/Documentos/Cursos Itflex/Curso_Python/Seção 5/aula_csv/clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )