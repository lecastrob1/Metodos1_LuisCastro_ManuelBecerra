from expansiontermicamineral import ExpansionTermicaMineral #llama la clase de otro .py
import matplotlib.pyplot as plt

archivo1 = 'olivine_angel_2017.csv'
olivine = ExpansionTermicaMineral(archivo1)
print("El error global del olivine es "+str(olivine.calcular_y_graficar()[0]))
print("El coeficiente de expansion del olivine es "+str(olivine.calcular_y_graficar()[1]))
print("Y esta es las graficas de Olivine")
plt.show()

archivo2 = 'graphite_mceligot_2016.csv'
graphite = ExpansionTermicaMineral(archivo2)
print("El error global del grafito es "+str(graphite.calcular_y_graficar()[0]))
print("El coeficiente de expansion del grafito es "+str(graphite.calcular_y_graficar()[1]))
print("Y esta es las graficas de Grafito")
plt.show()