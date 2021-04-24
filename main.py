from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_widht, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_widht,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:    
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < win_height- 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.x > 5:    
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.x < win_height- 80:
            self.rect.y += self.speed
