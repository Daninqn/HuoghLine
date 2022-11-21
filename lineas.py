import cv2
import numpy as np

img = cv2.imread('ejemplo8.jpg')

#Convetimos la imagen en gris

imggris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Funcion canny() para limpiar la imagen y dejar bordes

imgfiltrada = cv2.Canny(imggris,100,250,apertureSize=3)

#funcion HoughLines() devuelve los pares ro y theta de la imagen

lineas = cv2.HoughLines(imgfiltrada, 1, np.pi / 180,200)

#la funcion devuelve un vector con los pares de Ro y theta entonces los recorremos

for linea in lineas:

    #Pasamos nuevamente de los puntos (rho, theta) a (x,y) parar poder dibujarlo en la imagen
    rho , theta = linea[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho

    x1 = int (x0 + 1000 * (-b))

    y1 = int (y0 + 1000 * (a))

    x2 = int (x0 - 1000 * (-b))

    y2 = int (y0 - 1000 * (a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('imagen',img)
k=cv2.waitKey(0)
cv2.destroyAllWindows()