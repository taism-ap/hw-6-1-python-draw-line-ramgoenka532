# Drawing a Line in Python
An introduction to (very) basic computer graphics - how hard can if be to draw a line?

## Drawing Points
Create a file called draw_points.py, using the code below as a base.
```python
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
```
Open the draw_points.py file in your favourite IDE and make sure it works. Try changing the created pixel, try adding more pixels, go nuts.

If using repl.it, you will encounter an error akin to "no module named 'PIL'". This can be fixed using the following steps:
1. click on "Packages" on the left - the cube that resembles a package
2. search for "pillow"
3. select Pillow v7.0.0 (not Pillow-PIL or any of the others that come up)
4. click the add symbol
5. re-run the code after Pillow has been installed

If you are using an IDE on your computer, you need some way to install new modules. Personally, I use pip - let's talk.


## Drawing a Line
For homework, you are asked to create a python program to draw a line using the algorithm you developed in class. The progression will be as follows:
- [ ] A program called draw_horizontal_line.py which will draw a single horizontal line. This will be the basis of the rest of the programs; it should have:
   * a function that creates the image/canvas
   * a function that can take parameters for drawing the line, i.e.
  
        ```python
        def draw_line(start, finish):
          "draw a line starting at start and finishing at finish"
        ```
   * the draw line function called to draw a horizontal line
  
- [ ] A program called draw_horizontal_lines.py which will draw multiple random horizontal lines using your algorithm. An example of how to use randint in python is shown below.

    ```python
    import random as rand
    # the code below will generate a random integer between 0 and 10
    x = rand.randint(0,10)
    print(x)
    ```
- [ ] A program called draw_multiple_lines.py which can draw multiple non-horizontal lines using your algorithm.

- [ ] A program called draw_thick_line.py which can draw a non-horizontal line of a parameterized thickness.
