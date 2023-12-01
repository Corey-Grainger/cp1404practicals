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

    def handle_conversion(self):
        """Handles converting miles to kilometres."""
        miles = self.validate_miles()
        self.message = str(miles * MILES_TO_KM_CONVERSION_RATE)

    def validate_miles(self):
        """Get a valid value for miles."""
        try:
            miles = float(self.root.ids.input_field.text)
            return miles
        except ValueError:
            return 0

    def handle_increment(self, increment):
        """Handles incrementing the input_field by increment."""
        miles = self.validate_miles() + increment
        self.root.ids.input_field.text = str(miles)
        self.handle_conversion()


ConvertMilesToKm().run()

