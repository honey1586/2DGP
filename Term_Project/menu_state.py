import gfw
from pico2d import *
import game_state
import title_state

def enter():
    global image
    image = load_image('res/menu.png')



def update():
    pass


def draw():
    image.draw(400, 300)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.pop()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.pop()
    elif (e.type ,e.key) == (SDL_KEYDOWN , SDLK_RETURN):
        gfw.quit()



def exit():
    pass


def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()
