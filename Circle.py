"""
Nombre del Proyecto: Dibujar un circulo
Fecha de asignación: 2/Febrero/2021
Fecha de entrega:    4/Febrero/2021
Modificacion
Nombre del Proyecto: Histograma
Fecha de asignación: 4/Febrero/2021
Fecha de entrega:    9/Febrero/2021 
Por:                 Eduardo Chavez Garcia 
"""

from PIL import Image, ImageDraw, ExifTags
import os

import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import cv2
import numpy as np

def Build_Circle():
    if __name__ == "__main__":
        img = Image.new('RGB', (800, 800), color='White')
        d = ImageDraw.Draw(img)
        d.ellipse((0, 0, 800, 800), fill="Black")
        img.save('Circulo.jpg')
        img = Image.open("./Circulo.jpg")
        img.show()



def graficar(datos, nombre_del_archivo):
    plt.figure(1)
    x=range(len(datos))
    plt.xticks([0, 50, 100, 150, 200, 255],[0, 50, 100, 150, 200, 255])
    plt.bar(x, datos, align='center')
    plt.title('Histograma')
    plt.xlabel('Valores de intensidad')
    plt.ylabel('Numero de pixeles')
    plt.savefig('CirculoHistograma', bbox_inches='tight')
    return None

def scalegray():
    arr_image = Image.open('Circulo.jpg')
    array_image=np.array(arr_image)
    array_zeros=np.zeros((int(array_image.shape[0]), int(array_image.shape[1])))
    for n in (range(array_image.shape[0])):
        for m in (range(array_image.shape[1])):
            R=0 
            G=0 
            B=0
            suma=0
            for j in (range(array_image.shape[2])):
                if j==0:
                    R=array_image[n,m,j]*0.3
                    suma=suma+R
                elif j==1:
                    G=array_image[n,m,j]*0.3
                    suma=suma+G
                else:
                    B=array_image[n,m,j]*0.3
                    suma=suma+B
            array_zeros[n,m]=suma
    #Reprensetando la imagen 
    cv2.imwrite('Imagen a escala de grises.jpg', array_zeros)
    variable=cv2.imread('imgray.jpg')
    cv2.imshow('I M A G E',variable)
    cv2.waitKey(0)

def ConvertirImagen(lista):
    cv2.imwrite('Binarizada.jpg', lista)
    variable = cv2.imread('Binarizada.jpg')
    cv2.imshow('I M A G E', variable)
    cv2.waitKey(0)

def ConvertirVetor(direccion):
    imagen =Image.open(direccion)
    array_image=np.array(imagen)
    vector=array_image.ravel()
    return vector

def DibujarHistograma(lista):
    plt.hist(lista,100,[0,100])
    plt.show()

def ConvertirMatriz(direccion):
    imagen=Image.open(direccion)
    array_image=np.array(imagen)
    return array_image

def binarizarimagen(umbral,matriz):
    for n in (range(matriz.shape[0])):
        for m in (range(matriz.shape[1])):
            if umbral <matriz[n,m]:
                matriz[n,m]=0
            else:
                matriz[n,m]=255
    return matriz






menu="""
    Menu
    1. Crear Circulo
    2. Obtener Histograma
    3. Imagen a escala de grises
    4. Binarizar imagen (La imagen debe estar en escala de grises)
    5. Salir
    """
op=None
while op!=5:
    os.system('cls')
    print(menu)

    op=int(input('Selecciona una opcion: '))

    if op==1:
        Build_Circle()
        print('La imagen se creo con el nombre "Circulo.jpg" ')
        os.system('pause')
    elif op==2:
        foto=Image.open("./Circulo.jpg")
        #si la imagen es a color la convertimos a escala de grise
        if foto.mode != 'L':
            foto=foto.convert('L')
        histograma=foto.histogram()
        graficar(histograma, "./Circulo.jpg")
    elif op==3:
        scalegray()
    elif op==4:
        direccion='Imagen a escala de grises.jpg'
        lista=ConvertirVetor(direccion)
        #DibujarHistograma(lista)
        matriz=ConvertirMatriz(direccion)
        matriz1=binarizarimagen(125,matriz)
        ConvertirImagen(matriz1)
    elif op==5:
        print('Fue un placer atenderle')
