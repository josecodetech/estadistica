import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
media = 10
desviacion_estandar = 2
valor_objetivo = 12
# calculo probabilidad con distribucion acumulada CDF
probabilidad = norm.cdf(valor_objetivo,media,desviacion_estandar)
print(f"Probabilidad de ser menor o igual a 12: {probabilidad*100}%")
# calculo funcion de densidad de probabilidad PDF
x = np.linspace(media- 4*desviacion_estandar,media+4*desviacion_estandar,1000)
# print(x)
pdf = norm.pdf(x,media, desviacion_estandar)
# creamos la grafica
plt.plot(x,pdf,label='PDF N(10,2)')
plt.fill_between(x,pdf,where=(x<=12),color='blue',alpha=0.3,label='P(x<=12)')
plt.xlabel('Valores')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribucion normal')
plt.legend()
plt.show()

