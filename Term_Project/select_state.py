import gfw
from pico2d import *
import gfw_image

def enter():
    global image , ch_image , idx
    image = load_image('res/SelectionWindow.png')
    ch_image = load_image('res/Select_Character1.png')
    idx = 0


def update():
    pass


def draw():
    global idx
    image.draw(400, 300)
    ch_image.clip_draw(0,-100,167,320,132,246)



def handle_event(e):
    global idx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_LEFT):
        idx = 2



def exit():
    global image
    del image


def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()
