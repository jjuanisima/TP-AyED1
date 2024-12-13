'''
Una librería almacena su lista de precios en un diccionario. Diseñar un programa 
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un 
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más 
costoso que venden en el comercio.
'''


def stock_libreria(lista_precios: dict, producto: str, precio: float) -> dict:
    '''
    Agrega un producto y su precio en el stock

    Pre:
        lista_precios (dict): diccionario con los precios de los productos
        producto (str): noombre del producto a agregar
        precio (float): precio del producto
    Post:
        devuelve un diccionario con el stock actualizado
    '''

    lista_precios[producto] = precio
    return lista_precios

def incrementar_precios(lista_precios: dict) -> dict:
    '''
    Incrementa el precio de los productos que contienen 'cuaderno' en un 15%

    Pre:
        lista_precios (dict): diccionario con los precios de los productos
    Post:
        devuelve un diccionario actualizado con los precios incrementados
    '''

    for producto in lista_precios:
        if 'cuaderno' in producto.lower():
            lista_precios[producto] = lista_precios[producto] + (lista_precios[producto] * 0.15)
    return lista_precios

def mas_costoso(lista_precios: dict) -> tuple:
    '''
    Encuentra el producto más caro del stock

    Pre:
        lista_precios (dict): diccionario con los precios de los productos
    Post:
        devuelve una tupla con el nombre del producto más costoso y su precio
    '''

    if lista_precios:
        valor_max = max(lista_precios, key=lista_precios.get)
        return valor_max, lista_precios[valor_max]
    return None, None

if __name__ == "__main__":
    lista_precios = {}
        
    while True:
        producto = input("\nNombre del producto ('S' para salir): ")

        if producto.upper() == 'S':
            print("Carga de productos finalizada :)")
            break

        if producto not in lista_precios:
            try:
                precio = float(input("Precio del producto: "))
                stock_libreria(lista_precios, producto, precio)
            except ValueError:
                print("ERROR. Revisa de ingresar un precio válido :|")
        else:
            print("El producto ya existe en el almacén :|")

    incrementar_precios(lista_precios)
    print("Stock actual:")
    for producto, precio in lista_precios.items():
        if 'cuaderno' in producto:
            print(f"- {producto}: ${precio:.2f} (+15%)")
        else:
            print(f"- {producto}: ${precio:.2f}")

    producto, precio = mas_costoso(lista_precios)
    print(f"\nProducto más costoso: '{producto}' - ${precio}")