'''
Widget animation
================

This example demonstrates creating and applying a multi-part animation to
a button widget. You should see a button labelled 'plop' that will move with
an animation when clicked.
'''
from os import environ
#environ['KIVY_CLOCK'] = 'interrupt'
import kivy
kivy.require('1.0.7')

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_string('''
<MyWidget>:
    size_hint: None, None
    size: '20dp', '600dp'
    canvas:
        Color:
            rgb: .5, .5, .5
        Rectangle:
            size: self.size
            pos: self.pos
''')

class MyWidget(Widget):
    pass


class TestApp(App):

    def animate(self, instance):
        # create an animation object. This object could be stored
        # and reused each call or reused across different widgets.
        # += is a sequential step, while &= is in parallel
        animation = Animation(pos=(1000, 0), t='linear')
        animation += Animation(pos=(0, 0), t='linear')
        animation.repeat = True

        # apply the animation on the button, passed in the "instance" argument
        # Notice that default 'click' animation (changing the button
        # color while the mouse is down) is unchanged.
        animation.start(instance)

    def build(self):
        # create a button, and  attach animate() method as a on_press handler
        button = MyWidget()
        self.animate(button)
        return button


if __name__ == '__main__':
    TestApp().run()
