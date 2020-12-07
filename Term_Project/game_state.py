import gfw
from pico2d import *
import background as bg
from enemy import Enemy ,CollisonImage
from bullet import Bullet
import player
import gobj
import zombiebullet
import random
import bossbullet
import menu_state
import boss as bs

image = None

def enter():
    Reset()

    #global obj_dead
    global bgm
    bgm = load_music('res/game_bgm.mp3')
    bgm.repeat_play()

    global sound
    sound = load_wav('res/mission1_start.wav')
    sound.play()



def Reset():
    gfw.world.clear()
    gfw.world.init(['bg','bossbullet','boss', 'zombiebullet', 'bullet', 'zombie', 'p','obj_dead'])

    global bg
    bg.init()
    gfw.world.add(gfw.layer.bg, bg)

    global p
    p = player.Player()
    gfw.world.add(gfw.layer.p, p)

    global zombie , zombies
    for i in range (0,20):
        zombie = Enemy(random.randint(500,1600) , 115, random.randint(1,2))
        gfw.world.add(gfw.layer.zombie, zombie)

    global boss
    boss = bs.Boss()
    gfw.world.add(gfw.layer.boss ,boss)

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()
    for b in Bullet.bullets: b.draw()
    for zb in zombiebullet.ZombieBullet.bullets: zb.draw()
    for bb in bossbullet.BossBullet.bullets: bb.draw()


def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:

            gfw.push(menu_state)

    p.handle_event(e)

def pause():
    pass

def resume():
    pass

def exit():
    global bgm , sound
    del bgm , sound


if __name__ == '__main__':
    gfw.run_main()
