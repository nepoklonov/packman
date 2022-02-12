from view.configuration import ViewConfiguration
from model.point import Point


def find_cell(configuration: ViewConfiguration, point: Point):
    i = point.y
    j = point.x
    x1 = configuration.offset_x + j * configuration.square_length
    y1 = configuration.offset_y + i * configuration.square_length
    cx = x1 + configuration.square_length / 2
    cy = y1 + configuration.square_length / 2
    return Point(cx, cy)
