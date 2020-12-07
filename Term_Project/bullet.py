from pico2d import *
import gfw
import gobj
import enemy
import boss
import menu_state


class Bullet:
    bullets = []

    def __init__(self, x, y, dir):
        self.base_bullet_image = gfw.load_image('res/base_bulletRIGHT.png')
        self.baseR_bullet_image = gfw.load_image('res/base_bulletLEFT.png')
        self.baseUP_bullet_image = gfw.load_image('res/base_bulletUP.png')
        self.x, self.y = x, y
        self.dir = dir
        self.layer = list(gfw.world.objects_at(gfw.layer.zombie))
        self.enemy = []

        self.layer2 = list(gfw.world.objects_at(gfw.layer.boss))
        self.boss = []
        # if enemy.isCreate == True:
        #     self.layer = list(gfw.world.objects_at(gfw.layer.zombie))
        #     self.enemy = self.layer[0]

        # print('Radius = %d' % self.radius)


    def draw(self):
        if self.dir == 2:
            self.base_bullet_image.clip_draw(0, 0, 150, 150, self.x + 30, self.y + 8, 350, 350)
        elif self.dir == 1:
            self.baseR_bullet_image.clip_draw(0, 0, 150, 150, self.x - 30, self.y + 8, 350, 350)
        elif self.dir == 3:
            self.baseUP_bullet_image.clip_draw(0, 0, 150, 150, self.x, self.y + 30, 350, 350)

    def update(self):
        x, y = self.x, self.y
        if self.dir == 2:
            x += 10
        elif self.dir == 1:
            x -= 10
        elif self.dir == 3:
            y += 10

        self.y = y
        self.x = x

        if x < -10 or x > get_canvas_width() + 10 or y > get_canvas_height() + 10:
            gfw.world.remove(self)
        if enemy.isCreate == True:
            for i in range(len(self.layer)):
                self.enemy = self.layer[i]
                if gobj.collides_box(self, self.enemy):
                    gfw.world.remove(self)
                    obj_dead = enemy.CollisonImage(self.enemy.x,self.enemy.y,self.enemy.dir,self.enemy.sel)
                    gfw.world.add(gfw.layer.obj_dead, obj_dead)
                    print(len(self.layer))
                    if len(self.layer) <= 1:
                        enemy.isCreate = False
                        boss.ImmortalMode = False
                    enemy.Enemy.remove(self.enemy)

        if boss.isCreate == True:
            self.boss = self.layer2[0]
            if gobj.collides_box(self,self.boss):
                if boss.ImmortalMode == False:
                    boss.hp -= 1
                gfw.world.remove(self)
                if boss.hp == 0:
                    gfw.world.remove(self.boss)
                    boss.isCreate =False
                    gfw.change(menu_state)

    def get_bb(self):
        x, y = self.x, self.y
        minX = 0
        minY = 0
        maxX = 0
        maxY = 0
        if self.dir == 1:
            minX = self.x - 50
            minY = self.y
            maxX = self.x - 10
            maxY = self.y + 15
        elif self.dir == 2:
            minX = self.x + 10
            minY = self.y
            maxX = self.x + 50
            maxY = self.y + 15
        elif self.dir == 3:
            minX = self.x - 7
            minY = self.y + 10
            maxX = self.x + 7
            maxY = self.y + 50

        return minX, minY, maxX, maxY
