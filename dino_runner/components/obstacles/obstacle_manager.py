import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.explosion import Explosion
from dino_runner.utils.constants import HAMMER_TYPE, EXPLOSION_SOUND, DEATH_SOUND, DINO_DEAD
from dino_runner.utils.sound_utils import play_sound_effect


class ObstacleManager:
  def __init__(self):
    self.obstacles = []

  def update(self, game):
    obstacle_type = [
      Cactus(),
      Bird(),
    ]

    if len(self.obstacles) == 0:
      self.obstacles.append(obstacle_type[random.randint(0, 1)])
    
    for obstacle in self.obstacles:
      obstacle.update(game.game_speed, self.obstacles)
      if game.player.dino_rect.colliderect(obstacle.rect):
        if not game.player.has_power_up:
          game.player.image = DINO_DEAD[0]
          play_sound_effect(DEATH_SOUND)
          pygame.time.delay(3000)
          game.playing = False
          game.death_count += 1
          break
        elif game.player.type == HAMMER_TYPE:
          rect_x = obstacle.rect.x
          rect_y = obstacle.rect.y
          explosion = Explosion(rect_x, rect_y)
          play_sound_effect(EXPLOSION_SOUND)
          self.obstacles.append(explosion)
          self.obstacles.remove(obstacle)
  
  def reset_obstacles(self):
    self.obstacles = []

  def draw(self, screen):
    for obstacle in self.obstacles:
      obstacle.draw(screen)
