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
    BODY_UP_SHOOT_ACTION = 5

    LEG_RIGHT_IDLE_ACTION = 4
    LEG_LEFT_IDLE_ACTION = 3
    LEG_RIGHT_WALK_ACTION =2
    LEG_LEFT_WALK_ACTION = 1
    LEG_JUMP_ACTION = 0

    #constructor
    def __init__(self):
        self.x,self.y = 50,125
        self.dx,self.dy = 0,0

        self.body_fidx = 0
        self.leg_fidx = 0
        self.lxocha = 0
        self.lyocha = 0
        self.bxocha= 0
        self.byocha = 0
        self.framespeed = 0
        self.temp = 0
        self.tmp =0
        self.dir = 0

        self.fireaction = False
        self.isLeftWalking = False
        self.isRightWalking = False
        self.isJump = False
        self.isUpLook = False

        self.body_action = Player.BODY_RIGHT_IDLE_ACTION
        self.leg_action = Player.LEG_RIGHT_IDLE_ACTION

        self.time = 0

        Player.body_image = gfw.load_image('res/body_idle.png')
        Player.leg_image = gfw.load_image('res/leg_idle.png')


    def draw(self):
        leg_sx = self.leg_fidx * 150
        leg_sy = self.leg_action * 150
        self.leg_image.clip_draw(leg_sx, leg_sy, 150, 150, self.x - 5 + self.lxocha, self.y - 28, 350, 350)

        body_sx = self.body_fidx * 150
        body_sy = self.body_action * 150
        self.body_image.clip_draw(body_sx,body_sy,150,150,self.x+self.bxocha,self.y + self.byocha,350,350)

    def update(self):
        global px
        self.calframe()
        self.moving()

        if self.dx > 0:
            self.body_action = Player.BODY_RIGHT_IDLE_ACTION
            if self.fireaction == True:
                self.body_action = Player.BODY_RIGHT_SHOOT_ACTION
            self.leg_action = Player.LEG_RIGHT_WALK_ACTION
            self.lxocha = 0

        if self.dx < 0:
            self.body_action = Player.BODY_LEFT_IDLE_ACTION
            if self.fireaction == True:
                self.body_action = Player.BODY_LEFT_SHOOT_ACTION
            self.leg_action = Player.LEG_LEFT_WALK_ACTION
            self.lxocha = 10

        if self.isJump == True:
            if self.y <= 213:
                self.leg_action = Player.LEG_JUMP_ACTION
                self.y += 4
            if self.y > 213:
                self.isJump = False

        if self.isJump == False and self.y > 125:
            self.y -= 4
            if self.dir == 2:
                self.leg_action = Player.LEG_RIGHT_IDLE_ACTION
            if self.dir == 1:
                self.leg_action = Player.LEG_LEFT_IDLE_ACTION

        px += self.dx

    def calframe(self):
        self.time += gfw.delta_time
        frame = self.time * 10

        if self.fireaction == False:
            self.byocha = 0
            self.bxocha = 0
            self.body_fidx = int(frame) % 10

        if self.fireaction == True:
            self.body_fidx = 5
            if self.dir == 3 and self.tmp == 2:
                self.bxocha = -5
                self.byocha = 25
                self.body_fidx = 0
            elif self.dir == 3 and self.tmp == 1:
                self.bxocha = 5
                self.byocha = 25
                self.body_fidx = 1

        if self.isJump == False:
            self.leg_fidx = int(frame) % 10
        if self.isJump == True:
            if self.dir == 2:
                self.leg_fidx =0
            if self.dir == 1:
                self.leg_fidx =1




    # 움직임
    def moving(self):
        self.x = self.x + self.dx

    def jump(self):
        self.isJump = True


    def fire(self , dir):
        bullet = Bullet(self.x,self.y,dir)
        Bullet.bullets.append(bullet)

    def tryfire(self):
        self.fireaction = True

        if self.dir == 1:

            self.body_action = Player.BODY_LEFT_SHOOT_ACTION

        elif self.dir == 2:

            self.body_action = Player.BODY_RIGHT_SHOOT_ACTION

        elif self.dir == 3:

            self.body_action = Player.BODY_UP_SHOOT_ACTION



        self.fire(self.dir)

    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                self.dir = 1  # 왼쪽
                self.dx -= 1

            if e.key == SDLK_RIGHT:
                self.dir = 2  # 오른쪽
                self.dx += 1

            if e.key == SDLK_UP:
                self.tmp = self.dir
                self.dir = 3
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
            if e.key == SDLK_UP:
                self.dir = self.tmp
            if e.key == SDLK_a:
                self.fireaction = False
                self.body_action = self.temp







