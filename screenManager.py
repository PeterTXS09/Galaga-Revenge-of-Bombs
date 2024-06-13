from screenGame import ScreenGame


class ScreenManager:
    def __init__(self, screen):
        self.screen = screen
        self.screenGame = ScreenGame(self.screen)

    def playGame(self):
        self.screenGame.loop()