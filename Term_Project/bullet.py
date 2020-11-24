from pico2d import *
import gfw

class Bullet:
    bullets = []
    def __init__(self, x,y,dir):
        self.base_bullet_image = gfw.load_image('res/base_bulletRIGHT.png')
        self.baseR_bullet_image = gfw.load_image('res/base_bulletLEFT.png')
        self.baseUP_bullet_image = gfw.load_image('res/base_bulletUP.png')
        self.x,self.y = x,y
        self.dir = dir

        # print('Radius = %d' % self.radius)
    def draw(self):
        if self.dir == 2:
            self.base_bullet_image.clip_draw(0, 0, 150, 150, self.x + 30, self.y + 8, 350, 350)
        elif self.dir == 1:
            self.baseR_bullet_image.clip_draw(0, 0, 150, 150, self.x - 30, self.y + 8, 350, 350)
        elif self.dir == 3:
            self.baseUP_bullet_image.clip_draw(0, 0, 150, 150, self.x , self.y + 30, 350, 350)

    def update(self):
        x,y = self.x,self.y
        if self.dir == 2:
            x += 10
        elif self.dir == 1:
            x -= 10
        elif self.dir == 3:
            y += 10

        self.y = y
        self.x = x

        if x < -10 or x > get_canvas_width() + 10 or y > get_canvas_height() +10:
            Bullet.bullets.remove(self)
            print('Ball count - %d' % len(Bullet.bullets))

