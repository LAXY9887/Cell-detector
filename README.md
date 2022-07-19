# Cell-detector
This tool aims to detect cells in flourescent microscope data (VSI files).

# Part1 : Extract TIFFs from Cell Sense VSI files.

In the initial steps, I use `bfconvert` to handle Bio-fromat file (VSI).

Here is the bftools doc : https://docs.openmicroscopy.org/bio-formats/5.7.1/users/comlinetools/index.html

To make the conversion process more efficiently, I use `subprocess.Popen` to call shell script `bfconvert` in Python, and multiprocess is performed by `concurrent.future` module.

### Usage of bfconvert:

`bfconvert -overwrite input.vsi output.Channel%c.Z%z.tiff`

This line extract from `input.vsi` and output each `Channels` with `%c` as channel index; each `Z-stacks` with `%z` as Z index.

```
For example, a VSI file can be convert into: 
  
  output.Channel**0~N**.Z**0~n**.tiff 
  
  In total, there will be N * n TIFF images output.
```

By doing this conversion, I can separate different flourescent channels and Z-stacks, and pixel information can be futher summaried from these TIFFs. This conversion process is done by `bftools_VSI_to_TIFF.py`, in this script, VSI file directory and file name are taken and pass into `bfconvert_VSI_to_TIFF.sh` and call `bfconvert`.

## 2022-07-19 Debug

The reason why I didn't call `bfconvert` is that bugs happends upon subprocess handel `%c` or `%z` in the args* list, which is essential to separate Channel and Z-stacks by `bfconvert`. Therefore, I write the expression in a separate shell script `bfconvert_VSI_to_TIFF.sh` to avoid passing `%c` or `%z` to subprocess.

## 2022-07-19 Next plane

Next step is to obtain pixel values and process the image to tensor, preparing for model training dataLoader.
