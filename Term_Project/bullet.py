from pico2d import *
import gfw

class Bullet:
    bullets = []
    def __init__(self, x,y,dir):
        self.base_bullet_image = gfw.load_image('res/base_bullet.png')
        self.baseR_bullet_image = gfw.load_image('res/base_bulletR.png')
        self.x,self.y = x,y
        self.dir = dir

        # print('Radius = %d' % self.radius)
    def draw(self):
        if self.dir == 1 or self.dir == 3:
            self.base_bullet_image.clip_draw(0, 0, 150, 150, self.x + 20, self.y + 8, 350, 350)
        elif self.dir == 0 or self.dir == 2:
            self.baseR_bullet_image.clip_draw(0, 0, 150, 150, self.x + 20, self.y + 8, 350, 350)

    def update(self):
        if self.dir == 1 or self.dir == 3:
            x += 10
        elif self.dir == 0 or self.dir == 2:
            x -= 10

        self.x = x

        if x < -20 or x > get_canvas_width() + 20:
            Bullet.bullets.remove(self)
            print('Ball count - %d' % len(Bullet.bullets))

