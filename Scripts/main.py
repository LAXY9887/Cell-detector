# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:45:19 2022

@author: Cryptomero‧Zero

"""

from bftools_VSI_to_TIFF import bfconvert_VSI_to_TIFF

VSI = "D:/Github-repository/Cell-detector/Testing/VSI/PLA-RNH_01.vsi"
outDir = "D:/Github-repository/Cell-detector/Testing/TIFFs/TEST1"

bfconvert_VSI_to_TIFF(VSI,outDir)