import csv

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

if profesor_falopeado:
    print("No entre al campus otario!!!")
else:
    print("Sos un otario igual.")