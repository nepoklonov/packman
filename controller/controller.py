import tkinter as tk
from model.field import Field
from model.point import Point


class Controller:
    window: tk.Tk
    field: Field

    def __init__(self, window, field):
        self.window = window
        self.field = field

    def move(self, dx: int, dy: int):
        self.field.player.direction = Point(dx, dy)

    def start(self):
        self.window.bind("<Up>", lambda e: self.move(0, -1))
        self.window.bind("<Down>", lambda e: self.move(0, 1))
        self.window.bind("<Left>", lambda e: self.move(-1, 0))
        self.window.bind("<Right>", lambda e: self.move(1, 0))
