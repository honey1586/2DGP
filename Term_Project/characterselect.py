from pico2d import *
import gfw_image

RES_DIR = 'res/'

class SelCh:
    player = []
    image = []

    def __init__(self):
        if SelCh.image == None:
            for i in range(0,2):
                SelCh.image[i] = gfw_image.load(RES_DIR + 'Select_Character'+ i)