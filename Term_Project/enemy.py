from pico2d import *
import gfw
import player
from zombiebullet import ZombieBullet

IDLE_STATE = 1
WALK_STATE = 2
ATTACK_STATE = 3
DEAD_STATE = 4

state = IDLE_STATE
deadMode = False
isCreate = False

class Enemy:
    zombie1_idleimage = None
    zombie1_walkimage = None
    zombie1_attackimage = None
    zombie1_deadimage = None


    zombie2_idleimage = None
    zombie2_walkimage = None
    zombie2_attackimage = None
    zombie2_deadimage = None


    def __init__(self):
        self.x = 500
        self.y = 115

        self.dx = 0
        self.sel = 1
        self.dist = 0
        self.dir = 'w'
        self.traceMode = False
        self.attackMode = False
        self.target = 0

        self.attackdelay = 0
        self.dd = 0
        self.time = 0

        global isCreate
        isCreate = True
        Enemy.zombie1_idleimage = gfw.load_image("res/zombie1_idle.png")
        self.zombie1_idleimage_size = 7
        Enemy.zombie1_walkimage = gfw.load_image("res/zombie1_walk.png")
        self.zombie1_walkimage_size = 11
        Enemy.zombie1_attackimage = gfw.load_image("res/zombie1_attack.png")
        self.zombie1_attackimage_size = 9
        Enemy.zombie1_deadimage = gfw.load_image("res/zombie1_dead.png")
        self.zombie1_deadimage_size = 12


        Enemy.zombie2_idleimage = gfw.load_image("res/zombie2_idle.png")
        self.zombie2_idleimage_size = 10
        Enemy.zombie2_walkimage = gfw.load_image("res/zombie2_walk.png")
        self.zombie2_walkimage_size = 14
        Enemy.zombie2_attackimage = gfw.load_image("res/zombie2_attack.png")
        self.zombie2_attackimage_size = 12
        Enemy.zombie2_deadimage = gfw.load_image("res/zombie2_dead.png")
        self.zombie2_deadimage_size = 12

        self.fidx = 0
        self.imagesize = 0

    def draw(self):
        z1_sx = self.fidx * 150
        if self.sel == 1:
            if state == IDLE_STATE:
                self.zombie1_idleimage.clip_composite_draw(z1_sx,0,150,150,0,self.dir,self.x ,self.y,350,350)
            if state == WALK_STATE:
                self.zombie1_walkimage.clip_composite_draw(z1_sx,0,150,150,0,self.dir,self.x ,self.y,350,350)
            if state == ATTACK_STATE:
                self.zombie1_attackimage.clip_composite_draw(z1_sx,0,150,150,0,self.dir,self.x ,self.y,350,350)
            if state == DEAD_STATE:
                self.zombie1_deadimage.clip_composite_draw(z1_sx,0,150,150,0,self.dir,self.x ,self.y,350,350)

        if self.sel == 2:
            if state == IDLE_STATE:
                self.zombie1_idleimage.clip_composite_draw(z1_sx,0,150,150,0,self.dir,self.x ,self.y,350,350)
            if state == WALK_STATE:
                self.zombie1_walkimage.clip_composite_draw(z1_sx,0,150,150,0,self.dir,self.x ,self.y,350,350)
            if state == ATTACK_STATE:
                self.zombie1_attackimage.clip_composite_draw(z1_sx,0,150,150,0,self.dir,self.x ,self.y,350,350)
            if state == DEAD_STATE:
                self.zombie1_deadimage.clip_composite_draw(z1_sx,0,150,150,0,self.dir,self.x ,self.y,350,350)


    def update(self):

        if self.attackMode == False and deadMode == False:
            self.checkdistance()
        if self.traceMode == True and self.attackMode == False and deadMode == False:
            self.move()

        self.calframe()


    def calframe(self):
        if self.sel == 1:
            if state == IDLE_STATE:
                self.fidx = 0
                self.imagesize = self.zombie1_idleimage_size
            if state == WALK_STATE:
                self.imagesize = self.zombie1_walkimage_size
            if state == ATTACK_STATE:
                self.imagesize = self.zombie1_attackimage_size
            if state == DEAD_STATE:
                self.dd = 100
                self.imagesize = self.zombie1_deadimage_size

        self.time += gfw.delta_time * 0.5
        frame = self.time * self.imagesize
        self.fidx = int(frame) % self.imagesize

        if self.attackMode == True:
            if self.fidx >= 8:
                if self.time >= 0.9:
                    self.fire(self.dir)
                self.fidx = 0

        if deadMode == True:
            if self.fidx >= 11:
                if self.time >= 0.8:
                    gfw.world.remove(self)
                self.fidx = 0

    def move(self):
        global state
        state = WALK_STATE
        if player.x < self.x:
            self.dir = 'w'
            self.x -= 0.5
        else:
            self.dir = 'h'
            self.x += 0.5


    def checkdistance(self):
        self.dist = math.sqrt((self.x - player.x)**2)
        if self.dist <= 400 and self.attackMode == False:
            self.fidx = 0
            self.traceMode = True

        if self.dist <= 180:
            self.target = player.x
            self.fidx = 0
            self.traceMode = False
            self.attack()

    def attack(self):
        global state
        self.attackMode = True
        state = ATTACK_STATE

    def fire(self, dir):
        self.time = 0
        bullet = ZombieBullet(self.x, self.y + 35, dir ,(self.target , 80))
        gfw.world.add(gfw.layer.zombiebullet, bullet)
        self.attackMode = False

    def get_bb(self):
        x,y = self.x,self.y
        return x - 30, y - 45, x + 30, y + 40 - self.dd


