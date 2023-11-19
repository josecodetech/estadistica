import numpy as np
datos = [10,12,14,16,18,20,22,23,25,29,34]
media = round(np.mean(datos),2)
mediana = np.median(datos)
desviacion_estandar = round(np.std(datos),2)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desviacion estandar: {desviacion_estandar}")
