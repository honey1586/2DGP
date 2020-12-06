from pico2d import *
import gfw
import player
from bossbullet import BossBullet
import bullet
import gobj

isCreate = False
hp = 30
ImmortalMode = True

class Boss:
    idleimage = None
    attackimage = None


    def __init__(self):
        self.x = 900
        self.y = 400
        self.fidx = 0
        self.dir = 'w'
        self.sx = 0
        self.attackdelay = 0
        self.moveMode = True
        self.attackMode = False
        self.MOVE_STATE = 1
        self.ATTACK_STATE = 2

        self.layer = list(gfw.world.objects_at(gfw.layer.bullet))
        self.bullet = []

        self.state = self.MOVE_STATE
        self.time = 0
        self.imagesize = 0

        Boss.idleimage = gfw.load_image("res/boss_move.png")
        self.idleimage_size = 1
        Boss.attackimage = gfw.load_image("res/boss_attack.png")
        self.attackimage_size = 7

        self.imagesize = 1

        global isCreate
        isCreate = True

    def draw(self):
        self.sx = self.fidx * 150
        if self.state == self.MOVE_STATE:
            self.idleimage.clip_composite_draw(self.sx, 0, 150, 150, 0, self.dir, self.x - player.px / 2 , self.y,
                                                       350, 350)
        if self.state == self.ATTACK_STATE:
            self.attackimage.clip_composite_draw(self.sx, 0, 150, 150, 0, self.dir, self.x - player.px / 2, self.y,
                                                       350, 350)

    def update(self):
        self.time += gfw.delta_time
        frame = self.time * self.imagesize
        self.fidx = int(frame) % self.imagesize

        if self.state == self.MOVE_STATE:
            self.move()

        if self.attackMode == True:
            self.attackdelay += gfw.delta_time
            if self.fidx >= 6:
                if self.attackdelay >= 0.1:
                    self.fire()
                    self.attackdelay = 0


    def move(self):
        if player.x < self.x - player.px / 2:
            self.dir = 'w'
            self.x = self.x - 2
        else:
            self.dir = 'h'
            self.x = self.x + 2

        if math.sqrt((self.x - player.x - player.px /2) ** 2) <= 2:
            self.attack()

    def attack(self):
        self.state = self.ATTACK_STATE
        self.attackMode = True
        self.imagesize = self.attackimage_size

    def fire(self):
        self.time = 0
        bossbullet = BossBullet(self.x - player.px / 2, self.y + 35)
        gfw.world.add(gfw.layer.bossbullet, bossbullet)

        if player.x == self.x:
            self.fidx = 0
        else:
            self.attackMode = False
            self.imagesize = self.idleimage_size
            self.state = self.MOVE_STATE


    def get_bb(self):
        x, y = self.x, self.y
        return x - 70 - player.px / 2 , y - 50, x + 70  - player.px / 2, y + 50

