# -*- coding: utf-8 -*-
from configs import SCREEN_WIDTH, SCREEN_HEIGHT
from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer
import cocos


class L(Layer):

    def __init__(self):
        super(L, self).__init__()
        label = cocos.text.Label('Hello, world',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        label.position = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
        self.add(label)

if __name__ == '__main__':
    director.init(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, caption='Stealth')
    director.window.set_fullscreen(True)
    l = L()
    scene = Scene(l)
    director.run(scene)
