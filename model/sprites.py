from model.point import Point


class Sprite:
    position: Point
    type: str
    r: int
    color: str

    def __init__(self, position):
        self.position = position


class Player(Sprite):
    type = "player"
    r = 20
    color = "red"
    direction = Point(0, 1)


class Food(Sprite):
    type = "food"
    r = 10
    color = "green"
