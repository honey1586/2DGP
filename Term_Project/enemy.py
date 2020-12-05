from pico2d import *
import gfw
import player

class Enemy:
    zombie1_idleimage = None
    zombie1_walkimage = None
    zombie1_attackimage = None
    zombie1_deadimage = None


    zombie2_idleimage = None
    zombie2_walkimage = None
    zombie2_attackimage = None
    zombie2_deadimage = None


    IDLE_STATE = 1
    WALK_STATE = 2
    ATTACK_STATE = 3
    DEAD_STATE = 4

    def __init__(self):
        self.x = 500
        self.y = 115
        self.state = Enemy.IDLE_STATE
        self.dx = 0
        self.sel = 1
        self.dist = 0
        self.dir = 0
        self.traceMode = False

        self.time = 0

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
        if self.sel == 1:
            z1_sx = self.fidx * 150
            if self.state == Enemy.IDLE_STATE:
                self.zombie1_idleimage.clip_draw(z1_sx,0,150,150,self.x ,self.y,350,350)
            if self.state == Enemy.WALK_STATE:
                self.zombie1_walkimage.clip_draw(z1_sx,0,150,150,self.x ,self.y,350,350)
            if self.state == Enemy.ATTACK_STATE:
                self.zombie1_attackimage.clip_draw(z1_sx, 0, 150, 150, self.x, self.y, 350, 350)

    def update(self):

        self.checkdistance()
        self.move()

        if self.sel == 1:
            if self.state == Enemy.IDLE_STATE:
                self.imagesize = self.zombie1_idleimage_size
            if self.state == Enemy.WALK_STATE:
                self.imagesize = self.zombie1_walkimage_size
            if self.state == Enemy.ATTACK_STATE:
                self.imagesize = self.zombie1_attackimage_size
        self.calframe()

    def calframe(self):
        self.time += gfw.delta_time * 0.5
        frame = self.time * 10
        self.fidx = int(frame) % self.imagesize

    def move(self):
        if self.traceMode == True:
            self.state = Enemy.WALK_STATE
            if player.x < self.x:
                self.dir = 0
                self.x -= 0.5
            else:
                self.dir = 1
                self.x += 0.5

    def checkCollision(self):
        pass


    def checkdistance(self):
        self.dist = math.sqrt((self.x - player.x)**2)
        print("player.x = ",player.x , "self.x = ",self.x)
        if self.dist <= 400:
            self.traceMode = True

        if self.dist <= 180:
            self.traceMode = False
            self.state = Enemy.ATTACK_STATE


    def attack(self):
        pass




