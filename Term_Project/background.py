from pico2d import *
import gfw
import player


def init():
    global bg1
    bg1 = gfw.image.load('res/bg1.png')

def draw():
    global x,y

    x, y = get_canvas_width() // 2 + 960 - player.px /2, get_canvas_height() // 2
    if x > 1360:
        x = 1360
        player.px = 0
    if x < 1000:
        x -= 720

    bg1.draw(x, y)

def update():
    pass
