from pico2d import *
import gfw

class Bomb:
    bombs = []
    def __init__(self, x,y,dir):
        self.bomb_image = gfw.load_image('res/base_bulletRIGHT.png')
        self.bombR_image = gfw.load_image('res/base_bulletLEFT.png')
        self.x,self.y = x,y
        self.dir = dir

        # print('Radius = %d' % self.radius)
    def draw(self):
        if self.dir == 2:
            self.bomb_image.clip_draw(0, 0, 150, 150, self.x + 30, self.y + 8, 350, 350)
        elif self.dir == 1:
        elif self.dir == 3:
            self.bombR_image.clip_draw(0, 0, 150, 150, self.x - 30, self.y + 8, 350, 350)

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

        # if x < -10 or x > get_canvas_width() + 10 or y > get_canvas_height() +10:
        #     Bomb.bombs.remove(self)
        #     print('Ball count - %d' % len(Bomb.bombs))

