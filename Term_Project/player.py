from pico2d import *
import gfw
from gobj import *

class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
        (SDL_KEYDOWN, SDLK_DOWN):  ( 0, -1),
        (SDL_KEYDOWN, SDLK_UP):    ( 0,  1),
        (SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-1,  0),
        (SDL_KEYUP, SDLK_DOWN):    ( 0,  1),
        (SDL_KEYUP, SDLK_UP):      ( 0, -1),
    }
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    image = None

    #constructor
    def __init__(self,num):
        self.fidx = 0
        Player.image = load_image('res/Character'+str(num)+'_Idle.png')

    def draw(self):
        sx = self.fidx * 70
        self.image.clip_draw(sx, 0, 68, 81, 50,50)

    def update(self):
        self.fidx = (self.fidx + 1) % 4




    def fire(self):
        pass

    def handle_event(self, e):
        pass