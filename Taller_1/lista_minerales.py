
from mineral import Mineral #llama la clase de otro .py

#se produce un arreglo vacio
minerales_arreglo = []

archivo = 'minerales.txt'

#aqui lee el archvo linea por linea minerales.txt 
with open(archivo, 'r', encoding='latin-1') as file:
    lines = file.readlines()
    
for index, line in enumerate(lines):
    if index == 0:
        continue  # para slatarse la primera fila
    
    atributos = line.strip().split('\t') #separa y crea una lista por atributos

    #este proximo if arma la clase de dado material de la lista y lo agrega al arreglo
    if len(atributos) == 8:
        nombre, dureza, rompimiento_por_fractura, color, composicion, ilustre, specific_gravity, sistema_cristalino = atributos
        clase = Mineral(nombre, dureza, rompimiento_por_fractura, color, composicion, ilustre, specific_gravity, sistema_cristalino)
        minerales_arreglo.append(clase)

#este def conta los silicatos usando el arreglo anterior y anuncia cuantos hay
def contar_silicatos(minerales_arreglo):
    x=0
    i=0
    while i < len(minerales_arreglo):
        if minerales_arreglo[i].check_silicato() == True:
            x+= 1
        i+= 1
    print("Hay "+str(x)+" silicatos en esta lista de minerales")

contar_silicatos(minerales_arreglo)

#este def calcula la densidad promedia de los minerales en el arreglo
def calc_densidad_promedio(minerales_arreglo):

        i=0
        total=0
        while i < len(minerales_arreglo):
            total = total + float(minerales_arreglo[i].calcular_densidad())
            i+= 1
        promedio = total/len(minerales_arreglo)
        print("El promedio de la densidad de estos materiales es "+str(round(promedio,2))+"kg/m3")

calc_densidad_promedio(minerales_arreglo)