'''
En geometría un vector es un segmento de recta orientado que va desde un punto 
A hasta un punto B. Los vectores en el plano se representan mediante un par orde
nado de números reales (x, y) llamados componentes. Para representarlos basta 
con unir el origen de coordenadas con el punto indicado en sus componentes:

Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determi
narlo basta calcular su producto escalar y verificar si es igual a 0. Ejemplo:
     A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales

Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor 
de verdad indicando si son ortogonales o no. Desarrollar también un programa que 
permita verificar el comportamiento de la función.
'''


def son_ortogonales(vectora: tuple, vectorb: tuple) -> bool:
    '''
    Determina si dos vectores son ortogonales, calculando su producto escalar

    Pre:
        vectora, vectorb(tuple): dos tuplas de números que representas el primer y el segundo vector
    Post:
        devuelve True si el producto escalar de los vectores es cero (son ortogonales), False en caso contrario
    '''

    return sum(a * b for a, b in zip(vectora, vectorb)) == 0

if __name__ == "__main__":
    vectora = (3, 4)
    vectorb = (-4, 3)

    print(f"Los vectores {vectora} y {vectorb} son ortogonales :)") if son_ortogonales(vectora, vectorb) else print(f"Los vectores {vectora} y {vectorb} no son ortogonales :(")