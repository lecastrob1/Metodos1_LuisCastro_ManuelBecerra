import numpy as np
import matplotlib.pyplot as plt

archivo = 'Parabolico.csv'
puntos_x = []
puntos_y = []

with open(archivo, 'r', encoding='latin-1') as file:
    lines = file.readlines()
   
for index, line in enumerate(lines):
    if index == 0:
        continue  
    
    puntos = line.strip().split(',')
    puntos_x.append(puntos[0])
    puntos_y.append(puntos[1])

X = np.array(puntos_x)
Y = np.array(puntos_y)

def Lagrange(x,X,i):
    
    L = 1
    
    for j in range(X.shape[0]):
        if i != j:
            L *= (x - X[j])/(X[i]-X[j])
            
    return L

def Interpolate(x,X,Y):
    
    Poly = 0
    
    for i in range(X.shape[0]):
        Poly += Lagrange(x,X,i)*Y[i]
        
    return Poly

x = np.linspace(-2.,3.,100)
y = Interpolate(x,X,Y)

plt.plot(x,y,color='k',label='OK')
plt.scatter(X,Y,color='r',marker='o')
plt.legend()
