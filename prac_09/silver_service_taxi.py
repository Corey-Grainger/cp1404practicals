"""CP1404 Week 09 Pracs
Silver Service Taxi Class
Estimated: 15 minutes
Commenced: 11:45am
Completed: 12:01pm"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a silver service taxi."""
    flagfall = 4.5

    def __init__(self, fanciness, **kwargs):
        """Initialise a silver service taxi."""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        return super().get_fare() + self.flagfall


