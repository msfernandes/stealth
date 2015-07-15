# -*- coding: utf-8 -*-
from configs import SCREEN_WIDTH, SCREEN_HEIGHT
from cocos.director import director
from scenes import GameScene


if __name__ == '__main__':
    director.init(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, caption='Stealth')
    director.window.set_fullscreen(True)
    scene = GameScene()
    director.run(scene)
