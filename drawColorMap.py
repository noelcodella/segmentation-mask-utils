# Noel C. F. Codella

import numpy as np
import sys

import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt

from matplotlib.pyplot import figure
figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

def main(argv):

    if len(argv) < 3:
        print "Usage: \n\t <color map txt file> <labels txt file> <image output>"
        return

    cmap = np.loadtxt(argv[0])

    labels = {}
    with open(argv[1]) as f:
        labels = f.read().splitlines()

    numc = cmap.shape[0]

    

    for i in range(0, numc):
        plt.text(0.01,1.0-float(i)/numc, labels[i], size=5,linespacing=1.0, backgroundcolor=[cmap[i,0]/255, cmap[i,1]/255, cmap[i,2]/255])


    plt.axis('off')
    plt.tight_layout()
    plt.savefig(argv[2],dpi=300)

    return


if __name__ == "__main__":
    main(sys.argv[1:])