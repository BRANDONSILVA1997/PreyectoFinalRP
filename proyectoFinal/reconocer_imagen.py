import numpy as np
import reconocimiento_patrones as rp
import procesamiento_imagen as pim
import LBG_alg as lbg

#Cambiar "ruta", "num_imagenes_reconocidas" y "grupo_imagenes" segun el grupo de imagenes que se quiere reconocer
ruta = "./appleJuice"
grupo_imagenes = "appleJuice_HSV_15"
num_imagenes_reconocidas = 15
#Se crean las clases que permiten manipular las imagenes que se reconoceran
if __name__ == '__main__':
    nombres = pim.obtiene_nombres_archivos(ruta)
    print(f"Se encontraron {len(nombres)} archivos:")
    for nombre in nombres:
        print(nombre)
    imagenes = pim.procesa_imagenes(ruta, nombres, 2) #Cambiar el ultimo valor para escoger el formato de los pixeles

#Se obtienen los centroides de los 10 cuantizadores a partir de un archivo .txt y se almacenan en una lista
    cuantizadores = [[],[],[],[],[],[],[],[],[],[]]
    archivo = open("cuantizadores_HSV.txt", "r") #Cambiar el nombre del archivo segun las imagenes que se reconoceran
    for linea in archivo: #Cada linea tiene el nombre del cuantizador y un centroide
        linea = linea.rstrip("\\n")
        #Se revisa de que cuantizador es cada linea y se asigna a la sublista que le corresponde
        cuantizador_es_apple_juice = linea.find("apple_juice")
        cuantizador_es_blue_bowl = linea.find("blue_bowl")
        cuantizador_es_blue_lego = linea.find("blue_lego")
        cuantizador_es_blue_mug = linea.find("blue_mug")
        cuantizador_es_blue_spoon = linea.find("blue_spoon")
        cuantizador_es_chocolate_cookies = linea.find("chocolate_cookies")
        cuantizador_es_orange_juice = linea.find("orange_juice")
        cuantizador_es_orange_knife = linea.find("orange_knife")
        cuantizador_es_red_lego = linea.find("red_lego")
        cuantizador_es_red_mug = linea.find("red_mug")
        if cuantizador_es_apple_juice != -1:            
            cuantizadores[0].append(linea)
        elif cuantizador_es_blue_bowl != -1:
            cuantizadores[1].append(linea)
        elif cuantizador_es_blue_lego != -1:
            cuantizadores[2].append(linea)
        elif cuantizador_es_blue_mug != -1:
            cuantizadores[3].append(linea)
        elif cuantizador_es_blue_spoon != -1:
            cuantizadores[4].append(linea)
        elif cuantizador_es_chocolate_cookies != -1:
            cuantizadores[5].append(linea)
        elif cuantizador_es_orange_juice != -1:
            cuantizadores[6].append(linea)
        elif cuantizador_es_orange_knife != -1:
            cuantizadores[7].append(linea)
        elif cuantizador_es_red_lego != -1:
            cuantizadores[8].append(linea)
        elif cuantizador_es_red_mug != -1:
            cuantizadores[9].append(linea)                    
    archivo.close()

#A cada cadena almacenada se le quitan los caracteres innecesarios y 
#se almacenan los valores de los centroides como float en una lista
    cuantizadores_float = []
    for centroides in cuantizadores:
        aux = []
        for centroide in centroides:
            inicio = centroide.find("[")
            fin = centroide.find("]")
            valores_string = centroide[inicio+1:fin].split(',')
            valores_float = []
            for valor in valores_string:
                valores_float.append(float(valor))
            aux.append(valores_float)
        cuantizadores_float.append(aux)
    #print(valores_centroides)
    cuantizadores_f = []
    cuantizadores_f.append(cuantizadores_float[0]) #Para probar un solo cuantizador

#Se obtienen las distancias totales minimas (Di) de los pixeles de cada imagen a un centroide
#Se reconoce cada imagen dependiendo de cual sea la Di minima
    imagenes_reconocidas = []
    nombre_cuantizadores = ["apple_juice", "blue_bowl", "blue_lego", "blue_mug", "blue_spoon", 
                            "chocolate_cookies", "orange_juice", "orange_knife", "red_lego", "red_mug"]
    num_imagen = 0
    for imagen in imagenes:
        distancias_totales_minimas = []
        for cuantizador in cuantizadores_float: #cambiar a cuantizadores_float al terminar de probar un solo cuantizador
            distancia_total_minima = 0
            for pixel in imagen.imagen:
                distancias_a_centroides = []
                for centroide in cuantizador:
                    if centroide != None:
                        distancia = np.linalg.norm(pixel-centroide)
                        distancias_a_centroides.append(distancia)
                distancia_minima_a_centroides = min(distancias_a_centroides)
                distancia_total_minima = distancia_total_minima + distancia_minima_a_centroides
            distancias_totales_minimas.append(distancia_total_minima)
        
        imagen_reconocida = 0
        minima_distancias_totales_minimas = distancias_totales_minimas[0]
        for i in range(0,len(distancias_totales_minimas)):
            if distancias_totales_minimas[i] < minima_distancias_totales_minimas:
                minima_distancias_totales_minimas = distancias_totales_minimas[i]
                imagen_reconocida = i
        imagenes_reconocidas.append(imagen_reconocida)
        print("La imagen " + str(num_imagen) + " se reconocio como: " + nombre_cuantizadores[imagen_reconocida])
        num_imagen = num_imagen + 1


    #Se crea la matriz de confusion
    num_cuantizadores = 10
    matriz_confusion = np.zeros([num_imagenes_reconocidas, num_cuantizadores])
    for i in range(0, len(imagenes_reconocidas)):
        matriz_confusion[i][imagenes_reconocidas[i]] = 1
    print("\n Matriz de confusion de " + grupo_imagenes + ": ")
    print(matriz_confusion)
        


          
   
