import tkinter as tk

from controller.controller import Controller
from model.field import Field
from model.game_settings import FieldSettings
from view.configuration import ViewConfiguration

# Model, View, Controller
# Model -- правила игры, текущая ситуация
# View -- отображение объектов
# Controller -- управление, реакции на пользовательские действия

from view.view import View

window = tk.Tk()
window.geometry("800x600")

field_settings = FieldSettings(8, 8)
field = Field(field_settings)

configuration = ViewConfiguration(
    square_length=30,
    offset_x=15,
    offset_y=40
)

view = View(field, window, configuration)
view.start()

controller = Controller(window, field)
controller.start()

window.mainloop()
