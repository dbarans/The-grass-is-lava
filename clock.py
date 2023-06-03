import pygame


class Time:
    def __init__(self):
        self.current = 0
        self.past = 0
        self.time_list = []

    def calculate_time(self):
        time = pygame.time.get_ticks()
        self.current = time - self.past
        self.past += self.current
        self.time_list.append(self.current/1000)
