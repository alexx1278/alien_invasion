import datetime

class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""
    def __init__(self, ai_settings):
        """Инициализирует статистику."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Игра запускается в неактивном состоянии.
        self.game_active = False
        # Рекорд не должен сбрасываться.
        f = open('bestscore')
        self.high_score = int(f.read())
        f.close()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def bestscore(self):
        if self.score >= self.high_score:
            f= open('bestscore', 'w')
            f.write(str(self.high_score))
            f.close()
            f = open('stat', 'w')
            t = {}
            t[str(datetime.datetime.now())] = self.high_score
            f.write(str(t))
            f.close()
