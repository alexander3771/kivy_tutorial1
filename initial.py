from kivy.core.text import LabelBase

FONT_DIR = 'fonts/'

LabelBase.register(name='Roboto',
                   fn_regular=FONT_DIR + 'Roboto-Regular.ttf',
                   fn_italic=FONT_DIR + 'Roboto-Italic.ttf',
                   fn_bold=FONT_DIR + 'Roboto-Bold.ttf',
                   fn_bolditalic=FONT_DIR + 'Roboto-BoldItalic.ttf')
