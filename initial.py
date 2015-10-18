from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

FONT_DIR = 'fonts/'

LabelBase.register(name='Roboto',
                   fn_regular=FONT_DIR + 'Roboto-Regular.ttf',
                   fn_italic=FONT_DIR + 'Roboto-Italic.ttf',
                   fn_bold=FONT_DIR + 'Roboto-Bold.ttf',
                   fn_bolditalic=FONT_DIR + 'Roboto-BoldItalic.ttf')

BACKGROUND_COLOR = '#101215'
Window.clearcolor = get_color_from_hex(BACKGROUND_COLOR)
