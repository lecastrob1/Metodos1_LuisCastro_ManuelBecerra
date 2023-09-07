from mineral import Mineral #llama la clase de otro .py+
import numpy as np
import matplotlib.pyplot as plt

class ExpansionTermicaMineral():
    
    def __init__(self, archivo):
        self.puntos_T = []
        self.puntos_V = []
        self.archivo = archivo

#lee el archivo
        with open(self.archivo, 'r', encoding='latin-1') as file:
            lines = file.readlines()
                
        for index, line in enumerate(lines):
            if index == 0:
                continue  # salta la primera linea
                
            puntos = line.strip().split(',')
            self.puntos_T.append(float(puntos[0]))
            self.puntos_V.append(float(puntos[1]))
        
    def calcular_y_graficar(self):
            coeficientes = list()
            i=0
            
            while i in range(0, len(self.puntos_T)):

                Y1 = self.puntos_V[i]
                h = self.puntos_T[i] -self.puntos_T[i-1]
                
                #aqui se usa la derivada central
                derivada = (self.puntos_V[i] - self.puntos_V[i-1])/(2*h)
                
                a = (1/Y1)*derivada
                coeficientes.append(a)
                i += 1

            
            fig, axs = plt.subplots(1, 2, figsize=(12, 6))
            
            axs[0].plot(self.puntos_T,self.puntos_V,label='',color='b')
            axs[0].set_xlabel('T(C)')
            axs[0].set_ylabel('V(cm3)')
            axs[0].set_title('Volumen vs Temperatura')
            
            
            axs[1].plot(self.puntos_T,coeficientes,label='',color='r')
            axs[1].set_xlabel('T(C)')
            axs[1].set_ylabel('a')
            axs[1].set_title('Coeficiente vs Temperatura')
            axs[1].set_ylim(0, 0.0001)
            plt.show
            
            error_global=np.std(coeficientes)/np.sqrt(len(coeficientes))
            
            return plt, error_global