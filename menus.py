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