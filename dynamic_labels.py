"""
CP1404 Practical
GUI program that has a list of names (strings) and dynamically creates a separate Label for each one.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabel(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["apple", "pear", "banana"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabel().run()
