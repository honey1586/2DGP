from pico2d import *
import gfw
import player
from zombiebullet import ZombieBullet


DEAD_STATE = 4
ZOMBIE_COUNT = 20


deadMode = False
isCreate = False

gsspeed = 0


class Enemy:
    zombies = []
    zombie1_idleimage = None
    zombie1_walkimage = None
    zombie1_attackimage = None


    zombie2_idleimage = None
    zombie2_walkimage = None
    zombie2_attackimage = None


    def __init__(self ,x,y, sel):
        self.x = x
        self.y = y
        self.dx = 0
        self.sel = sel
        self.dist = 0
        self.dir = 'w'
        self.traceMode = False
        self.attackMode = False
        self.target = 0

        self.attackdelay = 0
        self.dd = 0
        self.time = 0
        self.IDLE_STATE = 1
        self.WALK_STATE = 2
        self.ATTACK_STATE = 3

        self.state = self.IDLE_STATE
        global isCreate
        isCreate = True
        Enemy.zombie1_idleimage = gfw.load_image("res/zombie1_idle.png")
        self.zombie1_idleimage_size = 7
        Enemy.zombie1_walkimage = gfw.load_image("res/zombie1_walk.png")
        self.zombie1_walkimage_size = 11
        Enemy.zombie1_attackimage = gfw.load_image("res/zombie1_attack.png")
        self.zombie1_attackimage_size = 9

        Enemy.zombie2_idleimage = gfw.load_image("res/zombie2_idle.png")
        self.zombie2_idleimage_size = 10
        Enemy.zombie2_walkimage = gfw.load_image("res/zombie2_walk.png")
        self.zombie2_walkimage_size = 14
        Enemy.zombie2_attackimage = gfw.load_image("res/zombie2_attack.png")
        self.zombie2_attackimage_size = 12


        self.fidx = 0
        self.imagesize = 0

    def draw(self):
        z1_sx = self.fidx * 150
        if self.sel == 1:
            if self.state == self.IDLE_STATE:
                self.zombie1_idleimage.clip_composite_draw(z1_sx, 0, 150, 150, 0, self.dir, self.x - player.px /2, self.y, 350, 350)
            if self.state == self.WALK_STATE:
                self.zombie1_walkimage.clip_composite_draw(z1_sx, 0, 150, 150, 0, self.dir, self.x - player.px /2, self.y, 350, 350)
            if self.state == self.ATTACK_STATE:
                self.zombie1_attackimage.clip_composite_draw(z1_sx, 0, 150, 150, 0, self.dir, self.x - player.px /2, self.y, 350, 350)

        if self.sel == 2:
            if self.state == self.IDLE_STATE:
                self.zombie2_idleimage.clip_composite_draw(z1_sx, 0, 150, 150, 0, self.dir, self.x - player.px /2, self.y,350, 350)
            if self.state == self.WALK_STATE:
                self.zombie2_walkimage.clip_composite_draw(z1_sx, 0, 150, 150, 0, self.dir, self.x - player.px /2, self.y, 350, 350)
            if self.state == self.ATTACK_STATE:
                self.zombie2_attackimage.clip_composite_draw(z1_sx, 0, 150, 150, 0, self.dir, self.x - player.px /2 , self.y, 350, 350)


    def update(self):
        if self.attackMode == False and deadMode == False:
            self.checkdistance()
        if self.traceMode == True and self.attackMode == False and deadMode == False:
            self.move()

        self.calframe()

    def calframe(self):
        if self.sel == 1:
            if self.state == self.IDLE_STATE:
                self.fidx = 0
                self.imagesize = self.zombie1_idleimage_size
            if self.state == self.WALK_STATE:
                self.imagesize = self.zombie1_walkimage_size
            if self.state == self.ATTACK_STATE:
                self.imagesize = self.zombie1_attackimage_size

        if self.sel == 2:
            if self.state == self.IDLE_STATE:
                self.fidx = 0
                self.imagesize = self.zombie2_idleimage_size
            if self.state == self.WALK_STATE:
                self.imagesize = self.zombie2_walkimage_size
            if self.state == self.ATTACK_STATE:
                self.imagesize = self.zombie2_attackimage_size

        self.time += gfw.delta_time * 0.5
        frame = self.time * self.imagesize
        self.attackdelay = self.time
        self.fidx = int(frame) % self.imagesize

        if self.attackMode == True:
            if self.sel == 1:
                if self.fidx >= 8:
                    if self.attackdelay >= 0.9:
                        self.fire(self.dir)
                        self.attackdelay = 0
                    self.fidx = 0
            if self.sel == 2:
                if self.fidx >= 11:
                    if self.attackdelay >= 0.9:
                        self.fire(self.dir)
                        self.attackdelay = 0
                    self.fidx = 0

    def move(self):
        self.state = self.WALK_STATE
        if player.x < self.x:
            self.dir = 'w'
            self.x = self.x - 0.5
        else:
            self.dir = 'h'
            self.x = self.x - 0.5

    def checkdistance(self):
        self.dist = math.sqrt((self.x - player.x - player.px /2) ** 2)
        if self.dist <= 1600 and self.attackMode == False:
            self.fidx = 0
            self.traceMode = True

        if self.dist <= 200:
            self.target = player.x
            self.fidx = 0
            self.traceMode = False
            self.attack()

    def attack(self):
        self.attackMode = True
        self.state = self.ATTACK_STATE

    def fire(self, dir):
        self.time = 0
        bullet = ZombieBullet(self.x - player.px /2, self.y + 35, dir, (self.target, 80))
        gfw.world.add(gfw.layer.zombiebullet, bullet)
        self.attackMode = False

    def get_bb(self):
        x, y = self.x, self.y
        return x - 30 - player.px /2 , y - 45, x + 30 - player.px /2, y + 40 - self.dd
    def remove(self):
        gfw.world.remove(self)

class CollisonImage:

    def __init__(self,x,y,dir,sel):
        self.zombie1_deadimage = gfw.load_image("res/zombie1_dead.png")
        self.zombie1_deadimage_size = 12
        self.zombie2_deadimage = gfw.load_image("res/zombie2_dead.png")
        self.zombie2_deadimage_size = 12
        self.x = x
        self.y = y
        self.fidx =0
        self.time =0
        self.dir = dir
        self.sel = sel
    def update(self):
        self.time += gfw.delta_time
        frame = self.time * 12
        self.fidx = int(frame) % 12
        if self.fidx >= 11:
            if self.time >= 0.8:
                gfw.world.remove(self)
            self.fidx = 0
    def draw(self):
        z1_sx = self.fidx * 150
        if self.sel == 1:
            self.zombie1_deadimage.clip_composite_draw(z1_sx, 0, 150, 150, 0, self.dir, self.x - player.px / 2, self.y,350, 350)
        elif self.sel == 2:
            self.zombie2_deadimage.clip_composite_draw(z1_sx, 0, 150, 150, 0, self.dir, self.x- player.px /2, self.y, 350,350)
