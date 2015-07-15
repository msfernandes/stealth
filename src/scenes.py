# -*- coding: utf-8 -*-
from cocos.scene import Scene
from layers import BackgroundLayer
from board import Board


class GameScene(Scene):

    def __init__(self):
        super(GameScene, self).__init__()
        bg = BackgroundLayer()
        self.add(bg, z=0)
        self.board = Board()
        self.add(self.board)
