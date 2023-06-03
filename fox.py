import pygame
import random
import math


FOX1 = pygame.image.load("img/fox/fox1.png")
FOX2 = pygame.image.load("img/fox/fox2.png")
FOX3 = pygame.image.load("img/fox/fox3.png")
FOX4 = pygame.image.load("img/fox/fox4.png")
FOX5 = pygame.image.load("img/fox/fox5.png")
FOX6 = pygame.image.load("img/fox/fox6.png")
FOX7 = pygame.image.load("img/fox/fox7.png")
FOX8 = pygame.image.load("img/fox/fox8.png")


class Fox:
    def __init__(self):
        self.velocity = 6
        self.rotation_vel = 12
        self.angle = 0
        self.hitbox = FOX1
        self.image = FOX1
        self.img_count = 0
        self.img_count2 = 0
        self.direction = 0
        self.images = [FOX1, FOX2, FOX3, FOX4, FOX5, FOX6, FOX7, FOX8]
        self.starting_pos = (400, 440)
        self.x = self.starting_pos[0]
        self.y = self.starting_pos[1]
        self.current_steps = []
        self.learned_steps = []

    def animate_fox(self):
        if self.img_count2 > 2:
            self.image = self.images[self.img_count]
            if self.img_count < 7:
                self.img_count += 1
            else:
                self.img_count = 0
            self.img_count2 = 0

        else:
            self.img_count2 += 1

    def rotate_image(self, window):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(
            center=self.image.get_rect(topleft=(self.x, self.y)).center
        )
        window.blit(rotated_image, new_rect.topleft)

    def draw(self, window):
        self.animate_fox()
        self.rotate_image(window)

    def rotate(self, left=False, right=True):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def move_fox(self, direction):
        if direction == 0:
            self.rotate(right=True)
        elif direction == 1:
            self.rotate(left=True)
        self.move_forward()

    def generate_move(self):
        direction = random.randint(0, 2)
        self.current_steps.append(direction)
        self.move_fox(direction)

    def move_forward(self):
        radians = math.radians(self.angle)
        horizontal = math.sin(radians) * self.velocity
        vertical = math.cos(radians) * self.velocity
        self.y -= horizontal
        self.x += vertical

    def collide(self, mask, x=0, y=0):
        fox_mask = pygame.mask.from_surface(self.hitbox)
        offset = (int(self.x - x), int(self.y - y))
        point = mask.overlap(fox_mask, offset)
        return point

    def start_position(self):
        self.angle = 0
        self.x = self.starting_pos[0]
        self.y = self.starting_pos[1]

    def remember_steps(self):
        if len(self.current_steps) >= len(self.learned_steps):
            self.learned_steps = []
            for i in range(len(self.current_steps) - 6):
                self.learned_steps.append(self.current_steps[i])
        self.current_steps = []
