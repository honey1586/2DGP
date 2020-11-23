from pico2d import *
import gfw
from bullet import Bullet

px = 0

class Player:

    body_image = None
    leg_image = None

    BODY_RIGHT_IDLE_ACTION = 4
    BODY_LEFT_IDLE_ACTION = 3
    BODY_RIGHT_SHOOT_ACTION = 2
    BODY_LEFT_SHOOT_ACTION = 1

    LEG_RIGHT_IDLE_ACTION = 3
    LEG_LEFT_IDLE_ACTION = 2
    LEG_RIGHT_WALK_ACTION =1
    LEG_LEFT_WALK_ACTION = 0

    #constructor
    def __init__(self):
        self.x,self.y = 50,125
        self.dx,self.dy = 0,0

        self.body_fidx = 0
        self.leg_fidx = 0
        self.ocha = 0
        self.framespeed = 0
        self.temp = 0

        self.fireaction = False
        self.isLeftWalking = False
        self.isRightWalking = False
        self.isJump = False

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
        global px
        self.calframe()
        self.moving()

        if self.dx > 0:
            self.body_action = Player.BODY_RIGHT_IDLE_ACTION
            if self.fireaction == True:
                self.body_action = Player.BODY_RIGHT_SHOOT_ACTION
            self.leg_action = Player.LEG_RIGHT_WALK_ACTION
            self.ocha = 0

        if self.dx < 0:
            self.body_action = Player.BODY_LEFT_IDLE_ACTION
            if self.fireaction == True:
                self.body_action = Player.BODY_LEFT_SHOOT_ACTION
            self.leg_action = Player.LEG_LEFT_WALK_ACTION
            self.ocha = 10

        if self.isJump == True:
            if self.y <= 213:
                self.y += 4
            if self.y > 213:
                self.isJump = False
        if self.isJump == False and self.y > 125:
            self.y -= 4

        px += self.dx

    def calframe(self):
        self.time += gfw.delta_time
        frame = self.time * 10
        self.leg_fidx = int(frame) % 10
        if self.fireaction == False:
            self.body_fidx = int(frame) % 10

        if self.fireaction == True:
            self.body_fidx = 5

    # 움직임
    def moving(self):
        self.x = self.x + self.dx

    def jump(self):
        self.isJump = True


    def fire(self):
        bullet = Bullet(self.x,self.y,self.leg_action)
        Bullet.bullets.append(bullet)

    def tryfire(self):
        self.fire()
        self.fireaction = True

        if self.leg_action == Player.LEG_LEFT_IDLE_ACTION:
            self.body_action = Player.BODY_LEFT_SHOOT_ACTION

        elif self.isRightWalking == True or self.leg_action == Player.LEG_RIGHT_IDLE_ACTION:
            self.body_action = Player.BODY_RIGHT_SHOOT_ACTION



    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                self.dx -= 1

            if e.key == SDLK_RIGHT:
                self.dx += 1
            if e.key == SDLK_UP:
                pass
            if e.key == SDLK_a:
                self.temp = self.body_action
                self.tryfire()

            if e.key == SDLK_s:
                self.jump()


        if e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                self.dx += 1
                self.leg_action = Player.LEG_LEFT_IDLE_ACTION
            if e.key == SDLK_RIGHT:
                self.dx -= 1
                self.leg_action = Player.LEG_RIGHT_IDLE_ACTION

            if e.key == SDLK_a:
                self.fireaction = False
                self.body_action = self.temp







