import functools

import numpy as np

def get_missing_sign(size: int, width: int=None):
    '''
    Image to show when data is not available.
    '''
    if width is None:
        width = int(size*0.03)

    layer_list = []
    for k in range(-width, width+1):
        layer = np.diag(np.ones(size-abs(k)), k=k)
        layer_list.append(layer)
    miss_img = functools.reduce(lambda x, y: np.maximum(x, y), layer_list)
    miss_img = np.maximum(miss_img, np.rot90(miss_img))
    miss_img = 1-miss_img
    return miss_img
