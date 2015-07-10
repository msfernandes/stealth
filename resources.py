# -*- coding: utf-8 -*-
import pyglet
import os
BASE_DIR = os.getcwd()


class Resource(object):

    def __init__(self):
        pyglet.resource.path = [BASE_DIR + '/resources']

    def __center_image_anchor_point(self, image):
        image.anchor_x = image.width / 2
        image.anchor_y = image.height / 2

    def load_image(self, resource):
        pyglet.resource.reindex()
        resource_image = pyglet.resource.image(resource)
        self.__center_image_anchor_point(resource_image)
        return resource_image
