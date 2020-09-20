from helper import *
from pico2d import *
import random

# Boy와 관련된 것들을 클래스에 넣어서 관리하면 유지보수가 쉬워진다.
class Boy:
    def __init__(self):
        self.pos = get_canvas_width() // 2,80
        self.delta = 0,0
        self.target = 0,0
        self.speed = 1
        self.image = load_image('../res/run_animation.png')
        self.frame = 0
        self.moving = False

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.pos[0], self.pos[1])

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.pos, self.moving = move_toward(self.pos, self.delta, self.target)


class Grass:
    def __init__(self):
        self.x, self.y = 400,30
        self.image = load_image('../res/grass.png')
    def draw(self):
        self.image.draw(self.x,self.y)

def handle_events():
    global running
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_MOUSEBUTTONDOWN:
            boy.target = e.x,get_canvas_height() - e.y - 1
            boy.delta = delta(boy.pos,boy.target,10)





open_canvas()

boy = Boy()
grass = Grass()

running = True
while running:
    clear_canvas()

    grass.draw()
    boy.draw()

    update_canvas()
    handle_events()

    boy.update()


    delay(0.01)

# delay(1)
close_canvas()