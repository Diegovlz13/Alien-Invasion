class Settings:
    """Una clase para guardar toda la configuración de Alien Invasion."""
    
    def __init__(self):
        """Inicializa la configuración del juego."""
        # Configuración de la pantalla
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230) # Gris claro
        
        # Configuración de la nave
        self.ship_speed = 4.0
        
        # Configuración de las balas
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Configuraciones de alien
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction de 1 representa derecha; -1 representa izquiera
        self.fleet_direction = 1
        
        # Configuraciones de estadísticas
        self.ship_limit = 3
        
        