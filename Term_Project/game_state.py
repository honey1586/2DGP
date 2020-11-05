import gfw
from pico2d import *
from background import *
import gobj


canvas_width = 800
canvas_height = 600

def enter():
    pass

def update():
    pass

def draw():
    pass

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
