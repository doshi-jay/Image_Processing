"""Low-pass and high-pass filter an image.

"""

import os
import sys
import numpy
from numpy import fft
import pylab
from scipy import ndimage
import matplotlib.image as image
import matplotlib.colors as colors
import IPython
pylab.matplotlib.interactive(True)

#-------------------------------------------------------------------------------------------------------------
def makeRMap(x, y, data):
    """Returns an array that gives radial distance to given coords.
    
    """
    
    xPix=numpy.array([numpy.arange(0, data.shape[1], dtype=float)]*data.shape[0])-x
    yPix=(numpy.array([numpy.arange(0, data.shape[0], dtype=float)]*data.shape[1])-y).transpose()
    rPix=numpy.sqrt(xPix**2+yPix**2)

    return rPix

#-------------------------------------------------------------------------------------------------------------
def calcMagsAndPhases(farr):
    """Calculates magnitudes and phases of FFT'ed array.
    
    """
    
    mags=abs(farr)
    phases=numpy.arctan2(farr.imag, farr.real)
    
    return mags, phases

#-------------------------------------------------------------------------------------------------------------
def loadImage(fileName):
    """Loads in an image, converts it to a greyscale numpy array for us to play with.
    
    """
    
    img=image.imread(fileName)
    hsv=colors.rgb_to_hsv(img)
    gray=hsv[:, :, 2]

    return gray

#-------------------------------------------------------------------------------------------------------------
def saveImage(arr, fileName, logScaling = False):
    """Save image.
    
    """
    pylab.figure(figsize=(4, 4))
    pylab.axes([0, 0, 1, 1])
    pylab.imshow(arr, cmap=pylab.get_cmap('gray'))
    # if logScaling == False:
    #     pylab.imshow(arr, cmap=pylab.get_cmap('gray'))
    # else:
    #     pylab.imshow(arr, cmap=pylab.get_cmap('gray'), norm=colors.LogNorm(vmin=1e-2, vmax=arr.max()))
    pylab.savefig(fileName)
    
#-------------------------------------------------------------------------------------------------------------
# Main

# Load images
arr=loadImage("images/jay.jpg")
#arr=loadImage("images/Bird.jpg")
saveImage(arr, "input.png")

# FFT
farr=fft.fft2(arr)

# Low-pass filter: mask out high frequencies, save filtered image and masked mags
mags, phases=calcMagsAndPhases(farr)
maskRadius=20
rMap=makeRMap(mags.shape[0]/2, mags.shape[1]/2, mags)
mask=numpy.array(numpy.less(rMap, maskRadius), dtype = float)
saveImage(mask, "mask-lowpass.png")
mags=mags*fft.fftshift(mask)
saveImage(fft.fftshift(mags), "mags-lowpass.png", logScaling = True)

f=numpy.zeros(farr.shape, dtype = numpy.complex)
f.real=mags*numpy.cos(phases)
f.imag=mags*numpy.sin(phases)
ifarr=fft.ifft2(f).real
saveImage(ifarr, "lowpass.png")

# High-pass filter: mask out low frequencies, save filtered image and masked mags
mags, phases=calcMagsAndPhases(farr)
maskRadius=20
rMap=makeRMap(mags.shape[0]/2, mags.shape[1]/2, mags)
mask=numpy.array(numpy.greater(rMap, maskRadius), dtype = float)
saveImage(mask, "mask-highpass.png")
mags=mags*fft.fftshift(mask)
saveImage(fft.fftshift(mags), "mags-highpass.png", logScaling = True)

f=numpy.zeros(farr.shape, dtype = numpy.complex)
f.real=mags*numpy.cos(phases)
f.imag=mags*numpy.sin(phases)
ifarr=fft.ifft2(f).real
saveImage(ifarr, "highpass.png")

IPython.embed()
# sys.exit()
