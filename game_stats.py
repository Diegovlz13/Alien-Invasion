class GameStats:
    """Sigue las estadísticas del juego."""
    
    def __init__(self, ai_game):
        """Inicializa las estadísticas."""
        self.settings = ai_game.settings
        self.reset_stats()
        
    def reset_stats(self):
        """Inicializa las estadísticas que pueden cambiar duranre el juego."""
        self.ship_left = self.settings.ship_limit
        