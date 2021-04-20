"""
"Hello World" in Kivy
"""
from kivy.app import App
from kivy.app import Widget


# Create a custom derived Kivy App class
class HelloWorld(App):
    def build(self):
        self.root = Widget()
        return self.root  # build() should always return a widget object

    def try_this(self):
        self.x = 0


# Create a custom app object and start it running
HelloWorld().run()
