import matplotlib.pyplot as plt
import numpy as np

#06
seccion = ["US", "EMEA", "APAC"]
api = [100, 150, 200]
mobile = [50, 75, 100]
web = [25, 50, 75]
colores = ["red", "orange", "green"]

# Crear el gráfico de barras acumulado
x = range(len(seccion)) # Posiciones para las barras
height = [0] * len(seccion) # Alturas iniciales para las barras
for i in range(len(colores)):
    # Crear las barras para cada tipo de dato
    plt.bar(x, eval(f"{colores[i][0]}"), bottom=height, color=colores[i], label=f"{colores[i][0].upper()}")
    # Sumar los valores para apilar las siguientes barras
    height = [x + y for x, y in zip(height, eval(f"{colores[i][0]}"))]

# Añadir los títulos y etiquetas
plt.title("Costo por sección y tipo de dato")
plt.xlabel("Sección")
plt.ylabel("Costo")
plt.xticks(x, seccion) # Etiquetas para el eje x
plt.legend() # Mostrar la leyenda

# Mostrar el gráfico
plt.show()