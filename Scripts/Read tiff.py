# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 17:44:00 2022

@author: Cryptomero‧Zero

Image loading by cv2 is too slow, PIL image load faster

"""
#%%

""" Imports"""

import torch
from PIL import Image 
import os
import numpy as np
""" This is for solving image display bug """
os.environ["KMP_DUPLICATE_LIB_OK"]="True"

# Run multi-thread loading
from concurrent.futures import ThreadPoolExecutor

# test dir
img_path = '../Test_TIFF_Img/'

#%%

""" Loading images """

def Load_Img_PIL(img):
    Im = Image.open(img)
    Img_array = np.array(Im)
    return Img_array

def Load_tiff_series_as_tensor(tiff_folder):
    TIFF_list = os.listdir(tiff_folder)
    TIFFs = [os.path.join(tiff_folder,f) for f in TIFF_list]
    TIFF_tensor = torch.tensor([Load_Img_PIL(t) for t in TIFFs])
    return TIFF_tensor

""" Load batches of image multi-thread """
def Load_batch_TIFF_as_tensor(batch_folder):
    batches = [os.path.join(batch_folder,b) for b in os.listdir(batch_folder)]
    with ThreadPoolExecutor(max_workers=32) as executor:
        TIFF_batches = list(executor.map(Load_tiff_series_as_tensor, batches))
    # tensor.stack() merged TIFF_batches into single tensor.
    # expect to have the same TIFF number each batch!
    TIFF_batches_tensor = torch.stack(TIFF_batches)
    return TIFF_batches_tensor

batches = Load_batch_TIFF_as_tensor(img_path)

#%%
#import matplotlib.pyplot as plt

#plt.imshow(image_zStack[14])
