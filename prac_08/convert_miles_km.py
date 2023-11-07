"""CP1404 Week 8 Pracs
Convert Miles to Kilometres Program
Estimated = 20 minutes
Time Commenced 7:21pm
Time Completed: 7:48"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION_RATE = 1.60934


class ConvertMilesToKm(App):
    """App with GUI to convert miles to km."""
    message = StringProperty()

    def build(self):
        """Construct conversion app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.message = ""
        return self.root

    def handle_conversion(self, value):
        """Handles converting miles to kilometres"""
        try:
            self.message = str(float(value) * MILES_TO_KM_CONVERSION_RATE)
        except ValueError:
            self.message = "0.0"

    def handle_increment(self, input_field, increment):
        """Handles incrementing the input_field by increment"""
        try:
            input_field.text = str(float(input_field.text) + increment)
        except ValueError:
            input_field.text = str(0.0 + increment)


ConvertMilesToKm().run()
