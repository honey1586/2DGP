from pico2d import *
import gfw
import player
import gobj


class BossBullet:
    bullets = []

    def __init__(self, x, y):
        self.boss_bullet = gfw.load_image('res/bossbullet.png')
        self.x, self.y = x, y- 100

        if player.isCreate == True:
            layer = list(gfw.world.objects_at(gfw.layer.p))
            self.player = layer[0]

        # print('Radius = %d' % self.radius)

    def draw(self):
        self.boss_bullet.clip_composite_draw(0, 0, 150, 150, 0, 'w', self.x, self.y, 350, 350)

    def update(self):
        x, y = self.x, self.y

        y -= 3

        self.x = x
        self.y = y

        if x < -10 or x > get_canvas_width() + 10 or y <= 90:
            gfw.world.remove(self)

        if player.isCreate == True:
            if gobj.collides_box(self, self.player):
                gfw.world.remove(self)
                gfw.world.remove(self.player)
                player.isCreate = False

    def get_bb(self):
        x, y = self.x, self.y
        return x - 5, y - 5, x + 5, y + 5
