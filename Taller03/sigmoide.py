import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


w0 = 2.0
w1 = -1.5
x = 1.0

resultado_sigmoid = sigmoid(w0 + w1 * x)


print("Resultado del cálculo de sigma(w0 + w1 * x) con x =", x, ":")
print("sigma(w0 + w1 * x) =", resultado_sigmoid)

if resultado_sigmoid >= 0.5:
    clase = "positiva"
else:
    clase = "negativa"


print("El ejemplo con x =", x, "se clasifica como clase", clase + ".")

# Graficar la función sigmoidal
x_values = np.linspace(-5, 5, 100)  # Valores de x desde -5 hasta 5
y_values = sigmoid(w0 + w1 * x_values)

plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label='sigmoid(w0 + w1 * x)', color='blue')
plt.scatter(x, resultado_sigmoid, color='red', label=f'x = {x}, Clase: {clase}')
plt.axhline(y=0.5, color='gray', linestyle='--', label='Umbral de Clasificación (0.5)')
plt.xlabel('x')
plt.ylabel('sigma(w0 + w1 * x)')
plt.title('Gráfica de la Función Sigmoidal y Clasificación')
plt.legend()
plt.grid(True)
plt.show()