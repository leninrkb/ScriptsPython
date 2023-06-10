import albumentations as A
import cv2
import os
import datetime

global TRANSFORM
global NUM_TO_GENERATE
global WRITE
global VERBOSE
global INTERPOLACION
global RESIZE_TYPE
global MANTENER_ASPECTO

MANTENER_ASPECTO = True
RESIZE_TYPE = 'min'
INTERPOLACION = cv2.INTER_NEAREST
VERBOSE = True
NUM_TO_GENERATE = 10
WRITE = False

# aumentar la complejidad de la arquitectura para obtener mas modificaciones
TRANSFORM = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(brightness_limit=0.09, contrast_limit=0.09, p=0.5),
    A.ShiftScaleRotate(shift_limit=0.1, scale_limit=0.1, rotate_limit=15)
])


def guardar_img(img_array, path_out, num=0):
    """
    img_array = img leida por cv2\n
    path_out = dir de salida\n
    num = valor para numerar la img\n
    guarda la imagen en el path indicado,
    el nombre esta dado por el valor (en caso de pasarlo como parametro),
    y la fecha actual del sistema junto con el tiempo\n
    salida en formato jpg
    """
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        datos_img = '{}/{}_{}.jpg'.format(path_out, num, timestamp)
        cv2.imwrite(datos_img, img_array)
    except Exception as e:
        print(f'error en guardar_img: {e}')
    return


# hace el aumento de una sola imagen
# img_array = img leida por opencv
def aumentar_imagen(img_array, path_out, img_count, write=WRITE):
    new_img = TRANSFORM(image=img_array)['image']
    if write:
        guardar_img(new_img, path_out, img_count)
    return new_img


# genera imagenes nuevas a partir del path de entrada
# lee todas las imagenes dentro del path por defecto y genera el numero indicado x cada 1 
# imgs = ['nombre','de','las','img','a','aumentar']
def generar_imgs(path_in, path_out, imgs=None, generate=NUM_TO_GENERATE, write=WRITE, verbose=VERBOSE):
    if imgs is None:
        imgs = []
    augmented_imgs = []
    img_count = 0
    if not imgs == []:
        for img_name in imgs:
            img_array = cv2.imread(os.path.join(path_in, img_name))
            for i in range(generate):
                img_count += 1
                new_img = aumentar_imagen(img_array, path_out, img_count, write)
                if not write:
                    augmented_imgs.append(new_img)
    else:
        for img_name in os.listdir(path_in):
            img_array = cv2.imread(os.path.join(path_in, img_name))
            for i in range(generate):
                img_count += 1
                new_img = aumentar_imagen(img_array, path_out, img_count, write)
                if not write:
                    augmented_imgs.append(new_img)

    if verbose:
        print('imgs generated =', img_count)
        print('augmented_imgs len =', len(augmented_imgs))
    return augmented_imgs


# redimensiona una imagen
# img_array = img leida por opencv
'''
cv2.INTER_NEAREST: Interpolación de vecino más cercano, es la más rápida pero también la más poco precisa.
cv2.INTER_LINEAR: Interpolación lineal, una opción intermedia en términos de velocidad y precisión.
cv2.INTER_CUBIC: Interpolación cúbica, es la más lenta pero también la más precisa.
cv2.INTER_LANCZOS4: Interpolación de Lanczos, una opción intermedia en términos de velocidad y precisión.
'''


def redimensionar_img(img_array, nuevo_ancho=-1, nuevo_alto=-1, interpolacion=INTERPOLACION,
                      mantener_aspecto=MANTENER_ASPECTO, puntos_bajar=0):
    new_img = None
    try:
        if mantener_aspecto:
            size = img_array.shape
            w = size[1]
            h = size[0]
            nuevo_alto = h - puntos_bajar
            nuevo_ancho = w - puntos_bajar
        if nuevo_ancho == -1 or nuevo_alto == -1:
            return
        puntos_bajar = (nuevo_ancho, nuevo_alto)
        new_img = cv2.resize(img_array, puntos_bajar, interpolation=interpolacion)
    except Exception as e:
        print(f'error en redimensionar_img: {e}')
    return new_img


def redimensionar_img_cuadrado(img_array, resize_type=RESIZE_TYPE):
    w = img_array.shape[0]
    h = img_array.shape[1]
    if resize_type == 'min':
        if w < h:
            newimg = redimensionar_img(img_array, w, w)
        else:
            newimg = redimensionar_img(img_array, h, h)
    elif resize_type == 'max':
        if w > h:
            newimg = redimensionar_img(img_array, w, w)
        else:
            newimg = redimensionar_img(img_array, h, h)
    else:
        newimg = img_array
    return newimg


# dada una img se extraen de ella tantas subimg como es especifique m x n
# retorna una vector con todas las subimg
def dividir_img(img_array, n_filas, n_column):
    img_base = img_array
    sub_imgs = []
    height, width, channels = img_array.shape
    for ih in range(n_column):
        for iw in range(n_filas):
            x = width // n_filas * iw
            y = height // n_column * ih
            h = (height // n_column)
            w = (width // n_filas)
            y_end = int(y + h)
            x_end = int(x + w)
            temporal = img_base[y:y_end, x:x_end]
            sub_imgs.append(temporal)
            img_base = img_array
    return sub_imgs


# dada una ruta se extrae los nombres de todos los archivos como un vector
def extraer_nombres(path_in, negative=None):
    if negative is None:
        negative = []
    nombres = []
    for img_name in os.listdir(path_in):
        if img_name in negative:
            continue
        nombres.append(img_name)
    return nombres
