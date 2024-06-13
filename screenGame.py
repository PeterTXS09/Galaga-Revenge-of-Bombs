from background import BackgroundMoving
from player import Player
from status import Status
from score import Score
from enemySpawner import EnemySpawner
from collisionDetector import CollisionDetector
import pygame


class ScreenGame:
    def __init__(self, screen):
        # musica:
        pygame.mixer.init()
        pygame.mixer.music.load("music/bg_music.mp3")
        pygame.mixer.music.play(-1)
        # juego
        self.screen = screen
        self.bg = BackgroundMoving(screen.get_width(), screen.get_height())
        self.enemy_spawner = EnemySpawner()
        self.collision_detector = CollisionDetector()
        self.player = Player(screen.get_height(), screen.get_width())
        self.status = Status()
        self.score = Score()
        self.score_number = 0
        self.finished = False
        self.clock = pygame.time.Clock()

    def playGame(self):
        self.player.update()
        self.player.get_bullet_manager().update()
        self.enemy_spawner.update()
        self.enemy_spawner.draw(self.screen)
        self.player.draw(self.screen)
        self.player.get_bullet_manager().draw(self.screen)
        if self.collision_detector.check_collisions(self.enemy_spawner.get_enemies(), self.player.get_bullet_manager().get_bullets()):
            self.score_number += 1
        if self.score_number % 5 == 0:
            self.enemy_spawner.change_difficulty()
        if self.score_number % 15 == 0:
            self.player.get_bullet_manager().increase_type()
        self.status.draw(self.screen, self.player.get_lives())
        self.score.draw(self.screen, self.score_number)

    def loop(self):
        while not self.finished:
            self.clock.tick(20)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.finished = True
            self.screen.fill((0, 0, 0))
            self.bg.update(self.screen)
            self.playGame()
            if not self.player.is_alive():
                print('Score final: ' + str(self.score_number))
                self.finished = True
            pygame.display.update()
