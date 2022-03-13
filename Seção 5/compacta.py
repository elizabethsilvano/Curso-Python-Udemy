from zipfile import ZipFile
import os

# Para caminhos com barra invertida (\), utilize r
caminho = r'/home/elizabeths/Documentos/Cursos Itflex/Curso_Python/Seção 5/'

# ESCREVE
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)

with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')
