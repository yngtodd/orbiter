import pygame as pg


def instruct_label(screen, text, color, x, y settings):
    """Render text to screen."""
    instruct_font = pg.font.SysFont(None, 25)
    line_spacing = 22
    for idx, line in enumerate(text):
        label = instruct_font.render(line, True, color, settings.black)
        screen.blit(label, (x, y + idx * line_spacing))


def box_label(screen, text, dimensions, settings):
    """Make fixed-size label from screen, text, and left, top, width, height."""
    readout_font = pg.font.SysFont(None, 27)
    base = pg.Rect(dimensions)
    pg.draw.rect(screen, settings.white, base, 0)
    label = readout_font.render(text, True, settings.black)
    label_rect = label.get_rect(center=base.center)
    screen.blit(label, label_rect)
