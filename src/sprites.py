# -*- coding: utf-8 -*-
from cocos.sprite import Sprite
from resources import Resource
from configs import BOARD_UNITY_WIDTH, BOARD_UNITY_HEIGHT


class WallSprite(Sprite):

    def __init__(self, pos_x, pos_y):
        resource = Resource()
        image = resource.load_image('wall.png')
        super(WallSprite, self).__init__(image)
        self.image.width = BOARD_UNITY_WIDTH
        self.image.height = BOARD_UNITY_HEIGHT
        resource.center_image_anchor_point(self.image)
        self.position = (pos_x, pos_y)
