
def buscar_coincidencia(lista_diccionario_paises):
    while True:
        try:
            entrada = input("Ingrese busqueda ").strip().lower()
            resultado = []
            if not entrada:
                raise ValueError("No ingreso ningún valor de búsqueda")
            print(entrada)
            for pais in lista_diccionario_paises:
                if entrada in pais["nombre"]:
                    print(pais["nombre"])
                    resultado.append(pais["nombre"])
            return resultado
        except ValueError as e:
            print(f"Error: {e}")


def buscar_exacto(lista_diccionario_paises = []):
    entrada = input("Ingrese busqueda ").lower().strip()
    encontrado = False
    for pais in lista_diccionario_paises:
        if pais["nombre"] == entrada:
            encontrado = True
            print(pais)
    if not encontrado:
        print("El pais no existe en la base de datos.")

def buscar_pais(lista_diccionario_paises):
    entrada = menus.menu_buscar_paises()
    
    match entrada:
        case "1":
            buscar_coincidencia(lista_diccionario_paises)
            
        case "2":

            pass
        case "3":

            pass
    