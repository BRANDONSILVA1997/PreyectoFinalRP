
import numpy as np
import reconocimiento_patrones as rp
import cv2 as cv

class Imagen():
    
    #En ""nombre_archivo" se coloca el nombre del archivo, con la ruta del archivo si no esta 
    #en el mismo directorio del programa que use la clase.
    def __init__(self, nombre_archivo, tipo_imagen=1):
        self.tipo_imagen = tipo_imagen
        self.vectores_r = None
        self.vectores_a = None
        self.vectores_coeficientes_wiener = None
        self.nombre = nombre_archivo
        self.imagen = None
        #Las imagenes estan en formato BGR originalmente
        self.imagen_RGB = cv.cvtColor(cv.imread(nombre_archivo), cv.COLOR_BGR2RGB)
        self.imagen_HSV = cv.cvtColor(cv.imread(nombre_archivo), cv.COLOR_BGR2HSV)
        #La imagen se debe reducir al 50% "fx=0.5", "fy=0.5"
        self.imagen_RGB_reducida = cv.resize(self.imagen_RGB, (0,0), fx=0.5, fy=0.5)
        self.imagen_HSV_reducida = cv.resize(self.imagen_HSV, (0,0), fx=0.5, fy=0.5)
        self.imagen_RGB_reducida_sobel_horizontal = cv.Sobel(self.imagen_RGB_reducida, ddepth=-1, dx=0, dy=1, ksize=3)
        self.imagen_RGB_reducida_sobel_vertical = cv.Sobel(self.imagen_RGB_reducida, ddepth=-1, dx=1, dy=0, ksize=3)
        self.imagen_HSV_reducida_sobel_horizontal = cv.Sobel(self.imagen_HSV_reducida, ddepth=-1, dx=0, dy=1, ksize=3)
        self.imagen_HSV_reducida_sobel_vertical = cv.Sobel(self.imagen_HSV_reducida, ddepth=-1, dx=1, dy=0, ksize=3)
        #Las imagenes se trabajan como un arreglo de una dimension con los pixeles para realizar un cuantizador ("self.imagen").
        # Si se usa como una imagen a reconocer invocar "self.imagen_RGB", etc, para tener una matriz de dos dimensiones.
        #Con un entero (tipo_imagen) se escoge el formato de la imagen en una dimension
        if self.tipo_imagen == 1: #imagen BGR a RGB
            self.imagen = np.concatenate(self.imagen_RGB)
        elif self.tipo_imagen == 2: #imagen BGR a HSV 
            self.imagen = np.concatenate(self.imagen_HSV)
        elif self.tipo_imagen == 3: #imagen reducida RGB + sobel horizontal + sobel vertical 
            self.imagen_RGB_reducida = np.concatenate(self.imagen_RGB_reducida)
            self.imagen_RGB_reducida_sobel_horizontal = np.concatenate(self.imagen_RGB_reducida_sobel_horizontal)
            self.imagen_RGB_reducida_sobel_vertical = np.concatenate(self.imagen_RGB_reducida_sobel_vertical)
            self.imagen = []
            for i in range(0, len(self.imagen_RGB_reducida)):
                aux = np.concatenate((self.imagen_RGB_reducida[i], self.imagen_RGB_reducida_sobel_horizontal[i], self.imagen_RGB_reducida_sobel_vertical[i]))
                self.imagen.append(aux)
        else:  #imagen reducida HSV + sobel horizontal + sobel vertical
            self.imagen_HSV_reducida = np.concatenate(self.imagen_HSV_reducida)
            self.imagen_HSV_reducida_sobel_horizontal = np.concatenate(self.imagen_HSV_reducida_sobel_horizontal)
            self.imagen_HSV_reducida_sobel_vertical = np.concatenate(self.imagen_HSV_reducida_sobel_vertical)
            self.imagen = []
            for i in range(0, len(self.imagen_HSV_reducida)):
                aux = np.concatenate((self.imagen_HSV_reducida[i], self.imagen_HSV_reducida_sobel_horizontal[i], self.imagen_HSV_reducida_sobel_vertical[i]))
                self.imagen.append(aux)
            
        
