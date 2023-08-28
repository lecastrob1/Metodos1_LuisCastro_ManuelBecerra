import matplotlib.pyplot as plt

class Mineral: 
    
    def __init__(atr, nombre, dureza, rompimiento_por_fractura, color, composicion, ilustre, specific_gravity, sistema_cristalino):
        atr.nombre = nombre
        atr.dureza = dureza
        atr.ilustre = ilustre
        atr.rompimiento_por_fractura = rompimiento_por_fractura
        atr.color = color
        atr.composicion = composicion
        atr.sistema_cristalino = sistema_cristalino
        atr.specific_gravity = specific_gravity
    
    def check_silicato(atr):
        if "O" in atr.composicion and "Si" in atr.composicion:
            print("El "+atr.nombre+" SI es un silicato")
        else:
            print("El "+atr.nombre+" NO es un silicato")
    
    def calcular_densidad(atr):
        
        densidad = atr.specific_gravity*1000
        
        print("La densidad de "+atr.nombre+" es " + str(densidad) + "kg/m3")

    def visualizar_color(atr):
        fig, ax = plt.subplots(figsize=(1, 1))
        ax.add_patch(plt.Rectangle((0, 0), 1, 1, color=atr.color))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        plt.show()

    def print_info(atr):
        
        if atr.rompimiento_por_fractura == "TRUE":
            print("La dureza de "+atr.nombre+" es "+str(atr.dureza)+ ", SI se rompe por fractura y su sistema cristalino es "+str(atr.sistema_cristalino))
        if atr.rompimiento_por_fractura == "FALSE":
            print("La dureza de "+atr.nombre+" es "+str(atr.dureza)+ ", NO se rompe por fractura y su sistema cristalino es "+ str(atr.sistema_cristalino))