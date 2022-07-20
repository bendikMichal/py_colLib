# py_colLib
Small collision detection library for pygame

# Installation
* make sure you have **python** and **pygame** installed
* download py_colLib
* place **"colLib.py"** in directory where your file which requires this library is located
* import by **"import colLib"**

# Documentation
* Currently only two functions are available:
* **_"collideCircle(circle1, circle2)"_** returns boolean based on whether the two circles collide
* **_"colCircleRect(circle, pygame.Rect)"_** returns boolean based on whether the circle and rect collide
## **_IMPORTAINT !!!_**
* the rects must be **_"pygame.Rect"_**
* the circle must be a list : **_"[x, y, radius]"_**
