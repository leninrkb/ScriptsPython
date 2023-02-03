import datag as dg

path_in = 'D:/datasets/cuasapas_data/chaleco/nuevo_data_38/re'
path_out = 'D:/datasets/cuasapas_data/chaleco/nuevo_data_38/aum'
imgs = ['re_img_0.jpg']

# imgs = datag.generar_imgs(imgs = imgs, path_in=path_in, path_out=path_out, write=True, generate=5, verbose=True)
# imgs = datag.generar_imgs(path_in=path_in, path_out=path_out, write=True, generate=5, verbose=True)

# img_array = dg.cv2.imread(dg.os.path.join(path_in,imgs[0]))
# print(f' shape original: {img_array.shape}')

# img_array = dg.redimensionar_img(img_array, 2, 2)
# print(f' shape nuevo: {img_array.shape}')

# img_array = dg.redimensionar_img(img_array, 5, 5, dg.cv2.INTER_LINEAR)
# print(f' shape nuevo: {img_array.shape}')
