# Programación 1

# Trabajo páctico integrador

# Melisa
# Alejandro G. Mazzaforte
import csv
def importar_datos():
    with open('paises.csv', 'r', encoding='utf-8') as file:
        archivo_paises = csv.reader(file)
        
        lista_diccionario_paises = []
        
        for fila in archivo_paises:
            lista_diccionario_paises.append({"nombre":fila[0], "poblacion": int(fila[1]), "superficie": int(fila[2]), "continente":fila[3]})
        return lista_diccionario_paises
    

def main():

    print("""
    Bienvenido al sistema de análisis geográfico mundial
    """)
    lista_diccionario_paises = []
    opcion = ""

    while True:
        
        match opcion:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                print("Gracias por utilizar nuestro sistema! Lo esperamos nuevamente!!")
                break
                
    return lista_diccionario_paises

main()
