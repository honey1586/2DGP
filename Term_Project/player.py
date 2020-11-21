from pico2d import *
import gfw

class Player:
    body_image = None
    leg_image = None
    BODY_RIGHT_IDLE_ACTION = 3
    BODY_LEFT_IDLE_ACTION = 2
    BODY_RIGHT_SHOOT_ACTION = 1
    BODY_LEFT_SHOOT_ACTION = 0

    LEG_RIGHT_IDLE_ACTION = 3
    LEG_LEFT_IDLE_ACTION = 2
    LEG_RIGHT_WALK_ACTION = 1
    LEG_LEFT_WALK_ACTION = 0

    #constructor
    def __init__(self):
        self.x,self.y = 50,120
        self.dx,self.dy = 0,0

        self.body_fidx = 0
        self.leg_fidx = 0
        self.ocha = 0
        self.framespeed = 0

        self.body_action = Player.BODY_RIGHT_IDLE_ACTION
        self.leg_action = Player.LEG_RIGHT_IDLE_ACTION

        self.time = 0

        Player.body_image = gfw.load_image('res/body_idle.png')
        Player.leg_image = gfw.load_image('res/leg_idle.png')


    def draw(self):
        leg_sx = self.leg_fidx * 150
        leg_sy = self.leg_action * 150
        self.leg_image.clip_draw(leg_sx, leg_sy, 150, 150, self.x - 5 + self.ocha, self.y - 28, 350, 350)

        body_sx = self.body_fidx * 150
        body_sy = self.body_action * 150
        self.body_image.clip_draw(body_sx,body_sy,150,150,self.x,self.y,350,350)

    def update(self):
        self.calframe()
        self.moving()

    def calframe(self):
        self.time += gfw.delta_time
        frame = self.time * 10 * self.framespeed
        self.leg_fidx = int(frame) % 10
        self.body_fidx = int(frame) % 10
    # 움직임
    def moving(self):
        self.x = self.x + self.dx

    # 점프
    def tryjump(self):
        self.jump()

    def jump(self):
        pass

    def fire(self):
        pass

    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                self.dx -= 2
                self.body_action = Player.BODY_LEFT_IDLE_ACTION
                self.leg_action = Player.LEG_LEFT_WALK_ACTION
                self.ocha = 10
            if e.key == SDLK_RIGHT:
                self.dx += 2
                self.body_action = Player.BODY_RIGHT_IDLE_ACTION
                self.leg_action = Player.LEG_RIGHT_WALK_ACTION
                self.ocha = 0

            if e.key == SDLK_s:

        if e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                self.dx += 2
                self.leg_action = Player.LEG_LEFT_IDLE_ACTION
            if e.key == SDLK_RIGHT:
                self.dx -= 2
                self.leg_action = Player.LEG_RIGHT_IDLE_ACTION






