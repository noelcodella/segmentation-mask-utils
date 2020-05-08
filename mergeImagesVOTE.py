# Noel C. F. Codella
# python utility to merge/join imbinary masks via a VOTE operator
# Primary purpose is to merge annotation masks via an vote operation.
# 4/10/2020

import sys
import cv2
import numpy as np

def main(argv):

    if len(argv) < 2:
        print 'Usage: \n\t <rsize> <Output Binary Mask> <Input Binary Mask 1> ... <Input Binary Mask N> \n\t\t Merge binary masks by VOTE operator. Images must be same format and dimension. Output is not visible. Must use mergeImagesCMAPVOTE.'
        return

    numfiles = len(argv)
    rsize = int(argv[0])

    agg = None

    for i in range(2,numfiles):
        tmp = cv2.imread(argv[i]) 

        if (rsize > 0):
            tmp = cv2.resize(tmp, (rsize,rsize))

        tmp = tmp / 254.

        if (agg is not None):

            agg = cv2.add(agg, tmp)

        else:
            agg = tmp

    #agg = agg * (254./(numfiles-1))

    if (agg is None):
        agg = np.zeros((rsize,rsize,3), np.uint8)

    cv2.imwrite(argv[1], agg)

    return

if __name__ == "__main__":
    main(sys.argv[1:])
