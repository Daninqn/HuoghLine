import cv2
import numpy as np

img = cv2.imread('ejemplo7.png')

imgsalida = img.copy()
#Convetimos la imagen en gris

imggris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Funcion canny() para limpiar la imagen y dejar bordes

circulos = cv2.HoughCircles(imggris,cv2.HOUGH_GRADIENT, 1, 300, param1=90, param2=50, minRadius=0,maxRadius=0)

circulosDetectados = np.uint16(np.around(circulos))

for (x,y,r) in circulosDetectados[0,:]:
    
    cv2.circle(imgsalida, (x,y),r,(0,255,0),3)
    
    cv2.circle(imgsalida,(x,y),2,(0,255,255),3)

cv2.imshow('detected circles',imgsalida)
cv2.waitKey(0)
cv2.destroyAllWindows()