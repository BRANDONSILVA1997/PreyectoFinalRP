import imagen
import os

def nombres_archivos(path, ext):
    archivos = os.listdir(path)
    return [x for x in archivos if x.endswith(ext)]

#El programa que invoque esta funcion otorga una ruta por defecto, si no, se puede introducir una.
def obtiene_nombres_archivos(ruta):
    archivos_finales = set()
    while True:
        sel = input("¿Buscar archivos en la ruta por defecto? [S/n]: ")
        ruta = ruta 
        if sel == 'n' or sel == 'N':
            ruta = input("Escribe la ruta: ")
        
        ext = input("extensión de archivo: ")
        
        nombres = nombres_archivos(ruta, ext)
        print(f"Se encontraron {len(nombres)} archivos con extensión {ext}:")
        for nombre in nombres:
            print(nombre)
            
        sel = input("Añadir archivos? [S/n]: ")
        if sel == 'n' or sel == 'N':
            continue
    
        archivos_finales.update(nombres)
    
        sel = input("Agregar mas archivos? [s/N]: ")
        if not (sel == 'S' or sel == 's'):
            return archivos_finales


def procesa_imagenes(ruta, nombre_archivos, tipo_imagen):
    imagenes = []
    for nombre in nombre_archivos:
        imagenes.append(imagen.Imagen(ruta + "/" + nombre, tipo_imagen))
        
    return imagenes

