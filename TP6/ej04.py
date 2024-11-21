'''
Desarrollar un programa para eliminar todos los comentarios de un programa  es
crito en lenguaje Python. Tener en cuenta que los comentarios comienzan con el 
signo # (siempre que éste no se encuentre encerrado entre comillas simples o do
bles) y que también se considera comentario a las cadenas de documentación 
(docstrings).
'''


import re

def eliminar_comentarios() -> None:
    '''
    Elimina comentarios y docstrings del archivo 'archivoconcomentarios.py'

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    with open('TP6/archivoconcomentarios.py', 'r', encoding='utf-8') as archivo:
        codigo = archivo.read()

        codigo_sin_comentarios = re.sub("(?m)\s*#.*$", "", codigo)

        codigo_sin_docstrings = re.sub("(?s)(\'\'\'(.*?)\'\'\'|\"\"\"(.*?)\"\"\")", "", codigo_sin_comentarios)

        with open('TP6/archivoconcomentarios.py', 'w', encoding='utf-8') as archivo:
            archivo.write(codigo_sin_docstrings.strip())

if __name__ == "__main__":
    eliminar_comentarios()