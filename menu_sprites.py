########################################################################################################################
# Import statements
import pygame


# All Images: Tetris by Emily L from <a href="https://thenounproject.com/browse/icons/term/tetris/" target="_blank" title="Tetris Icons">Noun Project</a>

class LShapeSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(LShapeSprite, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Images/Lshape.png'))
        self.images.append(pygame.image.load('Images/Lshape1.png'))
        self.images.append(pygame.image.load('Images/Lshape2.png'))
        self.images.append(pygame.image.load('Images/Lshape3.png'))
        self.images.append(pygame.image.load('Images/Lshape4.png'))
        self.images.append(pygame.image.load('Images/Lshape5.png'))
        self.images.append(pygame.image.load('Images/Lshape6.png'))
        self.images.append(pygame.image.load('Images/Lshape7.png'))
        self.images.append(pygame.image.load('Images/Lshape8.png'))
        self.images.append(pygame.image.load('Images/Lshape9.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(500, 500, 100, 100)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class ZShapeSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(ZShapeSprite, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Images/Zshape.png'))
        self.images.append(pygame.image.load('Images/Zshape1.png'))
        self.images.append(pygame.image.load('Images/Zshape2.png'))
        self.images.append(pygame.image.load('Images/Zshape3.png'))
        self.images.append(pygame.image.load('Images/Zshape4.png'))
        self.images.append(pygame.image.load('Images/Zshape5.png'))
        self.images.append(pygame.image.load('Images/Zshape6.png'))
        self.images.append(pygame.image.load('Images/Zshape7.png'))
        self.images.append(pygame.image.load('Images/Zshape8.png'))
        self.images.append(pygame.image.load('Images/Zshape8.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(500, 200, 100, 100)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class TShapeSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TShapeSprite, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Images/Tshape.png'))
        self.images.append(pygame.image.load('Images/Tshape1.png'))
        self.images.append(pygame.image.load('Images/Tshape2.png'))
        self.images.append(pygame.image.load('Images/Tshape3.png'))
        self.images.append(pygame.image.load('Images/Tshape4.png'))
        self.images.append(pygame.image.load('Images/Tshape5.png'))
        self.images.append(pygame.image.load('Images/Tshape6.png'))
        self.images.append(pygame.image.load('Images/Tshape7.png'))
        self.images.append(pygame.image.load('Images/Tshape8.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(10, 500, 100, 100)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class OShapeSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(OShapeSprite, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Images/Oshape.png'))
        self.images.append(pygame.image.load('Images/Oshape1.png'))
        self.images.append(pygame.image.load('Images/Oshape2.png'))
        self.images.append(pygame.image.load('Images/Oshape3.png'))
        self.images.append(pygame.image.load('Images/Oshape4.png'))
        self.images.append(pygame.image.load('Images/Oshape5.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(10, 200, 100, 100)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
