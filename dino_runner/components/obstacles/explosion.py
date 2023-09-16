from dino_runner.utils.constants import EXPLOSION
from dino_runner.components.obstacles.obstacle import Obstacle

class Explosion(Obstacle):
  def __init__(self, rect_x, rect_y):
    super().__init__(EXPLOSION, 0)
    self.rect.y = rect_y
    self.rect.x = rect_x
    self.step_index = 0
  
  def draw(self, screen):
    screen.blit(self.image[0], self.rect)
    self.step_index += 1

    if self.step_index >= 10:
        self.step_index = 0