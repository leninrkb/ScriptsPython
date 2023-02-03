from datag import genimgs

path_in = 'D:/datasets/cuasapas_data/chaleco/nuevo_data_38/re'
path_out = 'D:/datasets/cuasapas_data/chaleco/nuevo_data_38/aum'
imgs = ['re_img_0.jpg']
imgs = genimgs(imgs=imgs, path_in=path_in, path_out=path_out, write=True, generate=5, verbose=True)