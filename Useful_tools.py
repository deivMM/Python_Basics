# =============================================================================
# Useful functions
# 
# round_to
# sort_list_of_fs_by_ascending_number
# 
# =============================================================================

import os
import re
import matplotlib.pyplot as plt
from math import log10, floor

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
plt.show()

# =============================================================================
lista = ['modelo_10', 'modelo_2','modelo_5','modelo_7','modelo_1',]
lista.sort(key= lambda x: int(x.strip('modelo_')))

