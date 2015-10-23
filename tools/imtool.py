__author__ = 'York'
from PIL import Image
from pylab import *

#图像缩放
def imresize(im,sz):
    pil_im = Image.fromarray(uint8(im))

    return array(pil_im.resize(sz))

#灰度均衡化处理
def histeq(im,nbr_bins = 256):
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum()
    cdf = 255*cdf/cdf[-1]

    im2 = interp(im.flatten(),bins[:-1].cdf)

    return im2.reshape(im.shape),cdf
