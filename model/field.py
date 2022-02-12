import random

from model.game_settings import FieldSettings
from model.point import Point
from model.sprites import Player, Food


class Field:
    settings: FieldSettings
    player: Player
    food: list[Food]
    score: int

    def __init__(self, settings: FieldSettings):
        self.score = 0
        self.settings = settings

        self.player = Player(Point(3, 3))

        all_cells = [Point(i, j) for i in range(self.settings.height)
                     for j in range(self.settings.width)]

        random.shuffle(all_cells)

        self.food = [Food(all_cells[i]) for i in range(7)]

    def can_move(self):
        width = self.settings.width
        height = self.settings.height
        next_position = self.player.position + self.player.direction
        return (width > next_position.x >= 0) and (height > next_position.y >= 0)

    def move(self):
        next_position = self.player.position + self.player.direction
        if self.can_move():
            self.player.position = next_position

    def find_food_and_eat(self):
        result = None
        for f in self.food:
            print(f.position, self.player.position)
            if f.position == self.player.position:
                result = f
        index = None
        if result is not None:
            index = self.food.index(result)
            self.food.remove(result)
            self.score += 1
            print("Количество очков:", self.score)
        return index
