import gfw
from pico2d import *
import game_state
from time import *

def enter():
    global loading,character1,character2,character3,character4,bg ,idx1,idx2,idx3,idx4 , ch1_image , ch2_image , ch3_image, ch4_image , cursor_image , cursorPos , pick_image , pick , pickX , pickY
    idx1 = 1
    idx2 = 0
    idx3 = 0
    idx4 = 0
    cursorPos = 0
    pick = False
    loading = False
    pickX = 0
    pickY = 570
    bg = load_image('res/SelectionWindow.png')
    cursor_image = load_image('res/SelectScene_Cursor.png')
    pick_image = load_image('res/CharacterPick.png')
    ch1_image = load_image('res/Select_Character1.png')
    ch2_image = load_image('res/Select_Character2.png')
    ch3_image = load_image('res/Select_Character3.png')
    ch4_image = load_image('res/Select_Character4.png')

    character1 = load_image('res/Character1.png')
    character2 = load_image('res/Character2.png')
    character3 = load_image('res/Character3.png')
    character4 = load_image('res/Character4.png')


def update():
    global loading,cursorPos
    if loading == True:
        sleep(1)
        game_state.num = cursorPos + 1
        gfw.change(game_state)


def draw():
    global loading ,idx1,idx2,idx3,idx4, cursorPos , pick ,  pickX , pickY

    ch1_image.clip_draw((167 * idx1), 0, 166, 320, 121, 246)
    ch2_image.clip_draw((167 * idx2), 0, 166, 320, 301, 246)
    ch3_image.clip_draw((167 * idx3), 0, 166, 320, 480, 246)
    ch4_image.clip_draw((167 * idx4), 0, 166, 320, 658, 246)

    if pick == True:
        if pickY >= 247: #247
            pickY -= 6

        if pickY <= 526:
            pick_image.clip_draw(0, 0, 173, 326, pickX, pickY)

        if pickY <= 247 and cursorPos == 0:
            character1.draw(126, 215)
            loading = True

        elif pickY <= 247 and cursorPos == 1:
            character2.draw(306,215)
            loading = True

        elif pickY <= 247 and cursorPos == 2:
            character3.draw(486,215)
            loading = True

        elif pickY <= 247 and cursorPos == 3:
            character4.draw(666,215)
            loading = True

    bg.draw(400, 300)
    cursor_image.draw(122 + (178 * cursorPos), 448)

    if cursorPos == 0:
        idx1 = 1
        idx2 = 0
        idx3 = 0
        idx4 = 0
    elif cursorPos == 1:
        idx1 = 0
        idx2 = 1
        idx3 = 0
        idx4 = 0
    elif cursorPos == 2:
        idx1 = 0
        idx2 = 0
        idx3 = 1
        idx4 = 0
    elif cursorPos == 3:
        idx1 = 0
        idx2 = 0
        idx3 = 0
        idx4 = 1

def handle_event(e):
    global idx1,idx2,idx3,idx4 , cursorPos , pick ,  pickX , pickY , ch_pick

    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_LEFT):
        if cursorPos > 0:
            cursorPos -= 1
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_RIGHT):
        if cursorPos < 3:
            cursorPos += 1

    if (e.type, e.key) == (SDL_KEYDOWN, SDLK_a):
        if cursorPos == 0:
            pick = True
            pickX = 120

        elif cursorPos == 1:
            pick = True
            pickX = 300

        elif cursorPos == 2:
            pick = True
            pickX = 480

        elif cursorPos == 3:
            pick = True
            pickX = 660





def exit():
    global loading,character1,character2,character3,character4,bg ,idx1,idx2,idx3,idx4 , ch1_image , ch2_image , ch3_image, ch4_image , cursor_image , cursorPos , pick_image , pick , pickX , pickY
    del loading,character1,character2,character3,character4,bg ,idx1,idx2,idx3,idx4 , ch1_image , ch2_image , ch3_image, ch4_image , cursor_image , cursorPos , pick_image , pick , pickX , pickY
    print("del select_state")


def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()
