import os
import pygame as pg

from orbiter.bodies import Mars
from orbiter.bodies import Satellite

from orbiter.settings import Settings
from orbiter.rendering import GameText
from orbiter.rendering import box_label
from orbiter.rendering import instruct_label
from orbiter.rendering.shadow import cast_shadow

from orbiter.physics import calc_eccentricity

from orbiter.mapping import (
    mapping_on, mapping_off
)


def main():
    pg.init()

    os.environ['SDL_VIDEO_WINDOW_POS'] = '700, 100'
    screen = pg.display.set_mode((800, 645), pg.FULLSCREEN)
    pg.display.set_caption('Mars Orbiter')
    background = pg.Surface(screen.get_size())
    pg.mixer.init()

    gametext = GameText()

    settings = Settings()
    planet = Mars(settings)
    planet_sprite = pg.sprite.Group(planet)
    sat = Satellite(background, settings)
    sat_sprite = pg.sprite.Group(sat)

    dist_list = []
    eccentricity = 1
    eccentricity_calc_interval = 5

    clock = pg.time.Clock()
    fps = 30
    tick_count = 0

    mapping_enabled = False

    running = True
    while running:
        clock.tick(fps)
        tick_count += 1
        dist_list.append(sat.distance)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                screen = pg.display.set_mode((800, 645))
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                background.fill(settings.black)
            elif event.type == pg.KEYUP:
                sat.thrust.stop()
                mapping_off(planet, settings)
            elif mapping_enabled:
                if event.type == pg.KEYDOWN and event.key == pg.K_m:
                    mapping_on(planet, settings)

        sat.locate(planet)
        planet.gravity(sat)

        if tick_count % (eccentricity_calc_interval * fps) == 0:
            eccentricity = calc_eccentricity(dist_list)
            dist_list = []

        screen.blit(background, (0, 0))

        if sat.fuel <= 0:
            instruct_label(screen, ['Fuel Depleted!'], settings.red, 340, 195, settings)
            sat.dx = 2
        elif sat.distance <= 68:
            instruct_label(screen, ['Atmospheric Entry!'], settings.red, 320, 195, settings)
            sat.dx = 0
            sat.dy = 0

        if eccentricity < 0.05 and sat.distance >= 69 and sat.distance <= 120:
            map_instruct = ['Press & hold M to map soil moisture']
            instruct_label(screen, map_instruct, settings.lt_blue, 250, 175, settings)
            mapping_enabled = True
        else:
            mapping_enabled = False

        planet_sprite.update()
        sat_sprite.update()
        sat_sprite.draw(screen)

        if pg.time.get_ticks() <= 15000:
            instruct_label(screen, gametext.intro_text, settings.green, 145, 100, settings)

        box_label(screen, 'Dx', (70, 20, 75, 20), settings)
        box_label(screen, 'Dy', (150, 20, 80, 20), settings)
        box_label(screen, 'Altitude', (240, 20, 160, 20), settings)
        box_label(screen, 'Fuel', (410, 20, 160, 20), settings)
        box_label(screen, 'Eccentricity', (580, 20, 150, 20), settings)

        box_label(screen, '{:.1f}'.format(sat.dx), (70, 50, 75, 20), settings)
        box_label(screen, '{:.1f}'.format(sat.dy), (150, 50, 80, 20), settings)
        box_label(screen, '{:.1f}'.format(sat.distance), (240, 50, 160, 20), settings)
        box_label(screen, '{}'.format(sat.fuel), (410, 50, 160, 20), settings)
        box_label(screen, '{:.8f}'.format(eccentricity), (580, 50, 150, 20), settings)

        instruct_label(screen, gametext.instruct_text0, settings.white, 10, 575, settings)
        instruct_label(screen, gametext.instruct_text1, settings.white, 570, 510, settings)

        cast_shadow(screen)
        pg.draw.rect(screen, settings.white, (1, 1, 798, 643), 1)

        pg.display.flip()


if __name__=='__main__':
    main()
