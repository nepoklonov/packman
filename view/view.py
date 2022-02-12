import tkinter as tk

from model.field import Field
from model.sprites import Sprite
from view.utils import find_cell
from view.configuration import ViewConfiguration


class View:
    canvas: tk.Canvas
    config: ViewConfiguration
    field: Field

    def __init__(self, field, window: tk.Tk, config: ViewConfiguration):
        self.field = field
        self.config = config
        self.player = None
        self.food_ovals = []
        self.canvas = tk.Canvas(window, width=800, height=600)
        self.canvas.pack()

    def start(self):
        self.draw_field()
        self.player = self.draw(self.field.player)
        for f in self.field.food:
            self.food_ovals.append(self.draw(f))
        self.start_timer()

    def start_timer(self):
        if self.field.can_move():
            self.field.move()
            coordinate = self.field.player.direction * self.config.square_length
            self.canvas.move(self.field.player.type, coordinate.x, coordinate.y)

        food_index = self.field.find_food_and_eat()
        if food_index is not None:
            self.canvas.delete(self.food_ovals[food_index])
            self.food_ovals.pop(food_index)

        self.canvas.after(300, self.start_timer)

    def draw(self, sprite: Sprite):
        center = find_cell(self.config, sprite.position)
        return self.canvas.create_oval(center.x - sprite.r / 2,
                                       center.y - sprite.r / 2,
                                       center.x + sprite.r / 2,
                                       center.y + sprite.r / 2,
                                       fill=sprite.color, tag=sprite.type)

    def draw_field(self):
        for i in range(self.field.settings.height):
            for j in range(self.field.settings.width):
                x1 = self.config.offset_x + j * self.config.square_length
                y1 = self.config.offset_y + i * self.config.square_length
                x2 = x1 + self.config.square_length
                y2 = y1 + self.config.square_length
                self.canvas.create_rectangle(x1, y1, x2, y2)
