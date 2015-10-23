from PIL import Image

from pylab import *


im = array(Image.open('e:/test.jpg'))
imshow(im)

x = [100,100,400,400]
y = [200,500,200,500]

plot(x,y,'ro--')
plot(x[:4],y[:4])
axis('off')
title('Plotting:"test.jpg"')
show()