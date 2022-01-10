import numpy as np
import reconocimiento_patrones as rp
import procesamiento_imagen as pim
import LBG_alg as lbg

#Cambiar "nombre_cuantizador" y "ruta" segun el cuantizador que se este realizando y las imagenes que se usaran
nombre_cuantizador = "apple_juice" 
ruta = "./appleJuice" 

#Las imagenes originales estan en formato BGR

if __name__ == '__main__':
    nombres = pim.obtiene_nombres_archivos(ruta)
    print(f"Se encontraron {len(nombres)} archivos:")
    for nombre in nombres:
        print(nombre)
    imagenes = pim.procesa_imagenes(ruta, nombres, 2) #Cambiar el ultimo valor para escoger el formato de los pixeles

    pixeles_imagenes = []
    for i in range (len(imagenes)):
    #Se usa "imagen_RGB_reducida" para ahorrar tiempo al probar el programa
    #Para almacenar los centroides del cuantizador que se usara para el proyecto, es necesario
    #cambiar "np.concatenate(imagenes[i].imagen_RGB_reducida)" por "imagenes[i].imagen"
        pixeles_imagenes.append(imagenes[i].imagen)

    pixeles_imagenes = np.concatenate(pixeles_imagenes)
    valores = lbg.LBG()
    print("pix imag: ", pixeles_imagenes[0]) #Para probar que cada pixel tenga tres o nueve elementos y no hubo error al concatenar
    print("cantidad de pixeles: ", len(pixeles_imagenes)) #total de pixeles de todas las imagenes usadas

    #"hacer_regiones" se usa para que a los centroides del cuantizador se le asignen valores
    hacer_regiones = valores.cuantiza(x = pixeles_imagenes, epsilon1= 0.001, epsilon2=-0.001, e0=0.001, dist_func=None) 
    print(valores.centroides())

    #Para pasar los centroides a una lista para escribirlos correctamente en un archivo .txt:
    centroides = []
    for centroide in valores.centroides():
        aux = []
        for valor in centroide:
            aux.append(valor)
        centroides.append(aux)

    #Los centroides se guardan en un archivo .txt para usarlos despues para reconocer imagenes
    #Cambiar el nombre del archivo segun el cuantizador que se este haciendo
    archivo = open("cuantizadores_HSV.txt", "a")

    for centroide in centroides:
        archivo.write(nombre_cuantizador + " " + str(centroide) + " \n")
    archivo.close()  

"""
    correlaciones_imagenes = []
    for i in range (len(imagenes)):
        correlaciones_imagenes.append(imagenes[i].vectores_correlacion())
    correlaciones_imagenes = np.concatenate(correlaciones_imagenes)
"""
