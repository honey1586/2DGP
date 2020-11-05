import random
from pico2d import *
import gfw

RES_DIR = 'res/'

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
    def __init__(self):
        self.delta = 0, 0
        self.fidx = 0
        self.action = 0
        self.pos = 100,100
        Player.image = gfw.image.load(RES_DIR + '/Character1.png')



    def draw(self):
        sx = self.fidx * 70
        sy = self.action * 70
        self.image.clip_draw(sx, sy, 100, 100, *self.pos)

    def update(self):
        self.fidx = (self.fidx + 1) % 8

    def fire(self):
        pass

    def updateDelta(self, ddx, ddy):
        pass

    def updateAction(self, dx, ddx):
        pass


    def handle_event(self, e):
        pass
