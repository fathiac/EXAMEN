productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}
def stock_marca():
        
        marca=input(" INGRESE LA MARCA:").upper()
        if marca in productos[1]:
            if stock[1]:
                print(" MARCA ENCONTRADA ")
                print(" SE ENCUENTRA UN STOCK {stock}")
        else:
            print(" LA MARCA INGRESADA NO SE ENCUENTRA ")


def busqueda_precio():
    p_minimo=int((" INGRESE EL PRECIO MIN:"))
    if p_minimo>0:
        print(f"{p_minimo}")
        
    else:
        print(" DEBE INGRESAR UN NUMERO ENTERO POSITIVO")

    p_maximo=int(input(" INGRESE EL PRECIO MAX: "))
    if p_maximo>0:
        print(f"{p_maximo}")
    else:
        print(" DEBE INGRESAR UN NUMERO ENTERO POSITIVO")
    if [2] in stock:
         print(f" ESTOS SON LOS PRODUCTOS EN STOCK {stock,[2]}")
    else:
         print(" NO SE ENEUNTRAN PRODUCTOS DENTRO DE ESE RANGO ")


def actualizar_precio():
    modelo=input(" INGRESE MODELO QUE DESEE ACATUALIZAR: ")
    p_nuevo=int(input(" INGRESE EL NUEVO PRECIO: "))
    if modelo in productos:
        print(" EL MODELO SE HA ENCONTRADO ")
        print(f" ACTUALIZACION EXITOSA EL NUEVO PRECIO DE {modelo} ES {p_nuevo}")
    else:
        print(" NO SE HAN ENCONTRADO REGISTROS DE EL MODELO")

    print(" DESEA ACTUALIZAR OTRO MODELO SI/NO ")
    otro_modelo=input(" INGRESE SU RESPUESTA SI/NO ").strip().upper()
    if otro_modelo=="SI".upper():
            modelo=input(" INGRESE MODELO QUE DESEE ACATUALIZAR: ")
            p_nuevo=int(input(" INGRESE EL NUEVO PRECIO: "))
            if modelo in productos:
                print(" EL MODELO SE HA ENCONTRADO ")
                print(f" ACTUALIZACION EXITOSA EL NUEVO PRECIO DE {modelo} ES {p_nuevo}")
            else:
                print(" NO SE HAN ENCONTRADO REGISTROS DE EL MODELO")

    else:
        print(" ADIOS ")



def menu():
    print("1. Stock marca")
    print("2. Búsqueda por precio")
    print("3. Actualizar precio")
    print("4. Salir")
    
def main():
    while True:
            menu()
            try:
                opc=int(input(" ingrese una opcion: "))
            except ValueError:
                print(" debe ingresar una opcion correcta")
                continue
            if opc==1:
                    stock_marca()
            elif opc==2:
                    busqueda_precio()
            elif opc==3:
                    actualizar_precio()
            elif opc==4:
                    print(" programa finalizado ")
            else:
                    print(" PROGRAMA FINALIZADO ")
                    break
main()