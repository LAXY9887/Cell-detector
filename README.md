# Cell-detector
This tool aims to detect cells in flourescent microscope data (VSI files).

# Part1 : Extract TIFFs from Cell Sense VSI files.

In the initial steps, I use `bfconvert` to handle Bio-fromat file (VSI).

Here is the bftools doc : https://docs.openmicroscopy.org/bio-formats/5.7.1/users/comlinetools/index.html

To make the conversion process more efficiently, I use `subprocess.Popen` to call shell script `bfconvert` in Python, and multiprocess is performed by `concurrent.future` module.
