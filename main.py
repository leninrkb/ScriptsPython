import datag as dg

# path_in = 'D:/datasets/cuasapas_data/chaleco/nuevo_data_38/re'
# path_out = 'D:/datasets/cuasapas_data/chaleco/nuevo_data_38/aum'
imgs = ['re_img_0.jpg']

# imgs = datag.generar_imgs(imgs = imgs, path_in=path_in, path_out=path_out, write=True, generate=5, verbose=True)
# imgs = datag.generar_imgs(path_in=path_in, path_out=path_out, write=True, generate=5, verbose=True)

# img_array = dg.cv2.imread(dg.os.path.join(path_in,imgs[0]))
# print(f' shape original: {img_array.shape}')

# img_array = dg.redimensionar_img(img_array, 2, 2)
# print(f' shape nuevo: {img_array.shape}')

# img_array = dg.redimensionar_img(img_array, 5, 5, dg.cv2.INTER_LINEAR)
# print(f' shape nuevo: {img_array.shape}')
'''
# extraer sub_imagenes 
path_in = '/home/lenin/Documents/proyecto_mineros/dataset16/fotos_fondo_itca/'
path_out = '/home/lenin/Documents/proyecto_mineros/dataset16/n/'
imgs = dg.extraer_nombres_imgs(path_in)
# trabajo solo una para tomar las dimensiones que necesito
img = dg.cv2.imread(dg.os.path.join(path_in, imgs[0]))
img = dg.redimensionar_img_cuadrado(img, resize_type='min')
w = img.shape[0]
h = img.shape[1]
img_required_size = 30
m = w//img_required_size
n = h//img_required_size

print(w, h)
print(m, n)
print(len(imgs))

c=0
for name in imgs:
    img = dg.cv2.imread(dg.os.path.join(path_in, name))
    img = dg.redimensionar_img_cuadrado(img, resize_type='min')
    subimgs = dg.dividir_img(img, m, n)
    for subimg in subimgs:
        dg.guardar_img(subimg, path_out, c)
        c+=1
    break
print(f'total: {c}')
'''


# rezise a todas las p
path_in = '/home/lenin/Downloads/IMG_1234/'
path_out = '/home/lenin/Documents/proyecto_mineros/dataset16/salida/'
imgs = dg.extraer_nombres_imgs(path_in)
m=30
c=0
for img in imgs:
    new = dg.cv2.imread(dg.os.path.join(path_in, img))
    new = dg.redimensionar_img(new, m, m)
    dg.guardar_img(new, path_out, c)
    c+=1
    print(c, end=', ')

