'''
Utilizar la técnica de listas por comprensión para construir una lista con todos los 
números impares comprendidos entre 100 y 200.
'''


impares = [i for i in range(100, 201) if i % 2 != 0]
'''
impares = []
for i in range(100, 201):
    if i % 2 != 0:
        impares.append(i)
    return impares
'''

def main():
    '''
    Función principal, donde se ejecuta el programa
    '''
    print(impares)
    return None

main()