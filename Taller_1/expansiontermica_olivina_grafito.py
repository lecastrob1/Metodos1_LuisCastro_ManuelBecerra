from expansiontermicamineral import ExpansionTermicaMineral #llama la clase de otro .py
import matplotlib.pyplot as plt

archivo1 = 'olivine_angel_2017.csv'
olivine = ExpansionTermicaMineral(archivo1)
olivine.calcular_y_graficar()

archivo2 = 'graphite_mceligot_2016.csv'
graphite = ExpansionTermicaMineral(archivo2)
graphite.calcular_y_graficar()
plt.show