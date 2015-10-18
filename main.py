import time

from kivy.app import App
from kivy.properties import Clock

from initial import *
from elements import *


class ClockApp(App):
    sw_seconds = 0
    sw_started = False

    def update(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
            minutes, seconds = divmod(self.sw_seconds, 60)
            self.root.ids.stopwatch.text = '{minutes:02d}:{seconds:02d}.[size=40]{miliseconds:02d}[/size]'.format(
                minutes=int(minutes), seconds=int(seconds), miliseconds=int(seconds * 100 % 100))

    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def start_stop(self):
        self.root.ids.start_stop.text = 'Start' if self.sw_started else 'Stop'
        self.sw_started = not self.sw_started

    def reset(self):
        self.root.ids.start_stop.text = 'Start'
        self.sw_seconds = 0
        self.sw_started = True
        self.update(0)
        self.sw_started = False


if __name__ == '__main__':
    ClockApp().run()
