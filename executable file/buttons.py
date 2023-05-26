import time

import pygame
from constants import *


class Button:
    def __init__(self, width, height, inactive_color, active_color, screen, change_lang_func=None, current_lang = None):
        self.screen = screen
        self.width = width
        self.height = height
        self.inactive_clr = inactive_color
        self.active_clr = active_color
        self.chang_lang = change_lang_func

        self.current_lang = current_lang
        self.LANGUAGE_CHOOSE = current_lang

    def draw(self, x, y, message, action=None, font=font_main):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(surface=self.screen, color=self.active_clr, rect=(x, y, self.width, self.height),
                             border_radius=10)
            if click[0] == 1:
                if action is not None:
                    action()
                    pygame.time.delay(150)
        else:
            pygame.draw.rect(surface=self.screen, color=self.inactive_clr, rect=(x, y, self.width, self.height),
                             border_radius=10)

        text_width, text_height = font.size(message)

        text_offset_x = (self.width - text_width) / 2
        text_offset_y = (self.height - text_height) / 2

        display_surface = pygame.display.get_surface()

        shadow_surf = font.render(str(message), True, BLUE)
        shadow_rect = shadow_surf.get_rect(topleft=(x + text_offset_x + 1, y + text_offset_y + 1))
        display_surface.blit(shadow_surf, shadow_rect)

        debug_surf = font.render(str(message), True, 'White')
        debug_rect = debug_surf.get_rect(topleft=(x + text_offset_x, y + text_offset_y))
        display_surface.blit(debug_surf, debug_rect)

    def draw_button_with_icon(self, x, y, message, action=None, font=icons_font, inactive_color=RED):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        display_surface = pygame.display.get_surface()

        text_width, text_height = font.size(message)
        text_offset_x = (self.width - text_width) / 2
        text_offset_y = text_height / 45

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:

            shadow_surf = font.render(str(message), True, inactive_color)
            shadow_rect = shadow_surf.get_rect(topleft=(x + text_offset_x, y + text_offset_y))
            display_surface.blit(shadow_surf, shadow_rect)

            if click[0] == 1:
                if action is not None:
                    action()
                    pygame.time.delay(150)
        else:
            debug_surf = font.render(str(message), True, 'White')
            debug_rect = debug_surf.get_rect(topleft=(x + text_offset_x, y + text_offset_y))
            display_surface.blit(debug_surf, debug_rect)

    def zv_icons_draw(self, x, y, font=ZV_ICONS):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        display_surface = pygame.display.get_surface()

        text_width, text_height = font.size('v')
        text_offset_x = (self.width - text_width) / 2
        text_offset_y = text_height / 45

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            if not self.LANGUAGE_CHOOSE:
                shadow_surf = font.render('z', True, RED)
                shadow_rect = shadow_surf.get_rect(topleft=(x + text_offset_x, y + text_offset_y))
                display_surface.blit(shadow_surf, shadow_rect)
            else:
                shadow_surf = font.render('v', True, RED)
                shadow_rect = shadow_surf.get_rect(topleft=(x + text_offset_x, y + text_offset_y))
                display_surface.blit(shadow_surf, shadow_rect)

            if click[0] == 1:
                self.chang_lang()
                self.LANGUAGE_CHOOSE = not self.LANGUAGE_CHOOSE
                pygame.time.delay(200)
        else:
            if not self.LANGUAGE_CHOOSE:
                debug_surf = font.render('z', True, 'White')
                debug_rect = debug_surf.get_rect(topleft=(x + text_offset_x, y + text_offset_y))
                display_surface.blit(debug_surf, debug_rect)
            else:
                debug_surf = font.render('v', True, 'White')
                debug_rect = debug_surf.get_rect(topleft=(x + text_offset_x, y + text_offset_y))
                display_surface.blit(debug_surf, debug_rect)

        #print(self.LANGUAGE_CHOOSE)
