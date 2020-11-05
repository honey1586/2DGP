from pico2d import *
import gfw
from gobj import *

class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-2,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 2,  0),
        (SDL_KEYDOWN, SDLK_DOWN):  ( 0, 0),
        (SDL_KEYDOWN, SDLK_UP):    ( 0,  0),
        (SDL_KEYUP, SDLK_LEFT):    ( 2,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-2,  0),
        (SDL_KEYUP, SDLK_DOWN):    ( 0,  0),
        (SDL_KEYUP, SDLK_UP):      ( 0, 0),
    }
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    image = None

    #constructor
    def __init__(self,num):
        self.pos = 50,50
        self.fidx = 0
        self.delta = 0, 0
        self.action = 3
        self.time =0
        Player.image = load_image('res/Character4_Idle.png')

    def draw(self):
        sx = self.fidx * 71
        sy = self.action * 82
        self.image.clip_draw(sx, sy, 71, 82, *self.pos)


    def update(self):
        x, y = self.pos
        dx, dy = self.delta
        self.pos = x + dx, y + dy
        self.time += gfw.delta_time
        frame = self.time * 10
        self.fidx = int(frame) % 10


    def updateDelta(self, ddx, ddy):
        dx,dy = self.delta
        dx += ddx
        dy += ddy
        if ddx != 0:
            self.updateAction(dx, ddx)
        self.delta = dx, dy

    def updateAction(self, dx, ddx):
        self.action = \
            0 if dx < 0 else \
            1 if dx > 0 else \
            2 if ddx > 0 else 3

    def fire(self):
        pass

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.updateDelta(*Player.KEY_MAP[pair])
