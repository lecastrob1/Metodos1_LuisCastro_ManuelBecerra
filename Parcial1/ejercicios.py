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
        
        if abs(y) < tol:
            break
        

        if i==100:
            print("No se pudo")
        i+=1
    return y,i,D
            
            

#Punto B y C
print("Nuestro x_0 es -1, nuestro x_1 es 1 y nuestro x_2 es 0")
root = muller(funcion, -1,1, 0, 1*10**(-10))

print("La raiz es "+str(root[0])+" numero de iteraciones es "+str(root[1])+" x_3 es "+str(root[2]))






