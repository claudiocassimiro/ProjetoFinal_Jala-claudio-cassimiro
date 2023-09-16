import random
import pygame
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer
from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE

POWER_UPS = [
  Shield(),
  Hammer(),
]

class PowerUpManager:
  def __init__(self):
    self.power_ups = []
    self.when_appars = 0
  
  def generate_power_up(self, score):
    if len(self.power_ups) == 0 and self.when_appars == score:
      self.when_appars += random.randint(200, 300)
      self.power_ups.append(POWER_UPS[random.randint(0, 1)])

  def update(self, score, game_speed, player):
    self.generate_power_up(score)
    for power_up in self.power_ups:
      power_up.update(game_speed, self.power_ups)
      if player.dino_rect.colliderect(power_up.rect):
        power_up.start_time = pygame.time.get_ticks()
        player.shield = True
        player.has_power_up = True
        player.type = power_up.type
        if player.type == SHIELD_TYPE:
            player.power_up_time = power_up.start_time + (power_up.duration * 1000)
        elif player.type == HAMMER_TYPE:
            player.power_up_time = power_up.start_time + (power_up.duration * 1500)
        self.power_ups.remove(power_up)
  
  def reset_power_ups(self):
    self.power_ups = []
    self.when_appars = random.randint(200, 300)

  def draw(self, screen):
    for power_up in self.power_ups:
      power_up.draw(screen)