# Noel C. F. Codella
# python utility to merge/join imbinary masks via a MAX operator
# Primary purpose is to merge annotation masks via an OR operation.
# 4/10/2020

import sys
import cv2


def main(argv):

    if len(argv) < 2:
        print 'Usage: \n\t <Output Binary Mask> <Input Binary Mask 1> ... <Input Binary Mask N> \n\t\t Merge binary masks by MAX operator. Images must be same format and dimension.'
        return

    numfiles = len(argv)

    agg = None

    for i in range(1,numfiles):
        tmp = cv2.imread(argv[i])

        if (agg is not None):

            agg = cv2.max(agg, tmp)

        else:
            agg = tmp

    cv2.imwrite(argv[0], agg)

    return

if __name__ == "__main__":
    main(sys.argv[1:])
