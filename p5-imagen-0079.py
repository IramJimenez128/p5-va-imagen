import cv2
# Leer la imagen con cv2 = computer vision.
img = cv2.imread('kirby.jpg')
# Determinar el tipo de imagen numpy.ndarray.
print(type(img))
# Mostrar pixeles 450, 236, 3
print(img.shape)
#Mostrando imagen ventana barra de titulo Kirby 0079
cv2.imshow('Kirby 0079', img)
## Tiempo de espera.
cv2.waitKey(0)
# Destruir todas la ventanas.
cv2.destroyAllWindows()

