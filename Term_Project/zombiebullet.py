from pico2d import *
import gfw
import player
import gobj

class ZombieBullet:
    bullets = []
    def __init__(self, x,y,dir ,target):
        self.zombie_bullet = gfw.load_image('res/zombie1_bullet.png')
        self.x,self.y = x,y
        self.dir = dir
        self.tx,self.ty = target
        self.delta = math.sqrt((self.tx - x)**2) , math.sqrt((self.ty - y)**2)

        if player.isCreate == True:
            layer = list(gfw.world.objects_at(gfw.layer.player))
            self.player = layer[0]

        # print('Radius = %d' % self.radius)
    def draw(self):
        self.zombie_bullet.clip_composite_draw(0, 0, 150, 150,0,self.dir, self.x, self.y, 350, 350)

    def update(self):
        x,y = self.x,self.y
        dx,dy = self.delta

        if self.dir == 'w':
            x -= dx * gfw.delta_time
        elif self.dir == 'h':
            x += dx * gfw.delta_time
        y += dy * gfw.delta_time
        gravity = 3
        dy -= gravity
        print(y)
        self.x = x
        self.y = y
        self.delta = dx,dy

        if x < -10 or x > get_canvas_width() + 10 or y <= 90:
            gfw.world.remove(self)
            print('bullet count - %d' % len(ZombieBullet.bullets))

        if player.isCreate == True:
            if gobj.collides_box(self, self.player):
                gfw.world.remove(self)
                gfw.world.remove(self.player)
                player.isCreate = False

    def get_bb(self):
        x,y = self.x,self.y
        return x - 35, y - 20, x + 25, y + 15


