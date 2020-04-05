#import Pillow (fork of PIL - python image library) to do image stuff
from PIL import Image

#create a new image 100 x 100 pixels in size. The "1" is the mode for the image, in this case black or white
img = Image.new("1",[100,100])

#load the image into memory to make changes to it
pixels = img.load()

#adds a white pixel at point (50,50) - note, (0,0) is in the upper left hand corner of the image (as it should be)
pixels[50,50] = (1)


img.save('pixels.png')
img.close()

def draw_line(start, finish):
  "draw a line starting at start and finishing at finish using iteration"
  
  
#input the cordinates of the initial point of the line
xi = int(input("x cordinate of starting position"))
yi = int(input("y cordinate of starting position"))

#input the cordinates of the line's end point 
xf = int(input("x cordinate of ending position"))
yf = int(input("y cordinate of ending position"))

if xi != xf
  xi > xf
  xf = xi - 1 
  elif xi < xf 
  xf = xi + 1

if yi != yf 
  yi > yf 
  yf = yi -1 
 elif yi < yf 
 yf = yi + 1

for i in range (xi,yi - xf,yf)
 
img.save ("horizontal line.png")
img.close() 

