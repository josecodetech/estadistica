import numpy as np
from scipy.stats import t
# datos de ejemplo
edades = [22,25,20,35,12,36,25,21,30,42,35,41,21,25,26,27,28,29,30,31,25,24,23,21]
# tamaño muestra
n = len(edades)
# Media y desviacion estandar 
media = np.mean(edades)
desviacion_estandar = np.std(edades,ddof=1)
# Intervalo de confianza del 95% para la media
valor_referencia = 29
t_estadistico = (media - valor_referencia) / (desviacion_estandar / np.sqrt(len(edades)))
grados_libertad = len(edades)-1
# print(t_estadistico)
nivel_significancia = 0.05
t_critico = t.ppf(1-nivel_significancia/2, df=grados_libertad)
print(f'El t critico es {t_critico}')
print(f'El t estadistico es {t_estadistico}')
if abs(t_estadistico)>t_critico:
    print("Rechazamos la hipotesis nula")

else:
    print("No hay suficiente evidencia para rechazar la hipotesis nula")
    