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
    lines = file.readlines()

#se salta la primera linea
for index, line in enumerate(lines):
    if index == 0:
        continue  
#se separan los numeros y agrega el punto a la lista del axis correspondiente
    puntos = line.strip().split(',')
    puntos_x.append(puntos[0])
    puntos_y.append(puntos[1])

#se asigna un arreglo a las listas y hace los valores adentros floats
X = np.array(puntos_x, dtype=float)
Y = np.array(puntos_y, dtype=float)

#funcion de interpolacion 
def InterpolacionNewton(X,Y,x):
    
    sum_ = Y[0]
    
    Diff = np.zeros(( X.shape[0],Y.shape[0] ))
    h = X[1]-X[0]
    
    Diff[:,0] = Y

    poly = 1.
    
    for i in range(1,len(X)):
        
        poly *= (x-X[i-1])
        
        for j in range(i,len(X)):
            
            Diff[j,i] = Diff[j,i-1] - Diff[j-1,i-1] 
    
        sum_ += poly*Diff[i,i]/(np.math.factorial(i)*h**(i))
        
    return sum_

#se ejecuta la interpolacion
xt = np.linspace(np.min(X),np.max(X),100)
yt = []

for x in xt:
    yt.append(InterpolacionNewton(X,Y,x))
    
#se grafica
plt.scatter(X,Y,color='r')
plt.plot(xt,yt,color='b')
plt.title("Grafica de Interpolacion")
plt.xlabel("Posicion x")
plt.ylabel("Posicion y")
plt.show()

#esta parte te escribe la ecuacion de interpolacion
x = sym.Symbol('x',real=True)
y = InterpolacionNewton(X,Y,x)
y = sym.simplify(y)

def hallar_v0_te(X,Y):
    teta=np.arctan(0.363970234266202)
    muesteta=np.around(np.degrees(teta))
    cor=np.cos(teta)
    tar=np.tan(teta)
    V2=(9.8*(X[0]**2))/(2*((cor)**2)*((X[0])*(tar)-Y[0]))
    V=np.sqrt(V2)
    return V,muesteta
print(hallar_v0_te(X,Y))