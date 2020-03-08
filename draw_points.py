#import Pillow (fork of PIL - python image library) to do image stuff
from PIL import Image

#create a new image 100 x 100 pixels in size. The "1" is the mode for the image, in this case black or white
img = Image.new("1",[100,100])

#load the image into memory to make changes to it
pixels = img.load()

#adds a white pixel at point (50,50) - note, (0,0) is in the upper left hand corner of the image (as it should be)
pixels[50,50] = (1)

#saven the image as a .png file and then close the image

img.save('pixels.png')
img.close()
