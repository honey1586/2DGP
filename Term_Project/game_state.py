import gfw
from pico2d import *
import background as bg
from player import Player
from bullet import Bullet

def enter():
    gfw.world.init(['bg','player'])

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global bg
    bg.init()
    gfw.world.add(gfw.layer.bg,bg)


def update():
    gfw.world.update()
    for b in Bullet.bullets: b.update()

def draw():
    gfw.world.draw()
    for b in Bullet.bullets: b.draw()

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
