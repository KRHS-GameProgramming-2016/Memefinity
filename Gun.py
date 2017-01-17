import pygame, sys, math

class Gun():
    def __init__(self, kind):
        self.kind = kind
        
        if kind == "M4A1":
            self.fireRate = 60*.25
