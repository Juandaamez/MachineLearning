# Juan David Amezquita Nuñez
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, img_as_float, img_as_bool
from skimage.measure import label, regionprops

# Lee una imagen llamada 'Placa16_8.jpg' y la almacena en la variable 'placa'
placa = io.imread('placa01.jpg')
plt.figure() # Crea una nueva figura
plt.imshow(placa) # Muestra la imagen 'placa' en la figura actual

# Permite al usuario seleccionar una región de interés (ROI) en la imagen
# y devuelve la imagen recortada 'placa' y su posición 'pos'
placa, pos = plt.imcrop(placa)

# Convierte la imagen 'placa' a escala de grises
Grayplaca = color.rgb2gray(placa)
plt.figure() # Crea una nueva figura
plt.imshow(Grayplaca, cmap='gray') # Muestra la imagen en escala de grises en la figura actual

# Convierte la imagen en escala de grises a tipo de dato float
Grayplaca = img_as_float(Grayplaca)
plt.figure() # Crea una nueva figura
plt.hist(Grayplaca.ravel(), bins=256) # Muestra el histograma de la imagen en escala de grises

# Convierte la imagen 'placa' a tipo de dato float
placa = img_as_float(placa)

# Establece un umbral para binarizar la imagen
umbral = 0.5
binPlaca = img_as_bool(placa > umbral)

# Invierte los valores de blanco y negro en la imagen binarizada
binPlaca = ~binPlaca
plt.figure() # Crea una nueva figura
plt.imshow(binPlaca, cmap='gray') # Muestra la imagen binarizada en la figura actual

# Define el número mínimo de píxeles para eliminar áreas pequeñas
numpixels = 150
Filtro1 = morphology.remove_small_objects(binPlaca, numpixels)

plt.figure() # Crea una nueva figura
plt.imshow(Filtro1, cmap='gray') # Muestra la imagen filtrada en la figura actual

# Etiqueta componentes conectados en la imagen
Lo, num = label(Filtro1, return_num=True)

# Calcula propiedades de las componentes conectadas
prop = regionprops(Lo)
plt.figure() # Crea una nueva figura
plt.imshow(Lo, cmap='nipy_spectral') # Muestra las componentes etiquetadas en la figura actual

# Recorta la región correspondiente al último número identificado
ultimo_numero = Filtro1[prop[-1].bbox[0]:prop[-1].bbox[2], prop[-1].bbox[1]:prop[-1].bbox[3]]
plt.figure() # Crea una nueva figura
plt.imshow(ultimo_numero, cmap='gray') # Muestra la región del último número en la figura actual

# Calcula las propiedades "Centroid" y "Circularity" del último número
prop_ultimo_numero = regionprops(ultimo_numero, coordinates='rc')

# Calcula el último número de Centroid y Circularity
centroid = prop_ultimo_numero[0].centroid[::-1] # Invierte el orden de las coordenadas para que coincidan con Matlab
circularity = prop_ultimo_numero[0].perimeter**2 / (4 * np.pi * prop_ultimo_numero[0].area)

# Muestra los resultados en la ventana de Command Window
print('Propiedades del último número:')
print(f'Centroid: {centroid}')
print(f'Circularity: {circularity}')
