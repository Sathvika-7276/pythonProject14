"""
CP1404 Practical
GUI program to make an app that lets the user enter and clear their name, and greets them when
a button is pressed.
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        self.root.ids.output_label.text = "Please enter your name"
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
