# -*- coding: utf-8 -*-
from configs import SCREEN_WIDTH, SCREEN_HEIGHT
from cocos.layer import Layer
from pyglet.gl import glPushMatrix, glPopMatrix
from resources import Resource
import random


class BackgroundLayer(Layer):
    BACKGROUNDS = ['level1-bg.jpg', 'level2-bg.jpg']

    def __init__(self):
        super(BackgroundLayer, self).__init__()
        resource = Resource()
        self.image = resource.load_image(random.choice(self.BACKGROUNDS))
        self.image.width = self.__scale_width()
        self.image.height = self.__scale_height()
        resource.center_image_anchor_point(self.image)

    def draw(self):
        glPushMatrix()
        self.transform()
        self.image.blit(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        glPopMatrix()

    def __scale_width(self):
        scale = float(self.image.width) / float(SCREEN_WIDTH)
        scale = float(1) / float(scale)
        return float(self.image.width) * float(scale)

    def __scale_height(self):
        scale = float(self.image.height) / float(SCREEN_HEIGHT)
        scale = float(1) / float(scale)
        return float(self.image.height) * float(scale)
