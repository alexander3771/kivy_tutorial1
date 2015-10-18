import time

from kivy.app import App
from kivy.properties import Clock

from initial import *
from elements import *


class ClockApp(App):
    def update_time(self, nap):
        self.root.ids.time.text = time.strftime('[b]%H[/b].%M.%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)


if __name__ == '__main__':
    ClockApp().run()
