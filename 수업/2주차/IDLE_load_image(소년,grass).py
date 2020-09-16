Python 3.8.6rc1 (tags/v3.8.6rc1:08bd63d, Sep  7 2020, 23:10:23) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pico2d import *
Pico2d is prepared.
>>> open_canvas()
>>> import os
>>> os.getcwd()
'C:\\Python'
>>> os.chdir('/수업/res')
>>> os.listdir()
['animation_sheet.png', 'cat.jpg', 'character.png', 'grass.png', 'run_animation.png']
>>> image = load_image('character.png')
>>> image.draw_now(300,200)
>>> image.draw_now(400,300)
>>> for x in range(100,701,100):
	image.draw_now(x,500)

	
>>> image = load_image('character.png')
>>> for x in range(100,701,100):
	image.draw_now(x,500)

	
>>> image.draw_now(400,300)
>>> 
>>> clear_canvas_now()
>>> 
>>> claer_canvas_now()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    claer_canvas_now()
NameError: name 'claer_canvas_now' is not defined
>>> clear_canvas_now()
>>> for y in range(100,501,80):
	for x in range(100,701,35):
		image.draw_now(x,y)

		
>>> clear_canvas_now()
>>> for y in range(100,501,60):
	for x in range(100,701,25):
		image.draw_now(x,y)

		
>>> clear_canvas_now()
>>> for y in range(100,501,50):
	for x in range(100,701,35):
		image.draw_now(x,y)

		
>>> clear_canvas_now()
>>> 
>>> os.getcwd()
'C:\\Users\\qoreh\\OneDrive\\바탕 화면\\git_2DGP\\수업\\res'
>>> grass = load_image('grass.png')
>>> grass.draw_now(400,90)
>>> clear_canvas_now()
>>> grass.draw_now(400,30)
>>> close_canvas()
>>> 