#parte C
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.1,1.1,100)
h =0.01
def raiz_tan (x):
    return np.sqrt(np.tan(x))
def Derivadaprogresiva(f,x,h):
    
    d = 0.
    
    if h != 0:
        d = (f(x+h) - f(x))/h
        
    return d
proDerivative = Derivadaprogresiva(raiz_tan,x,h)
#Parte D
def DerivadaCentral(f,x,h):
    
    d = 0.
    
    if h != 0:
        d = (f(x+h) - f(x-h))/(2*h)
        
    return d
CDerivative = DerivadaCentral(raiz_tan,x,h)
#Parte E
def ExactDerivative(x):
    return (1 / np.cos (x)) ** 2 / (2 * np.sqrt (np.tan (x)))
EDerivative = ExactDerivative(x)

plt.scatter(x,EDerivative,label='Exacta', s=10)
plt.scatter(x,proDerivative,label='Derivada Derecha', s=10)
plt.scatter(x,CDerivative,label='Derivada Central', s=10)
plt.legend()

#Parte F
ErrorR = np.abs(EDerivative-proDerivative)
ErrorC = np.abs(EDerivative-CDerivative)
plt.scatter(x,ErrorR,label='error_progresiva', s=10)
plt.scatter(x,ErrorC,label='error_central',s=10)
plt.legend()
plt.show()
#no tienen la misma precision ya que el error centrado es muchisimo menor
