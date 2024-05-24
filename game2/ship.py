import pygame


class Ship :
    def __init__(self, screen_surf):
        self.ship_img_surf = pygame.image.load('./img/ship.bmp').convert()
        self.ship_rect = self.ship_img_surf.get_rect()
        self.screen_surf = screen_surf
    def render(self):
        self.screen_surf.blit(self.ship_img_surf, self.ship_rect)
    def move_midbottom(self):
        self.ship_rect.midbottom = self.screen_surf.get_rect().midbottom