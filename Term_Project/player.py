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
    SP_KEY_MAP = {
        (SDL_KEYDOWN, SDLK_a): ('fire', 0),
        (SDL_KEYUP, SDLK_a): ('fire', 0),
    }

    Leg_image = None
    Body_image = None

    #constructor
    def __init__(self,num):
        self.legposX , self.legposY = 45,50
        self.bodyposX , self.bodyposY = 50,70
        self.fidx = 0
        self.delta = 0, 0
        self.leg_action = 3
        self.body_action = 3
        self.time = 0
        self.ocha = 0


        Player.Leg_image = load_image('res/leg_idle.png')
        Player.Body_image = load_image('res/body_idle.png')

    def draw(self):
        leg_sx = self.fidx * 150
        leg_sy = self.leg_action * 150
        body_sx = self.fidx * 150
        body_sy = self.body_action * 150
        self.Leg_image.clip_draw(leg_sx, leg_sy, 150, 150, self.legposX + self.ocha , self.legposY,300,300)
        self.Body_image.clip_draw(body_sx, body_sy, 150, 150, self.bodyposX,self.bodyposY,300,300)


    def update(self):
        legx, legy = self.legposX,self.legposY
        bodyx,bodyy = self.bodyposX, self.bodyposY
        dx, dy = self.delta
        self.legposX , self.legposY = legx + dx, legy + dy
        self.bodyposX , self.bodyposY = bodyx + dx, bodyy + dy

        self.time += gfw.delta_time
        frame = self.time * 10
        self.fidx = int(frame) % 10

    def updateDelta(self, ddx, ddy , motion , zzz):
        dx,dy = self.delta
        dx += ddx
        dy += ddy
        if ddx != 0:
            self.updateAction(dx, ddx , motion , zzz)
        self.delta = dx, dy

    def updateAction(self, dx, ddx , motion , zzz):
        if dx < 0 : # 왼쪽 걷기
            self.leg_action = 0

            self.ocha = 10
            if motion == 'fire':
                self.body_action = 0
            else:
                self.body_action = 2

        elif dx > 0: # 오른쪽 걷기
            self.leg_action = 1
            self.body_action = 3
            self.ocha = 0

        elif ddx > 0: # 왼쪽 기본 ( 바라보기 )
            self.leg_action = 2
        elif ddx < 0: # 오른쪽 기본 ( 바라보기 )
            self.leg_action = 3

    def fire(self):
        pass


    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP or pair in Player.SP_KEY_MAP:
            self.updateDelta(*Player.KEY_MAP[pair],*Player.SP_KEY_MAP[pair])
