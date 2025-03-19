1. Optimize hitbox for player
2.  if self.x_speed > 0:
    self.rect.right = p.rect.left
    if self.x_speed < 0:
    self.rect.left = p.rect.right
    if self.y_speed > 0:
    self.rect.bottom = p.rect.top
    if self.y_speed < 0:
    self.rect.top = p.rect.bottom