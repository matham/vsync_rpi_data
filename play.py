from os import environ
environ['KIVY_CLOCK'] = 'free_only'
from time import clock

from kivy.uix.label import Label
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window


class MyApp(App):

    t = clock()
    count = 0
    label = None
    flip = 0
    ev = None
    rate = 30.
    tt = t

    def build(self):
        self.ev = Clock.schedule_interval_free(self.tick, 0)
        Window.fbind('on_flip', self.flippy)
        self.label = Label(text='0')
        return self.label

    def tick(self, *largs):
        t = clock()
        if t - self.tt < 1 / self.rate:
			return
        
        self.tt = t
        self.count += 1
        self.label.text = str(int(self.label.text) + 1)

        if t - self.t >= 1:
            print(self.count / (t - self.t), self.count - self.flip)
            self.t = t
            self.flip = 0
            self.count = 0

    def flippy(self, *largs):
        self.flip += 1


if __name__ == '__main__':
    MyApp().run()
