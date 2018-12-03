import os
import math
import random
import pygame as pg


class Satellite(pg.sprite.Sprite):
    """Satellite that rotates to face planet."""
    basedir = os.path.dirname(__file__)
    sat_img_path = os.path.join(basedir, 'assets/satellite.png')
    crash_img_path = os.path.join(basedir, 'assets/satellite_crash_40x33.png')
    sound_byte = os.path.join(basedir, 'assets/thrust_audio.ogg')

    def __init__(self, background, settings):
        super().__init__()
        self.background = background
        self.settings = settings
        self.img_sat = pg.image.load(self.sat_img_path).convert()
        self.img_crash = pg.image.load(self.crash_img_path).convert()
        self.image = self.img_sat
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.settings.black)
        self.x = random.randrange(315, 425)
        self.y = random.randrange(70, 180)
        self.dx = random.choice([-3, 3])
        self.dy = 0
        self.heading = 0
        self.fuel = 1000
        self.mass = 1
        self.distance = 0
        self.thrust = pg.mixer.Sound(self.sound_byte)
        self.thrust.set_volume(self.settings.sound_volume)

    def thruster(self, dx, dy):
        """Execute actions associate with firing thrusters."""
        self.dx += dx
        self.dy += dy
        self.fuel -= 2
        self.thrust.play()

    def check_keys(self):
        """Check for key presses and fire thrusters."""
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            self.thruster(dx=0.05, dy=0)
        if keys[pg.K_LEFT]:
            self.thruster(dx=-0.05, dy=0)
        if keys[pg.K_UP]:
            self.thruster(dx=0, dy=-0.05)
        if keys[pg.K_DOWN]:
            self.thruster(dx=0, dy=0.05)

    def locate(self, planet):
        """Calculate distance and heading to planet."""
        px, py = planet.x, planet.y
        dist_x = self.x - px
        dist_y = self.y - py
        # Get direction to planet and point satellite.
        planet_dir_radians = math.atan2(dist_x, dist_y)
        # PyGame uses degrees.
        self.heading = planet_dir_radians * 180 / math.pi
        self.heading -= 90 # sprite travels tail-first
        self.distance = math.hypot(dist_x, dist_y)

    def rotate(self):
        """Rotate satellite using degrees so dish faces planet."""
        self.image = pg.transform.rotate(self.img_sat, self.heading)
        self.rect = self.image.get_rect()

    def path(self):
        """Update Satellite's position and draw line to trace orbital path."""
        last_center = (self.x, self.y)
        self.x += self.dx
        self.y += self.dy
        pg.draw.line(self.background, self.settings.white, last_center, (self.x, self.y))

    def update(self):
        """Update satellite object during game."""
        self.check_keys()
        self.rotate()
        self.path()
        self.rect.center = (self.x, self.y)
        if self.dx == 0 and self.dy == 0:
            self.image = self.img_crash
            self.image.set_colorkey(self.settings.black)
