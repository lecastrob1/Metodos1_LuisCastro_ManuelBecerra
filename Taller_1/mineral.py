import matplotlib.pyplot as plt


class Mineral: 
    
    #aqui se asignan los atributos
    def __init__(atr, nombre, dureza, rompimiento_por_fractura, color, composicion, ilustre, specific_gravity, sistema_cristalino):
        atr.nombre = nombre
        atr.dureza = float(dureza)
        atr.ilustre = ilustre
        atr.rompimiento_por_fractura = rompimiento_por_fractura
        atr.color = color
        atr.composicion = composicion
        atr.sistema_cristalino = sistema_cristalino
        atr.specific_gravity = float(specific_gravity)
    
    #este es el metodo que chequa si es un silicato
    def check_silicato(atr):
        
        if "O" in atr.composicion and "Si" in atr.composicion:
            check = True
        else:
            check = False
    
        return(check)
    
    #este es el metodo calcula la densidad
    def calcular_densidad(atr):
        
        densidad = atr.specific_gravity*1000
        #el specific gravity solo es la razon de densidad del material 
        #con la densidad del agua entonces solo se multiplica por 1000 (la densidad del agua)
        
        return(densidad)

    #este metodo produce un cuadrado con el color del material
    def visualizar_color(atr):
        fig, ax = plt.subplots(figsize=(1, 1))
        ax.add_patch(plt.Rectangle((0, 0), 1, 1, color=atr.color))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        plt.show()
    
    #este metodo chequea si tiene rompimiento por fractura y le dice al usador
    def print_info(atr):
        
        if atr.rompimiento_por_fractura == "TRUE":
            print("La dureza de "+atr.nombre+" es "+str(atr.dureza)+ ", SI se rompe por fractura y su sistema cristalino es "+str(atr.sistema_cristalino))
        if atr.rompimiento_por_fractura == "FALSE":
            print("La dureza de "+atr.nombre+" es "+str(atr.dureza)+ ", NO se rompe por fractura y su sistema cristalino es "+ str(atr.sistema_cristalino))