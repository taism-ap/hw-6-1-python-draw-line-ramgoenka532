# Python Draw Line
Introduction to basic computer graphics

## Drawing Points
Open the draw_points.py file in your favourite IDE and make sure it works. Try changing the created pixel, try adding more pixels, go nuts.
If using repl.it, you will encounter an error akin to "no module named 'PIL'". This can be fixed using the following steps:
1. click on "Packages" on the left - the cube that resembles a package
2. search for "pillow"
3. select Pillow v7.0.0 (not Pillow-PIL or any of the others that come up)
4. click the add symbol
5. re-run the code after Pillow has been installed


## Drawing a Line
For homework, you are asked to create a python program to draw a line using the algorithm you developed in class.
1. a program called draw_line_simple.py that should have:
  * a function that creates the image/canvas
  * a function that can take parameters for drawing the line, i.e.
  
  ```python
  def draw_line(start, finish):
    "draw a line starting at start and finishing at finish"
  ```
2. a program called draw_multiple_lines.py that should have the same as the previous, but will now draw multiple lines on the same 
