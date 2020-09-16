Python 3.8.6rc1 (tags/v3.8.6rc1:08bd63d, Sep  7 2020, 23:10:23) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pico2d
Pico2d is prepared.
>>> pico2d
<module 'pico2d' from 'C:\\Python\\lib\\site-packages\\pico2d\\__init__.py'>
>>> pico2d.open_canvas()
>>> pico2d.close_canvas()
>>> import pico2d as p
>>> p.open_canvas()
>>> p.close_canvas()
>>> from random import randint
>>> randint(1,6)
6
>>> randint(1,6)
6
>>> randint(1,6)
3
>>> from random import randint as ri
>>> ri(1,6)
1
>>> from random import *
>>> uniform(1,2)
1.4011484134426655
>>> randrange(10,20)
17
>>> pico2d.open_canvas()
p
>>> p.close_canvas()
>>> from pico2d import*
>>> open_canvas()
close
>>> close_canvas()
>>> import os
>>> os.getcwd()
'C:\\Python'
>>> os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python38.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll']
>>> load_image('C:\Users\qoreh\OneDrive\바탕 화면\git_2DGP\수업\res')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> open_canvas()
>>> image = load_image('C:/Users/qoreh/OneDrive/바탕 화면/git_2DGP/수업/res')
cannot load C:/Users/qoreh/OneDrive/바탕 화면/git_2DGP/수업/res
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    image = load_image('C:/Users/qoreh/OneDrive/바탕 화면/git_2DGP/수업/res')
  File "C:\Python\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> image = load_image('C:\Users\qoreh\OneDrive\바탕 화면\git_2DGP\수업\res')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> image = load_image('C:/Users\qoreh\OneDrive\바탕 화면\git_2DGP\수업\res')
cannot load C:/Users\qoreh\OneDrive\바탕 화면\git_2DGP\수업es
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    image = load_image('C:/Users\qoreh\OneDrive\바탕 화면\git_2DGP\수업\res')
  File "C:\Python\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> image = load_image('C:\Python\res')
cannot load C:\Pythones
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    image = load_image('C:\Python\res')
  File "C:\Python\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> image = load_image('C:/Python/res')
cannot load C:/Python/res
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    image = load_image('C:/Python/res')
  File "C:\Python\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> os.getcwd()
'C:\\Python'
>>> os.chdir('C:/Users/qoreh/OneDrive/바탕 화면/git_2DGP/수업')
>>> os.getcwd()
'C:\\Users\\qoreh\\OneDrive\\바탕 화면\\git_2DGP\\수업'
>>> image = load_image('cat')
cannot load cat
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    image = load_image('cat')
  File "C:\Python\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> os.listdir()
['1주차', '2주차', '3주차', 'res']
>>> os.chdir('C:/Users/qoreh/OneDrive/바탕 화면/git_2DGP/수업/res')
>>> os.listdir()
['cat.jpg']
>>> image = load_image('cat.jpg')
>>> image.draw_now(400,300)
>>> 