# Noel C. F. Codella
# 4/10/2020

import sys
import cv2
import numpy as np

def main(argv):

    if len(argv) < 2:
        print 'Usage: \n\t <Output Image File> <Input Image File> \n\t\t Create empty mask of same size as input'
        return

    tmp = cv2.imread(argv[1])
        
    agg = np.zeros((tmp.shape[0],tmp.shape[1],tmp.shape[2]), tmp.dtype)

    cv2.imwrite(argv[0], agg)

    return

if __name__ == "__main__":
    main(sys.argv[1:])
