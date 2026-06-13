# Programación 1

# Trabajo páctico integrador

# Melisa
# Alejandro G. Mazzaforte
import csv
##################################################################################
########## IMPORTAR DATOS
##################################################################################
def importar_datos():

    try:
        with open('paises.csv', 'r', encoding='utf-8') as file:

            archivo_paises = csv.reader(file)
            cabecera = next(archivo_paises)

            if cabecera != ["nombre", "poblacion", "superficie", "continente"]:
                raise ValueError(
                    "La cabecera del archivo no es válida"
                )

            lista_diccionario_paises = []

            for fila in archivo_paises:
                if len(fila) != 4:
                    raise ValueError(
                        f"Fila incompleta: {fila}"
                    )
                poblacion = int(fila[1])
                superficie = int(fila[2])

                if poblacion < 0:
                    raise ValueError(
                        f"Población inválida en {fila[0]}"
                    )

                if superficie < 0:
                    raise ValueError(
                        f"Superficie inválida en {fila[0]}"
                    )

                lista_diccionario_paises.append({
                    "nombre": fila[0].lower(),
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": fila[3].lower()
                })

            return lista_diccionario_paises

    except FileNotFoundError:
        print("No se encontró el archivo paises.csv")

    except ValueError as e:
        print(f"Error: {e}")
##################################################################################

##################################################################################
#### MENUS
##################################################################################

#menus.py

def menu_principal():
    opciones_validas = ["1", "2", "3", "4","5", "6", "7"]
    while True:
        try:
            print("""
                Elija en el siguiente menú la opcion que necesite..
                    1. Agregar un país.
                    2. Actualizar los datos de Población y Superficie de un País.
                    3. Buscar un país por nombre (coincidencia parcial o exacta).
                    4. Filtrar países.
                    5. Ordenar países.
                    6. Mostrar estadísticas.
                    7. Para salir del sistema.
        """)

            opcion = input("Elija su opción ")

            if opcion not in opciones_validas:
                raise ValueError(f"'{opcion}' no es válida. Ingrese 1-7") 
              
            return opcion
        
        except ValueError as e:
            print(f"Error {e}")
            input("Presione Enter para continuar")


# Menú para filtrar por paises
def menu_buscar_paises():
  
    opciones_validas = ["1", "2", "3", "4"]

    while True:
        try:
            print("""
                  --- Criterios de búsqueda de paises ---
                  Elija en el siguiente menú la opcion que necesite..
                    1. Coincidencia parcial.
                    2. Nombre exacto.
                    3. Volver al menu principal
                  """)            
            entrada = input("Seleccione: ").strip()
            
            if entrada not in opciones_validas:
                raise ValueError(f"'{entrada}' no es válida. Ingrese 1-4")            
            return entrada            
        except ValueError as e:
            print(f" Error: {e}")
            input("Presione Enter para continuar...")



# Menú para filtrar por paises
def menu_filtrar_paises():
  
    opciones_validas = ["1", "2", "3", "4"]

    while True:
        try:
            print("""
                  --- Criterios de filtrado de paises ---
                  Elija en el siguiente menú la opcion que necesite..
                    1. Continente
                    2. Rango de población
                    3. Rango de superficie
                    4. Volver al menu principal

                  """)            
            filtro = input("Seleccione: ").strip()
            
            if filtro not in opciones_validas:
                raise ValueError(f"'{filtro}' no es válida. Ingrese 1-4")            
            return filtro            
        except ValueError as e:
            print(f" Error: {e}")
            input("Presione Enter para continuar...")

# Menú para ordenar paises
def menu_ordenar_paises():
  
    opciones_validas = ["1", "2", "3", "4"]

    while True:
        try:
            print("""
                  --- Criterios de orden de paises ---
                  Elija en el siguiente menú la opcion que necesite..
                    1. Nombre.
                    2. Población.
                    3. Superficie (ascendente o descendente).
                    4. Volver al menu principal
                  """)            
            orden = input("Seleccione: ").strip()
            
            if orden not in opciones_validas:
                raise ValueError(f"'{orden}' no es válida. Ingrese 1-4")            
            return orden            
        except ValueError as e:
            print(f" Error: {e}")
            input("Presione Enter para continuar...")

# Menú para estadisticas
def menu_estadisticas():
  
    opciones_validas = ["1", "2", "3"]

    while True:
        try:
            print("""
                  --- Estadísticas ---
                  Elija en el siguiente menú la opcion que necesite..
                    1. País con mayor y menor población.
                    2. Promedio de población.
                    3. Volver al menu principal 
                  """)            
            filtro = input("Seleccione: ").strip()
            
            if filtro not in opciones_validas:
                raise ValueError(f"'{filtro}' no es válida. Ingrese 1-3")            
            return filtro            
        except ValueError as e:
            print(f" Error: {e}")
            input("Presione Enter para continuar...")
##################################################################################

##################################################################################
### OPERACIONES CON PAISES
##################################################################################

def buscar_coincidencia(lista_diccionario_paises):
    while True:
        try:
            entrada = input("Ingrese busqueda ").strip().lower()
            resultado = []
            if not entrada:
                raise ValueError("No ingreso ningún valor de búsqueda. Intente nuevamente.")
            
            for pais in lista_diccionario_paises:
                if entrada in pais["nombre"]:
                    print(pais["nombre"])
                    resultado.append(pais["nombre"])
            if not resultado:
                print("No se encontraron coincidencias con la búsqueda.")
            return resultado
        except ValueError as e:
            print(f"Error: {e}")


def buscar_exacto(lista_diccionario_paises):
    try:
        entrada = input("Ingrese busqueda ").lower().strip()
        encontrado = False
        if not entrada:
            raise ValueError("No ingreso ningún valor de búsqueda. Intente nuevamente.")
        for pais in lista_diccionario_paises:
            if pais["nombre"] == entrada:
                encontrado = True
                print(pais)
        if not encontrado:
            print("El pais no existe en la base de datos.")
    except ValueError as e:
        print(f"Error: {e}")

def buscar_pais(lista_diccionario_paises):
    entrada = menu_buscar_paises()
    
    match entrada:
        case "1":
            buscar_coincidencia(lista_diccionario_paises)
            
        case "2":
            buscar_exacto(lista_diccionario_paises)
            pass
        case "3":

            pass
##################################################################################






##################################################################################
###### FUNCION MAIN
##################################################################################
def main():

    print("""
    Bienvenido al sistema de análisis geográfico mundial
    """)
    lista_diccionario_paises = importar_datos()
    opcion = ""

    while opcion != 7:
        opcion = menu_principal()
        match opcion:
            case "1":
            
                pass
            case "2":
                pass
            case "3":
                buscar_pais(lista_diccionario_paises)
                pass
            case "4":
                menu_filtrar_paises()
            case "5":
                pass
            case "6":
                pass
            case "7":
                print("Gracias por utilizar nuestro sistema! Lo esperamos nuevamente!!")
                break
                
    return lista_diccionario_paises

main()
