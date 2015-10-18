from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class ClockLayout(BoxLayout):
    time_prop = ObjectProperty(None)
