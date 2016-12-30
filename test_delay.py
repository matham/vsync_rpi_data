
from time import clock
from os import environ
environ['KIVY_CLOCK'] = 'free_only'

import RPi.GPIO as GPIO

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window

widget = Builder.load_string('''
<MyWidget@Widget>:
	c: 0
    canvas:
        Color:
            rgb: self.c, self.c, self.c
        Rectangle:
            size: self.size
            pos: self.pos

MyWidget
''')


class TestApp(App):

    t = clock()
    rate = 30.
    tt = t
    flip = 0
    count = 0
    pin = 37
    state = False

    def build(self):
		
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

        self.ev = Clock.schedule_interval_free(self.tick, 0)
        Window.fbind('on_flip', self.flippy)
        return widget

    def tick(self, *largs):
        t = clock()
        if t - self.tt < 1 / self.rate:
			return

        self.tt = t
        self.count += 1
        widget.c = 0. if widget.c == 1. else 1.

        if t - self.t >= 1:
            print(self.count / (t - self.t), self.count - self.flip)
            self.t = t
            self.flip = 0
            self.count = 0

    def flippy(self, *largs):
        GPIO.output(self.pin, self.state)
        self.state = not self.state
        self.flip += 1


if __name__ == '__main__':
    TestApp().run()
