from pico2d import *
import gfw
import player

def init():
    global bg1
    bg1 = gfw.image.load('res/bg1.png')

def draw():
    x, y = get_canvas_width() // 2 + 960, get_canvas_height() // 2
    bg1.draw(x - player.px * 2 , y)


def update():
    pass


