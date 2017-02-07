 elif self.kind == "pistol": 
            self.image = pygame.image.load("rsc/ball/bullet.png")
            
 if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
