# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:28:16 2022

@author: Cryptomero‧Zero

This module call bftools: bfconvert to convert VSI (Cell Sense) to TIFFs.

The channels and Z-stack were set to be output spearately.

Suggest join bftools to env path

    export PATH=$PATH:./bftools

Args: 
    1. VSI: A full-path to a single VSI file.
    2. outDir: A directory to output TIFFs of all channels and Z-stacks.

"""

import subprocess
import os

bfconvert = ".\\bftools\\bfconvert_VSI_to_TIFF.sh"

def bfconvert_VSI_to_TIFF(VSI,outDir):
    """ Check outDir, if not exist, create it."""
    if not (os.path.isdir(outDir)):
        os.mkdir(outDir)
    
    """ Get file name """
    VSI_Dir = os.path.dirname(VSI)
    VSI_file = os.path.basename(VSI)
    
    """ Run bftools by subprocess """
    args_str = [bfconvert,VSI_Dir,VSI_file,outDir]
    subprocess.run(args_str,shell=True)
    
if __name__ == "__main__":
    print("Convert VSI to TIFFs store to outDir.")