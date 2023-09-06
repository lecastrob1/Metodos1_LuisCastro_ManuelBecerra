import numpy as np
#Punto A
def funcion(x):
 return (np.e**(-x))-x 

def muller(f, x0, x1, x2, tol):
    fx0x1=(f(x1)-f(x0))/(x1-x0)
    fx1x2=(f(x2)-f(x1))/(x2-x1)
    a=(fx1x2-fx0x1)/(x2-x0)
    b=fx0x1-(x0+x1)*a
    c=f(x0)-(x0*fx0x1)+(x0*x1*a)
    h=x2-x1
    i=0
    while abs(h) > tol:
        D = (b ** 2 - (4 * a * c)) ** 0.5
        if abs(b - D) > abs(b + D):
            E = b - D
        else:
            E = b + D
        y = -2 * c / E
        x0 = x1
        x1 = x2
        x2 = y
        fx0x1=(f(x1)-f(x0))/(x1-x0)
        fx1x2=(f(x2)-f(x1))/(x2-x1)
        a=(fx1x2-fx0x1)/(x2-x0)
        b=fx0x1-(x0+x1)*a
        c=f(x0)-(x0*fx0x1)+(x0*x1*a)
        h=x2-x1
        i+=1
        if i==100:
           print("no se logro copilar :(")
           break
    return y,i,D

root = muller(funcion, -1,1, 0, 1*10**(-10))
print('la raiz de la función es '+str(root[0]))
print('El numero de iteraciones fueron '+str(root[1]))
print('El valor de X3 es '+str(root[0]))
#punto B


