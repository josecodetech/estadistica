espacio_muestral = [1,2,3,4,5,6]
numeros_pares = len([x for x in espacio_muestral if x%2 == 0])
probabilidad_par = numeros_pares / len(espacio_muestral)
print(f"La probabilidad de obtener un numero par es : {probabilidad_par}")