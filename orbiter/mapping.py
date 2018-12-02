import pygame as pg


def mapping_on(planet, settings):
    """Show soil moisture image of planet."""
    last_center = planet.rect.center
    planet.image_copy = pg.transform.scale(planet.img_water, (100, 100))
    planet.image_copy.set_colorkey(settings.black)
    planet.rect = planet.image_copy.get_rect()
    planet.rect.center = last_center


def mapping_off(planet, settings):
    """Restore normal planet image."""
    planet.image_copy = pg.transform.scale(planet.img_mars, (100, 100))
    planet.image_copy.set_colorkey(settings.black)
