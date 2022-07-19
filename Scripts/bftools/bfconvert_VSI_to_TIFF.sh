#!/usr/bin/bash
inputDir=$1
inFile=$2
outDir=$3
bfconvert -overwrite ${inputDir}/${inFile} ${outDir}/${inFile}.Channel%c.Z%z.tiff