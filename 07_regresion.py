import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
ventas = np.array([50,60,70,80,90,70,80,90,65,35])
gastos_publicidad = np.array([30,40,50,60,70,40,50,30,25,65])
coef_correlacion = np.corrcoef(ventas, gastos_publicidad)[0,1]
print(f"Coeficiente de correlacion de Pearson {coef_correlacion}")
# creamos el modelo
model = LinearRegression()
# ajustar el modelo 
model.fit(gastos_publicidad.reshape(-1,1),ventas)
# coef pendiente y la interseccion
pendiente = model.coef_[0]
interseccion = model.intercept_
# generamos las predicciones
ventas_pred = model.predict(gastos_publicidad.reshape(-1,1))
print(ventas_pred)
# grafica
plt.scatter(gastos_publicidad,ventas,label='Ventas / Gastos publicidad')
plt.plot(gastos_publicidad,ventas_pred,color='red',label='Regresion lineal')
plt.xlabel('Gastos publicidad')
plt.ylabel('Ventas')
plt.title("Ventas / Gastos publicidad")
plt.legend()
plt.show()
# mostramos valores 
print(f'Pendiente: {pendiente}')
print(f'Interseccion: {interseccion}')
