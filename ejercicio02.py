import matplotlib.pyplot as plt
datos = [10,12,14,16,18,20,20,22,22,22,24,24,26,28,30]
plt.hist(datos, bins=10,edgecolor='orange')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma de datos')
plt.show()