import csv
import os

def buscar_material(nombre_material):
    # Abre el archivo CSV
    with open('indices_refraccion.csv', 'r') as archivo:
        lector = csv.reader(archivo,delimiter=',')
        # Itera sobre las filas del archivo
        for fila in lector:
            # Comprueba si el nombre del material coincide con la columna 3
            if fila[2] == nombre_material:
                # Guarda el nombre de la columna 2
                nombre_carpeta = fila[0]
                # Guarda el nombre de la columna 3
                nombre_archivo = fila[2]
                # Construye la ruta completa al archivo
                ruta_archivo = os.path.join(nombre_carpeta, nombre_archivo)
                return ruta_archivo
def leer_datos(nombre_material):
    # Usa la función buscar_material para obtener el archivo
    material=buscar_material(nombre_material)
    # Abre el archivo con el nombre guardado
    with open(material, 'r') as archivo_material:
        # Lee todas las líneas del archivo
        lineas = archivo_material.readlines()
        # Encuentra la línea con el nombre especificado
        for i in range(len(lineas)):
            if '    data: |' in lineas[i]:
                break
        
        # Guarda los datos en forma de duplas
        duplas = []
        for linea in lineas[i+1:]:
            # Divide la línea en palabras
            palabras = linea.split()
            
            # Comprueba si las palabras son números
            if len(palabras) == 2 and all(palabra.lstrip('-').replace('.','',1).isdigit() for palabra in palabras):
                # Guarda las palabras como una dupla
                duplas.append(tuple(palabras))
            else:
                # Si las palabras no son números, termina el bucle
                break
                
    return duplas                        
