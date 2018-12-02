import os
import math
import random
import pygame as pg


class Mars(pg.sprite.Sprite):
    """Planet that rotates and projects gravitational field."""
    basedir = os.path.dirname(__file__)
    mars_img_path = os.path.join(basedir, 'assets/mars.png')
    water_img_path = os.path.join(basedir, 'assets/mars_water.png')

    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.img_mars = pg.image.load(self.mars_img_path).convert()
        self.img_water = pg.image.load(self.water_img_path).convert()
        self.image_copy = pg.transform.scale(self.img_mars, (100, 100))
        self.image_copy.set_colorkey(self.settings.black)
        self.rect = self.image_copy.get_rect()
        self.image = self.image_copy
        self.mass = 2000
        self.x = 400
        self.y = 320
        self.rect.center = (self.x, self.y)
        self.angle = math.degrees(0)
        self.rotate_by = math.degrees(0.01)

    def rotate(self):
        """Rotate the planet image with each game loop."""
        last_center = self.rect.center
        self.image = pg.transform.rotate(self.image_copy, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = last_center
        self.angle += self.rotate_by

    def gravity(self, satellite):
        """Calculate impact of gravity on satellite."""
        G = 1.0
        dist_x = self.x - satellite.x
        dist_y = self.y - satellite.y
        distance = math.hypot(dist_x, dist_y)
        # normalize to unit vector
        dist_x /= distance
        dist_y /= distance
        # apply gravity
        force = G * (satellite.mass * self.mass) / (math.pow(distance, 2))
        satellite.dx += (dist_x * force)
        satellite.dy += (dist_y * force)

    def update(self):
        """Rotate the planet."""
        self.rotate()
