'''
Escribir funciones lambda para:
    a. Informar si un número es oblongo. Se dice que un número es oblongo cuando 
se puede obtener multiplicando dos números naturales consecutivos. Por ejem
plo 6 es oblongo porque resulta de multiplicar 2 * 3.
    
    b. Informar si un número es triangular. Un número se define como triangular si 
puede expresarse como la suma de un grupo de números naturales consecuti
vos comenzando desde 1. Por ejemplo 10 es un número triangular porque se 
obtiene sumando 1+2+3+4.

Ambas funciones lambda reciben como único parámetro el número a evaluar y de
vuelven True o False. No se permite utilizar ayudas externas a las mismas.
'''


num_oblongo = lambda num: any(num == i * (i + 1) for i in range(num))
num_triangular = lambda num: any(num == i * (i + 1) // 2 for i in range(1, num))

if __name__ == "__main__":
    try:
        num = int(input("Número: "))

        if num_oblongo(num):
            print(f"El número {num} es oblongo :)")
        else:
            print(f"El número {num} no es oblongo :(")

        if num_triangular(num):
            print(f"El número {num} es triangular :)")
        else:
            print(f"El número {num} no es triangular :(")
    except ValueError:
        print(f"ERROR. Revisa de ingresar un número entero.")