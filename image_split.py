import numpy as np
import matplotlib
import skimage as si
import sys

from skimage.io import imread
from skimage.io import imsave
from os.path import abspath
from os.path import basename
from os.path import dirname
from os.path import isfile

if len(sys.argv)<2:
    print("Not enough arguments. Specify filenames")
    sys.exit()

for p in sys.argv[1:]:

    path = abspath(p)
    if not isfile(path):
        print("'%s' is not an existing file" % path)
        continue

    image = imread(path)

    red = image[:,:,0]
    green = image[:,:,1]
    blue = image[:,:,2]
    blank = np.zeros(red.shape, dtype=np.uint8)

    red = np.dstack((red, blank, blank))
    green = np.dstack((blank, green, blank))
    blue = np.dstack((blank, blank, blue))

    imsave(dirname(path)+'/r_'+basename(path), red)
    imsave(dirname(path)+'/g_'+basename(path), green)
    imsave(dirname(path)+'/b_'+basename(path), blue)