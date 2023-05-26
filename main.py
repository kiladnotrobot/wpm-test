import math
import os, pygame, time, datetime, random
import sys

from buttons import *
from utils import *


class Game:
    def __init__(self):
        self.sec_t = None
        self.width = WIDTH
        self.height = HEIGHT
        self.lang = False

        self.game_folder = os.path.dirname(__file__)
        self.img_folder = os.path.join(self.game_folder, 'assets')

        self.menu_background = pygame.image.load('assets/main_menu.png')
        self.menu_background = pygame.transform.smoothscale(surface=self.menu_background,
                                                            size=(self.width, self.height))

        self.loading_background = pygame.image.load('assets/type-speed-open.png')
        self.loading_background = pygame.transform.smoothscale(surface=self.loading_background,
                                                               size=(self.width, self.height))

        self.settings_background = pygame.image.load('assets/settings_background.png')
        self.settings_background = pygame.transform.smoothscale(surface=self.settings_background,
                                                                size=(self.width, self.height))

        self.game_background = pygame.image.load('assets/main_background.png')
        self.game_background = pygame.transform.smoothscale(surface=self.game_background,
                                                            size=(self.width, self.height))

        self.credits_background = pygame.image.load('assets/credits_background.png')
        self.credits_background = pygame.transform.smoothscale(surface=self.credits_background,
                                                               size=(self.width, self.height))

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('ПЕЧАТАЛКА')

        self.current_scene = None
        self.correct_word_counter = 0



    def change_lang(self):
        self.lang = not self.lang

    def kostil_quit(self):
        pygame.quit()
        sys.exit()

    def reset(self):

        self.screen.blit(self.loading_background, (0, 0))
        pygame.display.update()

    def start_screen(self):
        self.reset()

        start_button = Button(250, 80, GREY, BLUE_LIGHT, screen=self.screen)
        settings_button = Button(250, 80, GREY, BLUE_LIGHT, screen=self.screen)
        credits_button = Button(250, 80, GREY, BLUE_LIGHT, screen=self.screen)
        quit_button = Button(250, 80, GREY, BLUE_LIGHT, screen=self.screen)
        start = True
        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
                    self.kostil_quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        start = False
                        self.kostil_quit()

            self.screen.blit(self.menu_background, (0, 0))
            start_button.draw(675, 400, 'СТАРТ', action=self.game_cycle)
            settings_button.draw(675, 500, 'НАСТРОЙКИ', action=self.settings_menu)
            credits_button.draw(675, 600, 'АВТОРЫ', action=self.credits_menu)
            quit_button.draw(675, 700, 'ВЫХОД', action=self.kostil_quit)

            clock = pygame.time.Clock()
            pygame.display.update()
            clock.tick(FPS)

    def game_cycle(self):
        self.correct_word_counter = 0
        words = self.get_list_of_words()

        self.reset()
        time.sleep(1)

        self.screen.fill((0, 0, 0, 0))
        self.sec_t = datetime.datetime.now()

        input_box = InputBox(self.width, self.height, self.screen)
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.kostil_quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.kostil_quit()

                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        if words[0].lower() == input_box.text.lower():
                            self.correct_word_counter += 1
                        else:
                            pass
                        words.pop(0)
                input_box.handle_event(event)

            self.screen.blit(self.game_background, (0, 0))
            l = (datetime.datetime.now() - self.sec_t)
            t = datetime.time(l.seconds // 3600, l.seconds // 60, l.seconds % 60)

            debug(l.seconds, 10, 10)
            if l.seconds == TIMER:
                running = False
                self.end_screen()
                pygame.display.update()

            clock = pygame.time.Clock()

            render_input_text(words, font_for_game, self.width, self.height, self.screen, text=input_box.text)

            render_input_field(self.width, self.height, self.screen)
            input_box.update()
            input_box.draw(self.screen)

            restart_button = Button(100, 100, BLUE_LIGHT, GREY, screen=self.screen)
            restart_button.draw_button_with_icon(1500, 0, 'r', action=self.start_screen)

            pygame.display.update()
            clock.tick(FPS)

    def settings_menu(self):
        self.reset()
        settings = True
        while settings:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings = False
                    self.kostil_quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        settings = False
                        self.kostil_quit()

            self.screen.blit(self.settings_background, (0, 0))

            go_back_button = Button(250, 80, GREY, BLUE_LIGHT, screen=self.screen)
            go_back_button.draw(675, 800, 'НАЗАД', action=self.start_screen)

            language_checkbox = Button(50, 50, BLUE_LIGHT, GREY, screen=self.screen, change_lang_func=self.change_lang,
                                       current_lang=self.lang)
            language_checkbox.zv_icons_draw(950, 450)

            debug('Английский язык??',600,460)

            clock = pygame.time.Clock()
            pygame.display.update()
            clock.tick(FPS)

    def credits_menu(self):
        self.reset()
        credits = True
        while credits:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    credits = False
                    self.kostil_quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        credits = False
                        self.kostil_quit()

            self.screen.blit(self.credits_background, (0, 0))

            go_back_button = Button(250, 80, GREY, BLUE_LIGHT, screen=self.screen)
            go_back_button.draw(675, 800, 'НАЗАД', action=self.start_screen)

            clock = pygame.time.Clock()
            pygame.display.update()
            clock.tick(FPS)

    def end_screen(self):
        self.reset()
        end = True
        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = False
                    self.kostil_quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        end = False
                        self.kostil_quit()

            self.screen.fill(BLACK)

            go_back_button = Button(250, 80, GREY, BLUE_LIGHT, screen=self.screen)
            go_back_button.draw(675, 800, 'НАЗАД', action=self.start_screen)

            debug(f'Ваша скорость печати - {int(self.correct_word_counter / TIMER * 60)} сл/мин', 500, 450)
            clock = pygame.time.Clock()
            pygame.display.update()
            clock.tick(FPS)

    def get_list_of_words(self):
        words = []

        if self.lang:
            with open(r'assets/english.txt', 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    words.append(line.strip())

        else:
            with open(r'assets/russian.txt', 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    words.append(line.strip())

        random.shuffle(words)

        return words


if __name__ == '__main__':
    game = Game()
    game.start_screen()


