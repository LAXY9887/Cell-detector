# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:45:19 2022

@author: Cryptomero‧Zero

This is the main function that does everything.

"""

from bftools_VSI_to_TIFF import Bftools

VSI_Dir = "D:/Github-repository/Cell-detector/Testing/VSI_02"
outDir = "D:/Github-repository/Cell-detector/Testing/TIFFs/TEST3"

if __name__ == '__main__':
    bftools = Bftools()
    bftools.bfconvert_VSI_to_TIFF_multiP(VSI_Dir,outDir)