import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

#llama al archivo
archivo = 'Parabolico.csv'
#produce dos listas vacias para los puntos en x y y
puntos_x = []
puntos_y = []

#se abre y lee el archivo Parabolico.csv
with open(archivo, 'r', encoding='latin-1') as file:
    Puntos = file.readlines()

#se salta la primera linea 
for index, line in enumerate(Puntos):
    if index == 0:
        continue  
#se separan los numeros y agrega el punto a la lista del axis correspondiente  
    puntos = line.strip().split(',')
    puntos_x.append(puntos[0])
    puntos_y.append(puntos[1])

#se asigna un arreglo a las listas y hace los valores adentros floats
X = np.array(puntos_x, dtype=float)
Y = np.array(puntos_y, dtype=float)

#se define el lagrange que va ayudar para la interpolacion
def Lagrange(x,X,i):
    
    L = 1
    
    for j in range(X.shape[0]):
        if i != j:
            L *= (x - X[j])/(X[i]-X[j])
            
    return L

#se define la interpolacion
def Interpolate(x,X,Y):
    
    Poly = 0
    
    for i in range(X.shape[0]):
        Poly += Lagrange(x,X,i)*Y[i]
        
    return Poly

#se asigna
x = np.linspace(min(X),max(X),100)
y = Interpolate(x,X,Y)

#se grafica
plt.plot(x,y,color='k')
plt.scatter(X,Y,color='r',marker='o')
plt.title("Grafica de Interpolacion")
plt.xlabel("Posicion x")
plt.ylabel("Posicion y")
plt.legend()

#se produce la ecuacion
x = sym.Symbol('x',real=True)
y = Interpolate(x,X,Y)
y = sym.simplify(y)
print("La ecuacion de la grafica es "+y)

def hallar_v0_te(X,Y):
    teta=np.arctan(0.363970234266202)
    muesteta=np.around(np.degrees(teta))
    cor=np.cos(teta)
    tar=np.tan(teta)
    V2=(9.8*(X[0]**2))/(2*((cor)**2)*((X[0])*(tar)-Y[0]))
    V=np.sqrt(V2)
    return V,muesteta
print(hallar_v0_te(X,Y))