# Noel C. F. Codella
# python utility to merge/join multiple binary masks into a single color coded mask
# Combine multiple binary masks into a single color mask
# 4/24/2020

import sys
import cv2
import numpy as np

def main(argv):

    if len(argv) < 2:
        print 'Usage: \n\t <Output Image File> <Color Map File> <Resize> <Input Binary Mask 1> ... <Input Binary Mask N> \n\t\t Merge multiple binary masks into single color coded mask. Images must be same dimension. \nAssumes classes mutually exclusive. \nColor map is simply "R G B" per row. One row per class. Same row order as input. \nResize < 0 prevents resizing'
        return

    numfiles = len(argv)

    # threshold of votes , hardcode for now
    th = 0

    # Color map file is simply a file with **RGB** values on each line
    # separated by space
    cmap = np.loadtxt(argv[1])
    numc = cmap.shape[0]

    # optional resize parameter
    rsize = int(argv[2])

    # get the shape of the first image
    imdim = (cv2.imread(argv[3])).shape

    # if resize was set, override
    if (rsize > 0):
        imdim = (rsize, rsize)

    # create the merged color map mask
    agg = np.zeros((imdim[0],imdim[1],3), np.uint8)
    vote = np.zeros((imdim[0],imdim[1]), np.uint8)

    # minimum threshold  of votes
    vote = vote + th

    # iterate over all the binary masks
    for i in range(3,numfiles):
        tmp = cv2.imread(argv[i])

        # if resize requested, perform it
        if (rsize > 0):
            tmp = cv2.resize(tmp, imdim)

        # **BGR** pixel color order
        c = np.flip(cmap[i-3])

        for u in range(0,imdim[0]):
            for v in range(0, imdim[1]):
                # if mask pixel, change the aggregate to the current color
                if (tmp[u,v,2] > vote[u,v]):
                    agg[u,v,:] = c
                    vote[u,v] = tmp[u,v,2]

    cv2.imwrite(argv[0], agg)

    return

if __name__ == "__main__":
    main(sys.argv[1:])
