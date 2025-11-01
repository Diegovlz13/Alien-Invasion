import pygame

class Ship:
    """Una clase para gestionar la nave."""
    
    def __init__(self, ai_game):
        """Inicializa la nave y configura su posición inicial."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Coloca inicialmente cada nave nueva en el crentro de la parte inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Banderas de movimiento; empiezan con una bandera que no se mueve
        self.moving_right = False
        self.moving_left = False
        
        # Guarda un valor decimal para la posición horizontal exacta de la nave
        self.x = float(self.rect.x)
        
        
    def update(self):
        """Actualiza la posición de la nave en función de la bandera de moviento."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        # Actualiza el objeto rect self.x
        self.rect.x = self.x
        
        
    def blitme(self):
        """Dibuja la nave en su ubicación actual."""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Centra la nave en la pantalla."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)