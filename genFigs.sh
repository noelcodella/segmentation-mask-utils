#!/bin/bash

# A simple script to append an original image against the ground truth
# and model predictions for visual comparison. Takes as input 3 file
# lists as text files (original images, gt images, and predication
# masks), followed by an output folder. Results stored in the output
# folder according to the naming convention of the original images.
# All file lists should be in consistent order.

IFS=$'\n'

if [ $# -lt 4 ]
then
    echo "Usage: $0 <orig list> <gt list> <pred list> <output folder>"
    exit 1
fi

origl="$1"
gtl="$2"
predl="$3"
outf="$4"

mkdir -p $outf

tasks="$outf/tasks.txt"

cat $origl | sort > $outf/source.txt
cat $gtl | sort > $outf/gt.txt
cat $predl | sort > $outf/pred.txt

paste $outf/source.txt $outf/gt.txt $outf/pred.txt > $tasks

for line in `cat $tasks`
do

    orig="`echo $line | awk -F'\t' '{print $1}'`"
    gt="`echo $line | awk -F'\t' '{print $2}'`"
    pred="`echo $line | awk -F'\t' '{print $3}'`"
    ofile="$outf/`echo $orig | sed 's/.*\///g'`"

    convert $orig $gt $pred -resize 512x512! -quality 100 +append $ofile

    echo "Done $orig"

done
