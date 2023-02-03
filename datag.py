import albumentations as A
import cv2
import os
import matplotlib.pyplot as plt
import datetime

global TRANSFORM 
global NUM_TO_GENERATE
global WRITE
global VERBOSE
global INTERPOLACION

INTERPOLACION = cv2.INTER_NEAREST
VERBOSE = True
NUM_TO_GENERATE = 10
WRITE = False
# aumentar la complejidad de la arquitectura para obtener mas modificaciones
TRANSFORM = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(brightness_limit=0.5, contrast_limit=0.5, p=1.0),
    A.ShiftScaleRotate(shift_limit=0.09, scale_limit=0.09, rotate_limit=18)
])

# escribe la img en el path indicado, puede pasarle un count / 0 x defecto
def guardar_img(new_img, path_out, img_count=0):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    datos_img = '{}/{}_{}.jpg'.format(path_out,img_count,timestamp)
    cv2.imwrite(datos_img, new_img)
    return

# hace el aumento de una sola imagen
# img_array = img leida por opencv
def aumentar_imagen(img_array, path_out, img_count,  write=WRITE):
    new_img = TRANSFORM(image=img_array)['image']
    if write:
        guardar_img(new_img, path_out, img_count)
    return new_img

# genera imagenes nuevas a partir del path de entrada 
# lee todas las imagenes dentro del path por defecto y genera el numero indicado x cada 1 
# imgs = ['nombre','de','las','img','a','aumentar']
def generar_imgs(path_in, path_out,imgs=[],  generate=NUM_TO_GENERATE, write=WRITE, verbose=VERBOSE):
    augmented_imgs = []
    img_count = 0
    if not imgs == []:    
        for img_name in imgs:
            img_array = cv2.imread(os.path.join(path_in,img_name))
            for i in range(generate):
                img_count+=1
                new_img = aumentar_imagen(img_array, path_out, img_count, write)
                if not write: augmented_imgs.append(new_img)
    else:
        for img_name in os.listdir(path_in):
            img_array = cv2.imread(os.path.join(path_in,img_name))
            for i in range(generate):
                img_count+=1
                new_img = aumentar_imagen(img_array, path_out, img_count, write)
                if not write: augmented_imgs.append(new_img)
    if verbose:
        print('imgs generated =',img_count)
        print('augmented_imgs len =',len(augmented_imgs))
    return augmented_imgs
    

# redimensiona una imagen
# img_array = img leida por opencv
'''
cv2.INTER_NEAREST: Interpolación de vecino más cercano, es la más rápida pero también la más poco precisa.
cv2.INTER_LINEAR: Interpolación lineal, una opción intermedia en términos de velocidad y precisión.
cv2.INTER_CUBIC: Interpolación cúbica, es la más lenta pero también la más precisa.
cv2.INTER_LANCZOS4: Interpolación de Lanczos, una opción intermedia en términos de velocidad y precisión.
'''
def redimensionar_img(img_array, nuevo_ancho, nuevo_alto, interpolacion=INTERPOLACION):
    puntos_bajar = (nuevo_ancho, nuevo_alto)
    new_img = cv2.resize(img_array, puntos_bajar, interpolation = interpolacion)
    return new_img