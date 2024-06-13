import pygame

class ScreenResult:
    def __init__(self, width, height, win=False):
        self.half_width = width // 2
        self.half_height = height // 2
        self.center = (self.half_width, self.half_width)
        self.font = pygame.font.SysFont(None, 40)
        if win:
            self.text = self.font.render("GANASTE!!!", True, (0, 255, 0))
            self.img = pygame.image.load('imagenes/astronauta_ganaste.jpeg')
        else:
            self.texto = self.font.render("Perdiste!!!", True, (0, 255, 0))
            self.img = pygame.image.load('imagenes/imagen_perdiste.jpg')
        self.text_rect = self.text.get_rect(center=(self.half_width, self.half_width))
        self.img_rect = self.img.get_rect(center=(self.half_width, self.half_height // 2))
        
        self.text_name = self.font.render("Estudiante UPCH", True, (120, 125, 0))
        self.text_name_rect = self.text.get_rect(center=(self.half_width, self.half_height + 40))



    def draw(self, screen):
        screen.blit(self.img, self.img_rect)
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text_name, self.text_name_rect)