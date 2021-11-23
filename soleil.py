import random
import pygame
from pygame.math import Vector2
from planetes import planetes

class soleil :
    def __init__(self):
        self.rayon = 50
        self.couleur = (255, 255, 0)
        self.position = (500, 500)
        self.masse = 15
        self.gravite = 50

    def attraction(self, planetes):
        pass


    def statique(self):
        pass


    def draw (self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)