import gfw
from pico2d import *
import background as bg
from enemy import Enemy ,CollisonImage
from bullet import Bullet
import player
import gobj
import boss
import zombiebullet
import random
import bossbullet


def enter():
    gfw.world.init(['bg','bossbullet','boss', 'zombiebullet', 'bullet', 'zombie', 'p','obj_dead'])

    global bg
    bg.init()
    gfw.world.add(gfw.layer.bg, bg)

    global p
    p = player.Player()
    gfw.world.add(gfw.layer.p, p)

    global zombie , zombies
    for i in range (0,20):
        zombie = Enemy(random.randint(500,1900) , 115, random.randint(1,2))
        gfw.world.add(gfw.layer.zombie, zombie)

    global boss
    boss = boss.Boss()
    gfw.world.add(gfw.layer.boss ,boss)

    #global obj_dead

def update():
    gfw.world.update()


def draw():
    gfw.world.draw()
    for b in Bullet.bullets: b.draw()
    for zb in zombiebullet.ZombieBullet.bullets: zb.draw()
    for bb in bossbullet.BossBullet.bullets: bb.draw()
    gobj.draw_collision_box()


def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    p.handle_event(e)


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
