"""CP1404 Week 08 Pracs
Dynamic Labels program
Estimated: 25 minutes
Commenced: 8:31pm
Completed 8:54pm:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = ["John", "Jill", "Angela", "Marco"]

class DynamicLabels(App):
    """Build the dynamic labels demo app"""
    def __init__(self, names=NAMES, **kwargs):
        super().__init__(**kwargs)
        self.names = names

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            dynamic_label = Label(text=name)
            dynamic_label.color = (1,0,0,1)
            self.root.ids.name_labels.add_widget(dynamic_label)

DynamicLabels().run()
