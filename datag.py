import albumentations as A
import cv2
import os
import matplotlib.pyplot as plt
import datetime

# A.Flip(), voltea la img en vertical
# A.Transpose(), intercambia las dimensiones de la imagen, es decir, 
# cambia la orientación de la imagen 90 grados.

global TRANSFORM 
global NUM_TO_GENERATE
global WRITE
global VERBOSE

VERBOSE = True
NUM_TO_GENERATE = 10
WRITE = False
# aumentar la complejidad de la arquitectura para obtener mas modificaciones
TRANSFORM = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(brightness_limit=0.5, contrast_limit=0.5, p=1.0),
    A.ShiftScaleRotate(shift_limit=0.09, scale_limit=0.09, rotate_limit=18)
])


# hace el aumento de una sola imagen
def aumentar_imagen(img_array, path_out, img_count,  write=WRITE):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_img = TRANSFORM(image=img_array)['image']
    if write:
        datos_img = '{}/{}_{}.jpg'.format(path_out,img_count,timestamp)
        cv2.imwrite(datos_img, new_img)
    return new_img


# genera imagenes nuevas a partir del path de entrada 
# lee todas las imagenes dentro del path por defecto y genera el numero indicado x cada 1 
def genimgs(path_in, path_out,imgs=[],  generate=NUM_TO_GENERATE, write=WRITE, verbose=VERBOSE):
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
    
