import pygame as pg


def cast_shado(screen):
    """Add optional terminator and shadow behind planet to screen."""
    shadow = pg.Surface((400, 100), flags=pg.SRCALPHA) # (Width, Height)
    shadow.fill((0, 0, 0, 210))
    screen.blit(shadow, (0, 270)) # tuple is top left coordinates
