from kivy.app import App
from initial import *
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex('#101215')


class ClockApp(App):
    pass


if __name__ == '__main__':
    ClockApp().run()
