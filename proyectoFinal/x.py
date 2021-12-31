import numpy as np
import cv2 as cv
import LBG_alg as lbg
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

"""
imagen = cv.imread("./Objetos_segmentados/appleJuice/appleJuice75BGR.jpg")#+ nombre_archivo)
imagen = cv.cvtColor(imagen, cv.COLOR_BGR2RGB)
imagen_c = cv.resize(imagen, (0,0), fx=0.5, fy=0.5)
print(imagen[0][0])
imagen_lineal = np.concatenate(imagen)
print(imagen_lineal[0][0])

imagen = np.random.randint(255, size=(100,100,3))
plt.imshow(imagen)
plt.show()

plt.imshow(imagen_c)
plt.show()

imagen_sobel_horizontal = cv.Sobel(imagen_c, ddepth=-1, dx=0, dy=1, ksize=3)
    
plt.imshow(imagen_sobel_horizontal)
plt.show()
"""
x = np.random.randint(255, size=(1000,3))
print(x)
valores = lbg.LBG()
media = np.mean(x, 0)
print(media)
regiones = valores.cuantiza(x, epsilon1= 0.001, epsilon2=-0.001, e0=0.001, dist_func=None)

centroides = valores.centroides()

# Creamos la figura
fig = plt.figure()

# Agrrgamos un plano 3D
ax = plt.axes(projection='3d')

w = [w for w, y, z in centroides[:]]
y = [y for w, y, z in centroides[:]]
z = [y for w, y, z in centroides[:]]

g = [[100 100 100]]
print("g: ", g)
print(centroides)
print(w)

# plot_wireframe nos permite agregar los datos x, y, z. Por ello 3D
# Es necesario que los datos esten contenidos en un array bi-dimensional
#ax1.plot_wireframe(w, y, z)

# Mostramos el grafico
ax.plot(w,y,z,'red')
ax.scatter3D(w,y,z)
plt.show()