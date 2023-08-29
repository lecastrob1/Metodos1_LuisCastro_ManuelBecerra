import csv
import os
import unicodedata
import matplotlib.pyplot as plt
import numpy as np

def buscar_material(nombre_material):
    # Abre el archivo CSV
    with open('indices_refraccion.csv', 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo,delimiter=',')
        # Itera sobre las filas del archivo
        for fila in lector:
            # Comprueba si el nombre del material coincide con la columna 3
            if fila[2] == nombre_material:
                # Guarda el nombre de la columna 2
                nombre_carpeta = unicodedata.normalize('NFC', fila[0])
                # Guarda el nombre de la columna 3
                nombre_archivo = fila[2]
                # Construye la ruta completa al archivo
                ruta_archivo = os.path.join(nombre_carpeta, nombre_archivo)
                return ruta_archivo, nombre_carpeta

def leer_datos(nombre_material):
    # Usa la función buscar_material para obtener el archivo y la carpeta
    material, carpeta = buscar_material(nombre_material)
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
            
            # Termina cuando encuentra una línea vacía o las palabras "SPECS:"
            elif len(palabras) == 0 or "SPECS:" in linea:
                break
                
    return duplas, carpeta

def graficar_datos(nombre_material):
    # Usa la función leer_datos para obtener los datos y la carpeta
    datos, carpeta = leer_datos(nombre_material)
    
    datos = np.array(datos, dtype=float)

    # Calcula el promedio y la desviación estándar para cada material
    promedio = np.mean(datos[:, 1])
    desviacion = np.std(datos[:, 1])

    # Crea el gráfico
    plt.figure(figsize=(10, 6))

    # Grafica los datos para el material
    plt.plot(datos[:, 0], datos[:, 1], label=nombre_material)

    # Añade títulos y etiquetas
    plt.title(f'Índice de refracción vs longitud de onda\n'
              f'{nombre_material}: promedio={promedio:.2f}, desviación estándar={desviacion:.2f}')
    plt.xlabel('Longitud de onda (nm)')
    plt.ylabel('Índice de refracción')
    plt.legend()

    # Guarda el gráfico en la carpeta correspondiente a la categoría del material
    plt.savefig(os.path.join(carpeta, f'{nombre_material}.png'))

# Lee todos los nombres de materiales en materiales.txt y grafica cada uno
with open('materiales.txt', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    next(lector)  # Salta la primera fila
    for fila in lector:
        graficar_datos(fila[0])
