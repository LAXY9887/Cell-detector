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

Update 2022-07-20:

    Use concurrent.future.ProcessPoolExecutor to achieve multi-process loading.

Update 2022-07-21:

    ProcessPoolExecutor sucessed, need to add if __name__ == "__main__ " in the main.py !

    Ohterwise RunTimeError will happend, Error message:

    ```
    RuntimeError: 
            Attempt to start a new process before the current process
            has finished its bootstrapping phase.
            This probably means that you are on Windows and you have
            forgotten to use the proper idiom in the main module:
                if __name__ == '__main__':
                    freeze_support()
                    ...
            The "freeze_support()" line can be omitted if the program
            is not going to be frozen to produce a Windows executable.
    ```

"""

import subprocess
import os

""" Use multi-Processing """
from concurrent.futures import ProcessPoolExecutor

bfconvert = ".\\bfconvert_VSI_to_TIFF.sh"

class Bftools:

    """ Initialize , constructor """
    """ `-> None` means that this function return None """
    def __init__(self) -> None:
        pass

    """ A function to convert VSI file to TIFF by calling bfconvert """
    def bfconvert_VSI_to_TIFF(self,VSI,outDir):

        """
        Input args: 
            1. VSI: Raw image file from CellSense software.
            2. outDir: A path to output all TIFFs.
        """

        """ Check outDir, if not exist, create it."""
        if not (os.path.isdir(outDir)):
            os.mkdir(outDir)
        
        """ Get file name """
        VSI_Dir = os.path.dirname(VSI)
        VSI_file = os.path.basename(VSI)
        
        """ Run bftools by subprocess """
        args_str = [bfconvert,VSI_Dir,VSI_file,outDir]
        subprocess.Popen(args_str,shell=True)

    """ A function to convert multiple VSI to TIFF by multiProcessing """
    def bfconvert_VSI_to_TIFF_multiP(self,VSI_Dir,outDir,worker_num=10):
        """
        Input arg: A directory containing multiple VSI files.
        """

        VSI_list = list(os.listdir(VSI_Dir))

        """ To fillter out folders of the same names. """
        VSI_list_filltered = list(filter(lambda f: ".vsi" in f,VSI_list))
        VSI_list_filltered_full_path = [os.path.join(VSI_Dir,f) for f in VSI_list_filltered]

        """ Check outDir, if not exist, create it."""
        if not (os.path.isdir(outDir)):
            os.mkdir(outDir)

        """ To separate different VIS output, create new folders """
        """ os.path.splitext to remove .vsi extension in new folders' names """
        final_out_dir_list = [os.path.splitext(os.path.join(outDir,f))[0] for f in VSI_list_filltered]

        """ 
            Run Pool executor
            Usage: executor.map(function,arg1_list,arg2_list) 
            Note that this function take 2 arguments !
        """
        with ProcessPoolExecutor(max_workers=worker_num) as executor:
            executor.map(self.bfconvert_VSI_to_TIFF,VSI_list_filltered_full_path,final_out_dir_list)

if __name__ == "__main__":
    print("Convert VSI to TIFFs store to outDir.")