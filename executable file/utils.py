import random
from constants import *
import pygame
import datetime



pygame.init()

def debug(info, x, y):
    display_surface = pygame.display.get_surface()
    debug_surf = font_for_game.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    display_surface.blit(debug_surf, debug_rect)


def render_input_text(words, font_for_game, width, height, screen, text):
    word_field = pygame.draw.rect(screen, GREY, (320, 170, 960, 60), 0, 10)
    x, y = word_field.center
    words_res = ''

    for i in words:
        if len(words_res + ' ' + i) < 50:
            words_res += f' {i}'
        else:
            break

    counter = 0
    for i in range(len(text)):
        if len(text) <= len(words[0]):
            if (words[0][i]).lower() != (text[i]).lower():
                break
            elif (words[0][i]).lower() == (text[i]).lower() :
                counter += 1
        else:
            break
    text_surface = font_for_game.render(words_res, True, WHITE)
    correct_text_surface = font_for_game.render(words_res[0:counter+1],True,GREEN)

    text_offset_x = (width - x * 2)
    text_offset_y = (height / 6 - y / 2) / 2
    text_rect = text_surface.get_rect(topleft=(320 + text_offset_x, 150 + text_offset_y))
    correct_text_rect = correct_text_surface.get_rect(topleft=(320 + text_offset_x, 150 + text_offset_y))
    screen.blit(text_surface, text_rect)
    screen.blit(correct_text_surface, correct_text_rect)


def render_input_field(width, height, screen):
    input_field = pygame.draw.rect(screen, GREY, (320, 280, 960, 60),0, 10)

class InputBox:

    def __init__(self, width, height, screen, text=''):
        self.rect = pygame.draw.rect(screen, WHITE,(325, 280, 960,60),0, 10)
        self.color = WHITE
        self.text = text
        self.txt_surface = font_for_game.render(text, True, self.color)
        self.active = True

    def handle_event(self, event):
        if len(self.text) > 30:
            self.text = self.text[:-1]


        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:

                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font_for_game.render(self.text, True, self.color)


    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))