import gfw
from pico2d import *
from background import *
from player import Player

num = 0

def enter():
    gfw.world.init(['player'])

    global player
    player = Player(num)

    gfw.world.add(gfw.layer.player, player)

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

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
