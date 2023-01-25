# =============================================================================
# Useful functions
# 
# round_to
# sort_list_of_fs_by_ascending_number
# save_figs_as_pdf
# save_imgs_as_pdf
# 
# =============================================================================

import os
import re
import matplotlib.pyplot as plt
from PIL import Image
from math import log10, floor
from matplotlib.backends.backend_pdf import PdfPages

def round_to(num,n):
    '''
    Rounding a number to n significant digits
    '''
    return round(num, n - int(floor(log10(abs(num)))) - 1)

def sort_list_of_fs_by_ascending_number(list_of_fs):
    '''
    E.g.: ['Model_10.inp','Model_1.inp'] ---> ['Model_1.inp','Model_10.inp']
    '''
    list_of_fs.sort(key=lambda el:int(re.search('\d+',el).group()))

def save_figs_as_pdf(path, f_list):
    '''
    This function generates a pdf with a given figure list.
    ---
    path = path where the pdf is to be saved 
    f_list = figure list
    '''
    with PdfPages(path) as pdf:
        for f in f_list:
            pdf.savefig(f)

def save_imgs_as_pdf(pdf_name = None, path = '.', r_pattern = 'png', remove_imgs = False):
    '''
    This function generates a pdf with the images contained in the folder.
    ---
    pdf_name = Name of the pdf to be saved with
    path = path in which the images are contained 
    r_pattern = regex pattern of the images 
    remove_imgs = [T/F]
    '''
    if not pdf_name: pdf_name = path.split('/')[-1]
    img_list = [f for f in os.listdir(path) if re.search(r_pattern, f)]
    sort_list_of_fs_by_ascending_number(img_list)
    if not img_list:
        print('There is no image within the path with this pattern')
        return
    imgs = [Image.open(f'{path}/{f}').convert('RGB') for f in img_list]
    imgs[0].save(f'{path}/{pdf_name}.pdf', 'PDF' ,resolution=100.0, save_all=True, append_images=imgs[1:])
    if remove_imgs:[os.remove(f'{path}/{f}') for f in img_list]

# =============================================================================

f_list = []

for i in range(10):
    f, ax = plt.subplots(figsize=(10,10))
    ax.plot([0,1],[0,i])
    ax.set_ylim([-2,12])
    plt.title(f'Grafico_{i+1}')
    f_list.append(f)
    plt.savefig(f'Imagen_{i+1}.png')

save_figs_as_pdf('Graficas_desde_matplotlib.pdf', f_list)
save_imgs_as_pdf('Graficas_desde_imagenes.pdf', remove_imgs = True)

# =============================================================================

print(round_to(465465, 2))
print(round_to(465465.7987134413, 10))

# =============================================================================

list_of_fs = ['Model_10.inp','Model_1.inp','Model_2.inp']
sort_list_of_fs_by_ascending_number(list_of_fs)
print(list_of_fs)

# =============================================================================
# Filtros
lista = ['prueba1','prueba2','prueba3','prueba4','prueba']
filtro = list(filter(re.compile('prueba\d').search, lista))
    
filtro2 = [l for l in lista if re.search('prueba[1|3]',l)]
print(filtro2)
filtro2 = [l for l in lista if re.search('prueba[2-4]',l)]
print(filtro2)

# =============================================================================

f, ax = plt.subplots()
ax.plot([0,1,2,3,4],[0,10,12,15,16])
ax.axvspan(0, 1, color='lightblue',alpha=.3)
ax.axvspan(2,3, color='lightgrey',alpha=.3)
ax.axhspan(2,4, color='lightgreen',alpha=.3)
plt.show()

# =============================================================================
lista = ['modelo_10', 'modelo_2','modelo_5','modelo_7','modelo_1',]
lista.sort(key= lambda x: int(x.strip('modelo_')))

